# api/main.py

import os
import logging
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel
import pickle
import pandas as pd

origins = [
    "http://localhost:3000",
]

# Load environment variables or set default values
SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/api.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dummy user database
fake_users_db = {
    "user@example.com": {
        "username": "user@example.com",
        "full_name": "Test User",
        "hashed_password": pwd_context.hash("password"),
    }
}

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, username: str):
    return db.get(username)

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username)
    if user is None:
        raise credentials_exception
    return user

# Load the trained model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the scaler
with open('model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Initialize the FastAPI app
app = FastAPI(
    title="Predictive Maintenance API",
    description="An API that predicts equipment failure.",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for input data
class EquipmentData(BaseModel):
    temperature: float
    vibration: float
    pressure: float
    operational_hours: int

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post('/predict', summary="Predict Equipment Failure", description="Provide equipment data to predict failure.", tags=["Prediction"])
async def predict(data: EquipmentData, current_user: dict = Depends(get_current_user)):
    try:
        logger.info(f"User {current_user['username']} requested a prediction.")

        # Convert input data to DataFrame
        input_data = pd.DataFrame([data.dict()])

        # Feature engineering
        input_data['temp_pressure_interaction'] = input_data['temperature'] * input_data['pressure']
        input_data['vibration_squared'] = input_data['vibration'] ** 2

        # Reorder columns to match the training data
        feature_columns = ['temperature', 'vibration', 'pressure', 'operational_hours', 'temp_pressure_interaction', 'vibration_squared']
        input_data = input_data[feature_columns]

        # Scale the input data
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_scaled)

        # Map prediction to result
        result = "Failure" if prediction[0] == 1 else "No Failure"

        logger.info(f"Prediction result: {result}")

        # Return result
        return {'prediction': result}
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

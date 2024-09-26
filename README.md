# Predictive Maintenance Application

## Project Overview

This project is a full-stack application for predictive maintenance using a machine learning model. It includes:

- Generating synthetic equipment data.
- Training a machine learning model.
- Developing a FastAPI backend API with JWT authentication.
- Creating a React frontend.
- Containerization with Docker and Docker Compose.
- Automated testing with pytest.

## Prerequisites

- **Python 3.10** (recommended for compatibility)
- Docker and Docker Compose
- Node.js and npm (for the React frontend)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd predictive_maintenance_project
```

### 2. Create and Activate a Virtual Environment

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Generate Synthetic Data

```bash
python data/generate_data.py
```

### 5. Perform Data Analysis (Optional)

```bash
python scripts/data_analysis.py
```

### 6. Train the Machine Learning Model

```bash
python model/train_model.py
```
### 7. Run the FastAPI Application

```bash
uvicorn api.main:app --reload
```
Access the API documentation at http://127.0.0.1:8000/docs

### 8. Run Automated Tests

```bash
pytest tests/test_api.py
```

### 9. Run the Frontend (Optional)
Navigate to the frontend directory and follow the instructions to set up and run the React app.

### 10. Using Docker and Docker Compose
Build and run the application using Docker Compose:

```bash
docker-compose up --build
```

### Notes
Ensure you're using Python 3.10 to avoid compatibility issues.
Always activate your virtual environment before installing packages and running the application.
Update requirements.txt whenever you add new dependencies.
If you encounter any errors, check that all dependencies are installed and that the virtual environment is activated.
Conclusion
This application demonstrates a full-stack solution for predictive maintenance, incorporating machine learning, API development, frontend interface, containerization, and automated testing.
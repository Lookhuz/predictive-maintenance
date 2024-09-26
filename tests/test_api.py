# tests/test_api.py

import sys
import os
import pytest
from httpx import AsyncClient
from api.main import app

# Add the project root directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

@pytest.mark.asyncio
async def test_predict():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Get token
        response = await ac.post("/token", data={"username": "user@example.com", "password": "password"})
        assert response.status_code == 200
        token = response.json()["access_token"]

        headers = {"Authorization": f"Bearer {token}"}

        # Test prediction endpoint
        payload = {
            "temperature": 85.0,
            "vibration": 0.6,
            "pressure": 35.0,
            "operational_hours": 5000
        }

        response = await ac.post("/predict", json=payload, headers=headers)
        assert response.status_code == 200
        assert "prediction" in response.json()

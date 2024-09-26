# Dockerfile (Backend)

# Stage 1: Build stage
FROM python:3.10-slim as builder

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Run data generation and data analysis scripts
RUN python data/generate_data.py
RUN python scripts/data_analysis.py

# Stage 2: Runtime stage
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Create a directory for data/images
RUN mkdir -p /app/data

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Update PATH
ENV PATH=/root/.local/bin:$PATH

# Copy the application code
COPY --from=builder /app /app

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest

# Copy source code
COPY . .

# Run the app (Flask)
CMD ["python", "app.py"]

EXPOSE 5000

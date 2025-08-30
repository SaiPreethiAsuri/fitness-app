# ACEestFitness and Gym - Flask Web Application

This repository contains a **Flask web application** for fitness and gym management, along with **Pytest unit tests**, a **Dockerfile** for containerization, and a **GitHub Actions workflow** for CI/CD.

---

## 📥 Local Setup

### Prerequisites
- Python 3.11 installed
- pip installed

### Steps to set up and run locally

1. **Clone the repository**
```bash
      git clone https://github.com/SaiPreethiAsuri/fitness-app.git

2. **Install dependencies**
      pip install -r requirements.txt
Run the Flask application
      python app.py
The app will run on: http://127.0.0.1:5000

3.** Running Tests Locally**
Execute the unit tests using Pytest:
      python -m pytest
This will run all tests in the tests/ directory and show the summary.

### Docker Instructions
Build the Docker image
      docker build -t my-flask-app .
Run the container
      docker run -p 5000:5000 my-flask-app

### GitHub Actions CI/CD Overview
This project includes a GitHub Actions workflow (.github/workflows/ci.yml) that runs automatically on every push to any branch.
**The pipeline performs the following steps:**
Checkout the repository
Uses actions/checkout@v3 to fetch the latest code.
Set up Docker Buildx
Configures Docker for building images in the CI environment.
Build Docker image
Creates a container image named my-flask-app:ci with all dependencies and source code.
Run unit tests inside the container
Executes Pytest to verify the application functionality and stability.

The workflow ensures that every code change is automatically tested and validated in a containerized environment before deployment.
This setup ensures you can run, test, and containerize the application both locally and via CI/CD.


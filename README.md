# Flask Jenkins CI/CD Pipeline

A simple Flask web application with automated CI/CD pipeline using Jenkins.

## Project Structure

```
flask-jenkins-app/
├── app.py              # Main Flask application
├── test_app.py         # Unit tests using pytest
├── requirements.txt    # Python dependencies
├── Jenkinsfile        # Jenkins pipeline configuration
└── README.md          # Project documentation
```

## Application Endpoints

- `GET /` - Home endpoint with welcome message
- `GET /health` - Health check endpoint
- `GET /api/greet/<name>` - Personalized greeting endpoint

## Running Locally

```bash
# Install dependencies
pip3 install -r requirements.txt

# Run the application
python3 app.py

# Run tests
pytest test_app.py -v
```

## Jenkins Pipeline Stages

1. **Clone Repository** - Pulls latest code from GitHub
2. **Install Dependencies** - Installs Python packages from requirements.txt
3. **Run Unit Tests** - Executes pytest test suite
4. **Build Application** - Validates and packages the application
5. **Deploy Application** - Copies files to deployment directory

## Requirements

- Python 3.x
- Jenkins with Pipeline plugin
- GitHub repository access

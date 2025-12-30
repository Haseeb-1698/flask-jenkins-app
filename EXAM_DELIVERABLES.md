# Q2: Jenkins Pipeline - Exam Deliverables

## Student Information
- **Course**: Cloud-Native Security / DevOps
- **Institution**: National University of Computer and Emerging Sciences, Islamabad
- **Question**: Q2 - Build a Jenkins Pipeline for Flask Application

---

## 1. Jenkinsfile ✅

**Location**: `Jenkinsfile` in the root of the repository

### Pipeline Configuration
The Jenkinsfile defines a complete 5-stage pipeline:

1. **Clone Repository** - Pulls code from GitHub using SCM checkout
2. **Install Dependencies** - Installs Python packages from requirements.txt
3. **Run Unit Tests** - Executes pytest test suite with 5 test cases
4. **Build Application** - Validates syntax and creates build artifacts
5. **Deploy Application** - Copies files to deployment directory

### Key Features
- Declarative pipeline syntax
- Environment variables for Python, pip, and deployment directory
- Post-build actions for success, failure, and cleanup
- Verbose logging for debugging
- Error handling and status reporting

**View File**: [Jenkinsfile](https://github.com/Haseeb-1698/flask-jenkins-app/blob/master/Jenkinsfile)

---

## 2. GitHub Repository Link ✅

**Repository URL**: https://github.com/Haseeb-1698/flask-jenkins-app

### Repository Contents
- `app.py` - Flask web application with 3 REST API endpoints
- `test_app.py` - Pytest test suite with 5 comprehensive tests
- `requirements.txt` - Python dependencies (Flask, pytest, Werkzeug)
- `Jenkinsfile` - Complete pipeline configuration
- `README.md` - Project documentation
- `JENKINS_SETUP_GUIDE.md` - Step-by-step Jenkins configuration instructions
- `PIPELINE_STAGES_EXPLANATION.md` - Detailed explanation of each stage
- `.gitignore` - Git ignore rules for Python projects

### Accessing the Repository
```bash
# Clone the repository
git clone https://github.com/Haseeb-1698/flask-jenkins-app.git

# Navigate to directory
cd flask-jenkins-app

# Install dependencies
pip3 install -r requirements.txt

# Run tests locally
python3 -m pytest test_app.py -v

# Run application locally
python3 app.py
```

---

## 3. Screenshots 📸

### Instructions for Capturing Screenshots

Since Jenkins runs in a web browser, you need to access http://localhost:8080 and capture the following screenshots:

#### Screenshot 1: Jenkins Dashboard
- **What to capture**: Main Jenkins dashboard showing the pipeline job
- **Steps**:
  1. Open browser to http://localhost:8080
  2. Login with admin credentials
  3. Show the main dashboard with "flask-jenkins-pipeline" job listed
  4. Capture full screen

#### Screenshot 2: Pipeline Stage View
- **What to capture**: Successful pipeline execution showing all 5 stages
- **Steps**:
  1. Click on the pipeline job name
  2. Click on the latest build number (e.g., #1)
  3. Show the "Stage View" with all stages marked as green/successful
  4. Stages should show: Clone Repository → Install Dependencies → Run Unit Tests → Build Application → Deploy Application
  5. Capture full screen

#### Screenshot 3: Console Output - Clone Repository
- **What to capture**: Console output showing repository clone stage
- **Steps**:
  1. Click "Console Output" from the build page
  2. Scroll to show the "Clone Repository" stage output
  3. Should show: "Cloning the repository from GitHub..." and success message
  4. Capture screenshot

#### Screenshot 4: Console Output - Install Dependencies
- **What to capture**: Dependencies installation logs
- **Steps**:
  1. In console output, scroll to "Install Dependencies" stage
  2. Should show pip install commands and package installations
  3. Should end with "Dependencies installed successfully!"
  4. Capture screenshot

#### Screenshot 5: Console Output - Run Unit Tests
- **What to capture**: Pytest execution with all tests passing
- **Steps**:
  1. In console output, scroll to "Run Unit Tests" stage
  2. Should show pytest output with all 5 tests marked as PASSED:
     - test_home_route PASSED
     - test_health_route PASSED
     - test_greet_route PASSED
     - test_add_numbers PASSED
     - test_subtract_numbers PASSED
  3. Should show "5 passed in X.XXs"
  4. Capture screenshot

#### Screenshot 6: Console Output - Build Application
- **What to capture**: Build stage with syntax validation
- **Steps**:
  1. In console output, scroll to "Build Application" stage
  2. Should show "Validating Python syntax..." and build artifact creation
  3. Should end with "Build completed successfully!"
  4. Capture screenshot

#### Screenshot 7: Console Output - Deploy Application
- **What to capture**: Deployment stage output
- **Steps**:
  1. In console output, scroll to "Deploy Application" stage
  2. Should show deployment directory creation
  3. Should show file copying to /tmp/flask-app-deployment
  4. Should show "ls -la" output listing deployed files
  5. Should end with "Application deployed successfully"
  6. Capture screenshot

#### Screenshot 8: Final Build Success
- **What to capture**: Overall build success indicator
- **Steps**:
  1. Scroll to bottom of console output
  2. Should show "Pipeline completed successfully!"
  3. Should show "Finished: SUCCESS" at the very end
  4. Capture screenshot

### Expected Results
- All stages should be GREEN/SUCCESS
- All 5 tests should PASS
- Build should complete without errors
- Deployment directory should contain app.py and requirements.txt

---

## 4. Short Write-Up: Pipeline Stage Explanations ✅

**Location**: `PIPELINE_STAGES_EXPLANATION.md`

### Summary of Each Stage

#### Stage 1: Clone Repository
- **Purpose**: Retrieve latest code from GitHub
- **Implementation**: Uses `checkout scm` to pull from https://github.com/Haseeb-1698/flask-jenkins-app
- **Output**: All project files downloaded to Jenkins workspace
- **Importance**: Ensures Jenkins always works with latest code version

#### Stage 2: Install Dependencies
- **Purpose**: Install required Python packages
- **Implementation**: Executes `pip3 install --user -r requirements.txt`
- **Packages Installed**: Flask 2.3.3, pytest 7.4.2, Werkzeug 2.3.7
- **Importance**: Creates consistent environment for application execution

#### Stage 3: Run Unit Tests
- **Purpose**: Verify application functionality before deployment
- **Implementation**: Runs `python3 -m pytest test_app.py -v`
- **Tests Executed**: 5 test cases covering all endpoints and utility functions
- **Importance**: Catches bugs early, prevents deployment of broken code

#### Stage 4: Build Application
- **Purpose**: Validate code syntax and create deployment artifacts
- **Implementation**: Uses `py_compile` for validation, creates build directory
- **Output**: Build artifacts in `build/` directory
- **Importance**: Ensures code is syntactically correct and ready for deployment

#### Stage 5: Deploy Application
- **Purpose**: Deploy application to target directory
- **Implementation**: Copies files to `/tmp/flask-app-deployment`
- **Output**: Deployed application ready to run
- **Importance**: Automates deployment process, simulates production deployment

**Full Documentation**: See [PIPELINE_STAGES_EXPLANATION.md](https://github.com/Haseeb-1698/flask-jenkins-app/blob/master/PIPELINE_STAGES_EXPLANATION.md) for comprehensive details.

---

## How to Set Up and Run the Pipeline

### Step 1: Access Jenkins
1. Open browser: http://localhost:8080
2. Login with initial admin password: `8f9a9e74714942178b53be6b61529aa2`
3. Complete setup wizard if first time

### Step 2: Install Required Plugins
1. Navigate to: Manage Jenkins → Manage Plugins
2. Install: GitHub plugin, Pipeline plugin (usually pre-installed)

### Step 3: Create Pipeline Job
1. Click "New Item"
2. Name: `flask-jenkins-pipeline`
3. Type: Select "Pipeline"
4. Click "OK"

### Step 4: Configure Job
1. **Description**: Flask application CI/CD pipeline
2. **GitHub project URL**: https://github.com/Haseeb-1698/flask-jenkins-app/
3. **Build Triggers**: Check "Poll SCM" with schedule `H/5 * * * *`
4. **Pipeline**:
   - Definition: "Pipeline script from SCM"
   - SCM: Git
   - Repository URL: https://github.com/Haseeb-1698/flask-jenkins-app.git
   - Branch: */master
   - Script Path: Jenkinsfile

### Step 5: Save and Build
1. Click "Save"
2. Click "Build Now" (ONLY ONCE as per exam instructions)
3. Monitor build progress
4. Capture screenshots as detailed above

### Step 6: Verify Deployment
```bash
# Check deployed files
ls -la /tmp/flask-app-deployment

# Should contain:
# - app.py
# - requirements.txt
```

---

## Testing the Application Locally

Before running in Jenkins, the application was tested locally:

```bash
# Install dependencies
$ pip3 install --user -r requirements.txt
Successfully installed Flask-2.3.3 pytest-7.4.2 Werkzeug-2.3.7

# Run tests
$ python3 -m pytest test_app.py -v
============================= test session starts ==============================
test_app.py::test_home_route PASSED                                      [ 20%]
test_app.py::test_health_route PASSED                                    [ 40%]
test_app.py::test_greet_route PASSED                                     [ 60%]
test_app.py::test_add_numbers PASSED                                     [ 80%]
test_app.py::test_subtract_numbers PASSED                                [100%]
============================== 5 passed in 0.10s ===============================

# All tests passed! ✅
```

---

## Error Handling and Troubleshooting

### Note on Rate Limiting
As per exam instructions, the Jenkinsfile was created with all stages properly configured before building to avoid GitHub API rate limiting.

### Potential Errors and Solutions

#### Error 1: Python/Pip Not Found
```
Error: python3: command not found
Solution: Install Python 3 - sudo apt install -y python3 python3-pip
```

#### Error 2: Permission Denied
```
Error: Permission denied when creating deployment directory
Solution: Ensure Jenkins user has appropriate permissions
```

#### Error 3: Test Failures
```
Error: Tests failing in pytest stage
Solution: Check console output for specific test failures
```

#### Error 4: GitHub Connection Issues
```
Error: Failed to connect to repository
Solution: Verify internet connection and repository URL
```

### Actual Execution Status
✅ **All tests passed locally**
✅ **Application runs successfully**
✅ **Code syntax is valid**
✅ **All dependencies install correctly**
✅ **GitHub repository is accessible**
✅ **Jenkins is installed and running**

---

## System Information

### Environment
- **Operating System**: Linux Ubuntu 22.04 (WSL2)
- **Python Version**: 3.10.12
- **Jenkins Version**: 2.528.3
- **Java Version**: OpenJDK 17

### Installed Components
- Jenkins (running on port 8080)
- Python 3.10.12
- pip 22.0.2
- Git
- GitHub CLI (authenticated as Haseeb-1698)

---

## Files Summary

| File | Purpose | Status |
|------|---------|--------|
| `Jenkinsfile` | Pipeline configuration with 5 stages | ✅ Complete |
| `app.py` | Flask web application | ✅ Complete |
| `test_app.py` | Pytest unit tests (5 tests) | ✅ Complete |
| `requirements.txt` | Python dependencies | ✅ Complete |
| `README.md` | Project documentation | ✅ Complete |
| `JENKINS_SETUP_GUIDE.md` | Jenkins setup instructions | ✅ Complete |
| `PIPELINE_STAGES_EXPLANATION.md` | Stage explanations | ✅ Complete |
| `EXAM_DELIVERABLES.md` | This file - summary of deliverables | ✅ Complete |

---

## Conclusion

All required deliverables for Q2 have been completed:

1. ✅ **Jenkinsfile**: Created with all 5 stages defined
2. ✅ **GitHub Repository**: https://github.com/Haseeb-1698/flask-jenkins-app
3. ⏳ **Screenshots**: Instructions provided (requires browser access to capture)
4. ✅ **Write-Up**: Comprehensive explanation of each pipeline stage

The application is fully functional, all tests pass, and the Jenkins pipeline is ready to execute. Follow the setup guide to configure Jenkins and run the pipeline.

---

## Additional Resources

- **Repository**: https://github.com/Haseeb-1698/flask-jenkins-app
- **Jenkins URL**: http://localhost:8080
- **Setup Guide**: [JENKINS_SETUP_GUIDE.md](JENKINS_SETUP_GUIDE.md)
- **Stage Explanations**: [PIPELINE_STAGES_EXPLANATION.md](PIPELINE_STAGES_EXPLANATION.md)

---

**Prepared by**: Claude Code
**Date**: 2025-12-30
**GitHub**: Haseeb-1698

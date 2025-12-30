# Jenkins Pipeline Setup Guide

## Step-by-Step Instructions to Configure Jenkins Job

### Prerequisites
- Jenkins is running at http://localhost:8080
- Initial admin password: `8f9a9e74714942178b53be6b61529aa2`
- GitHub repository: https://github.com/Haseeb-1698/flask-jenkins-app

### Step 1: Access Jenkins

1. Open your web browser and navigate to: **http://localhost:8080**
2. Enter the initial admin password if prompted
3. Complete the setup wizard if this is your first time

### Step 2: Install Required Plugins

1. Go to **Manage Jenkins** → **Manage Plugins**
2. Click on the **Available** tab
3. Search for and install the following plugins:
   - **GitHub plugin**
   - **Pipeline plugin** (usually pre-installed)
   - **Git plugin** (usually pre-installed)
4. Click **Install without restart**
5. Wait for installation to complete

### Step 3: Create a New Pipeline Job

1. From the Jenkins dashboard, click **New Item**
2. Enter item name: `flask-jenkins-pipeline`
3. Select **Pipeline** as the job type
4. Click **OK**

### Step 4: Configure the Pipeline Job

#### General Settings
1. Add description: "Flask application CI/CD pipeline with automated testing and deployment"
2. Check **GitHub project** (if available)
3. Enter Project URL: `https://github.com/Haseeb-1698/flask-jenkins-app/`

#### Build Triggers
1. Check **Poll SCM** to enable periodic repository polling
2. In the Schedule field, enter: `H/5 * * * *` (polls every 5 minutes)
   - Alternatively, use **GitHub hook trigger for GITScm polling** if you've set up webhooks

#### Pipeline Configuration
1. Under **Pipeline** section:
   - Definition: Select **Pipeline script from SCM**
   - SCM: Select **Git**
   - Repository URL: `https://github.com/Haseeb-1698/flask-jenkins-app.git`
   - Credentials: Leave as **none** (public repository)
   - Branch Specifier: `*/master` or `*/main` (depending on your default branch)
   - Script Path: `Jenkinsfile`

2. Click **Save**

### Step 5: Install Python and Pip on Jenkins Agent

Before running the pipeline, ensure Python and pip are available in Jenkins:

```bash
# These commands were already executed on the system:
sudo apt update
sudo apt install -y python3 python3-pip
```

### Step 6: Run the Pipeline

1. Click **Build Now** from the job page
2. Watch the build progress in the **Build History** section
3. Click on the build number (e.g., #1) to see details
4. Click **Console Output** to see detailed logs

### Step 7: Expected Pipeline Execution

The pipeline will execute the following stages in order:

1. **Clone Repository** - Pulls code from GitHub
2. **Install Dependencies** - Installs Flask, pytest, and other packages
3. **Run Unit Tests** - Executes pytest test suite
4. **Build Application** - Validates Python syntax and creates build artifacts
5. **Deploy Application** - Copies files to deployment directory (`/tmp/flask-app-deployment`)

### Troubleshooting

#### Issue: Python or Pip Not Found
**Solution:** Ensure Python 3 and pip3 are installed on the Jenkins server:
```bash
sudo apt install -y python3 python3-pip
```

#### Issue: Permission Denied
**Solution:** Ensure Jenkins user has appropriate permissions:
```bash
sudo usermod -a -G sudo jenkins
sudo systemctl restart jenkins
```

#### Issue: GitHub Connection Failed
**Solution:** Check internet connectivity and verify repository URL is correct

#### Issue: Tests Failing
**Solution:** Check the console output for specific test failures and verify the code is correct

### Monitoring the Pipeline

- **Blue Ocean UI** (optional): Install Blue Ocean plugin for better visualization
- **Build History**: Shows all build executions with status
- **Console Output**: Detailed logs for each build
- **Stage View**: Visual representation of pipeline stages

### Notes for Exam Submission

- Only build **ONCE** after all changes to Jenkinsfile are complete
- If errors occur, document them in the write-up
- Take screenshots of:
  - Jenkins dashboard with job
  - Successful build with all stages
  - Console output showing each stage
  - Final deployment confirmation

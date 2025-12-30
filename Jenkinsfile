pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        PIP = 'pip3'
        DEPLOY_DIR = '/tmp/flask-app-deployment'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository from GitHub...'
                checkout scm
                echo 'Repository cloned successfully!'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    ${PIP} install --user -r requirements.txt
                    echo "Dependencies installed successfully!"
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests with pytest...'
                sh '''
                    ${PYTHON} -m pytest test_app.py -v --tb=short
                    echo "All tests passed successfully!"
                '''
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building the Flask application...'
                sh '''
                    echo "Validating Python syntax..."
                    ${PYTHON} -m py_compile app.py
                    echo "Creating build artifacts..."
                    mkdir -p build
                    cp app.py build/
                    cp requirements.txt build/
                    echo "Build completed successfully!"
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying the application...'
                sh '''
                    echo "Creating deployment directory..."
                    mkdir -p ${DEPLOY_DIR}

                    echo "Copying application files to deployment directory..."
                    cp -r build/* ${DEPLOY_DIR}/
                    cp requirements.txt ${DEPLOY_DIR}/

                    echo "Application deployed successfully to ${DEPLOY_DIR}"
                    ls -la ${DEPLOY_DIR}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
            echo 'All stages executed without errors.'
        }
        failure {
            echo 'Pipeline failed!'
            echo 'Please check the logs for error details.'
        }
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}

pipeline {
    agent { label 'selenium-node' }

    environment {
        VENV_DIR = 'jenkinsvenv'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Cloning repository...'
                git 'https://github.com/amanoj319319319/ZebraPythonSelenium.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                echo '🐍 Creating virtual environment...'
                sh 'python3 -m venv $VENV_DIR'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing Python dependencies...'
                sh '''
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '✅ Running pytest...'
                sh '''
                    source $VENV_DIR/bin/activate
                    pytest --html=Reports/report.html --self-contained-html
                '''
            }
        }

        stage('Archive Report') {
            steps {
                echo '🗂 Archiving HTML report...'
                archiveArtifacts artifacts: 'Reports/report.html', onlyIfSuccessful: true
            }
        }
    }

    post {
        always {
            echo '🎯 CI Pipeline finished'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}


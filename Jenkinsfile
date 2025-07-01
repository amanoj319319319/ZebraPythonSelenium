pipeline {
    agent {
        label 'selenium-node'  // Make sure your Jenkins agent has this label
    }

    environment {
        VENV_DIR = 'jenkinsvenv'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Cloning repository...'
                git url: 'https://github.com/amanoj319319319/ZebraPythonSelenium.git', branch: 'master'
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
                sh '''#!/bin/bash
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🚀 Running tests...'
                sh '''#!/bin/bash
                source $VENV_DIR/bin/activate
                pytest --html=Reports/report.html --self-contained-html
                '''
            }
        }

        stage('Archive Report') {
            steps {
                echo '📄 Archiving HTML report...'
                archiveArtifacts artifacts: 'Reports/report.html', allowEmptyArchive: false
            }
        }
    }

    post {
        success {
            echo '✅ Build successful!'
        }
        failure {
            echo '❌ Build failed!'
        }
        always {
            echo '🎯 CI Pipeline finished'
        }
    }
}

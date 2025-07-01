pipeline {
    agent { label 'selenium-node' }

    environment {
        VENV_DIR = 'jenkinsvenv'
        REPORT_PATH = 'Reports/report.html'
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
                archiveArtifacts artifacts: "$REPORT_PATH", allowEmptyArchive: false
            }
        }
    }

    post {
        success {
            emailext (
                subject: "✅ Selenium Test Report - SUCCESS [${env.JOB_NAME} #${env.BUILD_NUMBER}]",
                body: """<p>Hi,</p>
                         <p>The Jenkins build <b>#${env.BUILD_NUMBER}</b> completed successfully.</p>
                         <p>Job: <a href="${env.BUILD_URL}">${env.JOB_NAME}</a></p>
                         <p>Attached is the test report.</p>""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: 'bubbududdu0101@gmail.com, ankitakaushik0101@gmail.com',
                attachmentsPattern: "$REPORT_PATH",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                subject: "❌ Selenium Test Report - FAILURE [${env.JOB_NAME} #${env.BUILD_NUMBER}]",
                body: """<p>Hi,</p>
                         <p>The Jenkins build <b>#${env.BUILD_NUMBER}</b> has failed.</p>
                         <p>Job: <a href="${env.BUILD_URL}">${env.JOB_NAME}</a></p>
                         <p>Please check the logs.</p>""",
                to: 'bubbududdu0101@gmail.com, ankitakaushik0101@gmail.com'
                mimeType: 'text/html'
            )
        }
        always {
            echo '🎯 CI Pipeline completed'
        }
    }
}

pipeline {
agent any
stages {
stage('Checkout') {
steps { git 'https://github.com/your-repo/shopping-app.git' }
}
stage('Build Docker Image') {
steps { sh 'docker build -t shopping-app .' }
}
stage('Run Tests') {
steps { sh 'python -m pytest tests/' }
}
stage('SonarQube Scan') {
steps { sh 'sonar-scanner' }
}
}
}
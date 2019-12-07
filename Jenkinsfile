pipeline {
    agent any

    stages{
        stage('Prep') {
            steps {
                sh 'pip install pytest --user'
                sh 'pip install flake8 --user'
            }
        }
        stage('Unit Testing') {
            steps {
                sh 'python -m pytest'
            }
        }
        stage('Linting/Style Checking') {
            steps {
                sh 'python -m flake8'
            }
        }

    }
}

pipeline {
    agent any

    stages{
        stage('Prep') {
            steps {
                sh 'pip install pipenv'
                sh 'pipenv install pytest'
            }
        }
        stage('Unit Testing') {
            steps {
                sh 'pipenv run python -m pytest'
            }
        }
        stage('Linting/Style Checking') {
            steps {
                sh 'pipenv run python -m flake8'
            }
        }

    }
}

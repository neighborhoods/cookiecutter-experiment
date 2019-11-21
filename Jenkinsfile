pipeline {
    agent any

    stages{
        stage('Unit Testing') {
            steps {
                sh 'pip install pytest --user'
                sh 'python -m pytest'
            }
        }
        stage('Linting/Style Checking') {
            steps {
                sh 'pip install flake8 --user'
                sh 'python -m flake8'
            }
        }

    }
}

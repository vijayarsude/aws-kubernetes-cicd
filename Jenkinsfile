pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'vijay0609/kubernetes-flask-app'
        DOCKER_CREDENTIALS  = 'dockerhub-credentials'
    }
    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv --clear .venv
                .venv/bin/pip install -r app/requirements.txt
                .venv/bin/pip install pytest
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                .venv/bin/python -m pytest tests/ -v
                '''
            }
        }
        stage('Build Docker Image') {
            steps{
                sh '''
                docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .
                '''
            }
        }
        stage('Push Docker image') {
            steps {
                withCredentials([
                    usernamePassword (
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_TOKEN'
                    )
                ]){
                    sh '''
                    echo "$DOCKER_TOKEN" | docker login \
                    -u "$DOCKER_USER"    --password-stdin
                    docker push $DOCKER_IMAGE:$BUILD_NUMBER
                    '''
                }

            }
        }
    }

post {
    always {
        sh 'docker logout || true '

    }
    success {
        echo "CI pipeline successful"
    }
    failure {
        echo 'CI pipeline faild check console logs.'

    }
  }
}
pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = 'your_dockerhub_username/scientific-calculator'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running unit tests..."
                sh 'python -m unittest discover -v -s tests -p "test_*.py"'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $DOCKERHUB_REPO:${BUILD_NUMBER} .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo "Pushing image to DockerHub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                        echo "$PASS" | docker login -u "$USER" --password-stdin
                        docker tag $DOCKERHUB_REPO:${BUILD_NUMBER} $DOCKERHUB_REPO:latest
                        docker push $DOCKERHUB_REPO:${BUILD_NUMBER}
                        docker push $DOCKERHUB_REPO:latest
                    '''
                }
            }
        }

        stage('Deploy (Optional)') {
            steps {
                echo "Deploy step placeholder (can use Ansible here later)."
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs."
        }
    }
}
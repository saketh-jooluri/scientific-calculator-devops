pipeline {
    // Run on any available Jenkins agent
    agent any

    // Environment variables
    environment {
        DOCKERHUB_CREDS_ID = 'dockerhub-creds'  // Jenkins credentials ID
        DOCKER_IMAGE_NAME = "sakethjooluri/scientific-calculator-devops"
    }

    // Main stages
    stages {

        stage('1. Checkout Code') {
            steps {
                echo "Source code checked out successfully."
            }
        }

        stage('2. Run Test Cases') {
            steps {
                echo "Running unit tests..."
                sh 'python3 -m unittest discover tests'
            }
        }

        stage('3. Build Docker Image') {
            steps {
                echo "Building Docker image..."
                // Build Docker image with Jenkins build number
                sh "docker build -t ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER} ."
                sh "docker tag ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER} ${DOCKER_IMAGE_NAME}:latest"
            }
        }

        stage('4. Push Image to Docker Hub') {
            steps {
                script {
                    echo "Logging in and pushing image to Docker Hub..."
                    withCredentials([usernamePassword(
                        credentialsId: "${DOCKERHUB_CREDS_ID}", 
                        usernameVariable: 'DOCKER_USER', 
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        // Login to Docker Hub
                        sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                        // Push both the build-specific tag and latest
                        sh "docker push ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}"
                        sh "docker push ${DOCKER_IMAGE_NAME}:latest"
                    }
                }
            }
        }

        stage('5. Deploy on Local System') {
            steps {
                echo "Deploying container on the local system using Ansible..."
                sh 'ansible-playbook -i inventory deploy.yml'
            }
        }
    }

    // Post-actions
    post {
        success {
            echo "Pipeline finished successfully! Sending success email..."
            // Uncomment and configure email if needed
            /*
            emailext (
                subject: "SUCCESS: Pipeline '${env.JOB_NAME}' [${env.BUILD_NUMBER}]",
                body: "Check console output at ${env.BUILD_URL}",
                to: "your-email@example.com"
            )
            */
        }
        failure {
            echo "Pipeline failed. Sending failure email..."
            // Uncomment and configure email if needed
            /*
            emailext (
                subject: "FAILURE: Pipeline '${env.JOB_NAME}' [${env.BUILD_NUMBER}]",
                body: "Pipeline failed. Check console output at ${env.BUILD_URL}",
                to: "your-email@example.com"
            )
            */
        }
        always {
            echo "Cleaning up..."
            sh "docker logout"
        }
    }
}

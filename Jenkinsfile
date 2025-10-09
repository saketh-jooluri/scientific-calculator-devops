// Jenkinsfile

pipeline {
    // Defines where the pipeline will run. 'any' means any available agent.
    agent any

    // Environment variables used throughout the pipeline
    environment {
        // The ID of the Docker Hub credentials stored in Jenkins
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        // Your Docker Hub username and the desired image name
        DOCKER_IMAGE_NAME = "sakethjooluri/scientific-calculator-devops"
    }

    // The main stages of the CI/CD pipeline
    stages {
        stage('1. Checkout Code') {
            steps {
                // The code is already checked out automatically by Jenkins.
                // This stage now just confirms that step is complete.
                echo "Source code checked out successfully."
            }
        }

        stage('2. Run Test Cases') {
            steps {
                // Runs the Python unit tests to ensure code quality
                echo "Running unit tests..."
                sh 'python -m unittest discover tests'
            }
        }

        stage('3. Build Docker Image') {
            steps {
                // Builds the Docker image using the Dockerfile in the repo
                echo "Building Docker image..."
                // The image is tagged with the unique Jenkins build number for versioning
                sh "docker build -t ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER} ."
                // Also tag it as 'latest' for easy access
                sh "docker tag ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER} ${DOCKER_IMAGE_NAME}:latest"
            }
        }

        stage('4. Push Image to Docker Hub') {
            steps {
                script {
                    echo "Logging in and pushing image to Docker Hub..."
                    // This block securely accesses the stored Docker Hub credentials
                    withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        // Log in to Docker Hub
                        sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"

                        // Push both the build-specific tag and the 'latest' tag
                        sh "docker push ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}"
                        sh "docker push ${DOCKER_IMAGE_NAME}:latest"
                    }
                }
            }
        }

        stage('5. Deploy on Local System') {
            steps {
                // Uses Ansible to pull the new image and run the container
                echo "Deploying container on the local system using Ansible..."
                // This command executes the playbook to manage the deployment
                sh 'ansible-playbook -i inventory deploy.yml'
            }
        }
    }

    // Actions to be performed after the pipeline finishes
    post {
        // This block runs only if all stages succeed
        success {
            echo "Pipeline finished successfully! Sending success email..."
            // Optional: Send a success email. Requires Email Extension plugin.
            // emailext (
            //     subject: "SUCCESS: Pipeline '${env.JOB_NAME}' [${env.BUILD_NUMBER}]",
            //     body: "Check console output at ${env.BUILD_URL}",
            //     to: "your-email@example.com"
            // )
        }
        // This block runs only if any stage fails
        failure {
            echo "Pipeline failed. Sending failure email..."
            // Optional: Send a failure email.
            // emailext (
            //     subject: "FAILURE: Pipeline '${env.JOB_NAME}' [${env.BUILD_NUMBER}]",
            //     body: "Pipeline failed. Check console output at ${env.BUILD_URL}",
            //     to: "your-email@example.com"
            // )
        }
        // This block runs regardless of the pipeline's success or failure
        always {
            echo "Cleaning up..."
            sh "docker logout"
        }
    }
}
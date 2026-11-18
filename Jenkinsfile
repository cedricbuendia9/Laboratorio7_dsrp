pipeline {

    agent any

    stages {

        stage('Git Clone') {

            steps {
                checkout scm
            }

        }

        stage('Docker Build') {

            steps {

                sh '''
                docker build -t diabetes-online:v1 .
                '''

            }

        }

        stage('Docker Test') {

            steps {

                sh '''
                docker run -d --name diabetes-test -p 5001:5000 diabetes-online:v1
                '''

            }

        }

    }

}
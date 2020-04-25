pipeline {
  environment {
    registry = "appy385/calculator"
    registryCredential = 'docker-hub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Unit test') {
       steps {
          sh 'python -m unittest unitTest.py'
       }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
  }
}

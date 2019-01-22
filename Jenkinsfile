pipeline {
  agent any
  stages {
    stage('Commit') {
      steps {
        sh 'echo $APPENV'
      }
    }
    stage('Acceptance') {
      steps {
        sh '''APPENV=prod
echo $APPENV'''
      }
    }
    stage('Performance') {
      steps {
        sh 'echo $APPENV'
      }
    }
    stage('Promote') {
      steps {
        sh 'echo "I wouldn\'t go to..."'
      }
    }
  }
  environment {
    APPENV = 'dev'
    PROFILE = 'deveast'
  }
}
pipeline {
  agent any
  stages {
    stage('Commit') {
      steps {
        sh '$APPENV'
      }
    }
    stage('Acceptance') {
      steps {
        sh '''APPENV=prod
$APPENV'''
      }
    }
    stage('Performance') {
      steps {
        sh '$APPENV'
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
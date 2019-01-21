pipeline {
  agent any
  environment {
        APPENV  = 'dev'
        PROFILE = 'deveast'
    }
  stages {
    stage('Commit') {
      parallel {
        stage('Commit') {
          steps {
            sh '''#!/bin/bash -xe

echo $APPENV'''
          }
        }
        stage('test') {
          steps {
            input 'Must interact'
            sh '''#!/bin/bash -xe

echo $BUILD_ID
echo $DATE'''
          }
        }
        stage('test2') {
          steps {
            archiveArtifacts(artifacts: '*', onlyIfSuccessful: true)
          }
        }
      }
    }
    stage('Acceptance') {
      steps {
        sh '''#!/bin/bash -xe

echo $BUILD_ID'''
      }
    }
    stage('Performance') {
      steps {
        sh '''#!/bin/bash -xe

echo "Testing load"'''
      }
    }
    stage('Promote') {
      steps {
        sh '''#!/bin/bash -xe

echo "Promoting"'''
      }
    }
  }
}

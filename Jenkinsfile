pipeline {
  agent any
  stages {
    stage('Commit') {
      steps {
        sh '''#!/bin/bash -xe

echo $APPENV'''
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

echo "Testing load"
export APPENV = prod
echo $APPENV'''
      }
    }
    stage('Promote') {
      steps {
        sh '''#!/bin/bash -xe

echo "Promoting"'''
        archiveArtifacts '*'
      }
    }
  }
  environment {
    APPENV = 'dev'
    PROFILE = 'deveast'
  }
}
pipeline {
  agent any
  stages {
    stage('Commit - Dev') {
      steps {
        sh '''#!/bin/bash -xe

echo $APPENV
cat ./trigger.txt'''
      }
    }
    stage('Acceptance - Dev') {
      steps {
        sh '''#!/bin/bash -xe

echo $BUILD_ID'''
      }
    }
    stage('Performance - Dev') {
      steps {
        sh '''#!/bin/bash -xe

echo "Testing load"
APPENV=prod
echo $APPENV'''
      }
    }
    stage('Promote - Dev') {
      steps {
        sh '''#!/bin/bash -xe

echo "Promoting"'''
        archiveArtifacts '*'
      }
    }
    stage('Approval') {
      steps {
        input 'Approve Production Deployment'
      }
    }
    stage('Commit - Prod') {
      steps {
        sh 'echo "Mommy"'
      }
    }
    stage('Acceptance - Prod') {
      steps {
        sh 'echo "Daddy"'
      }
    }
    stage('Performance - Prod') {
      steps {
        sh 'echo "France"'
      }
    }
    stage('Promote - Prod') {
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
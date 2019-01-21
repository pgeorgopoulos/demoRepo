pipeline {
  agent any
  stages {
    stage('Commit') {
      steps {
        sh '''#!/bin/bash -xe

echo "Testing"'''
      }
    }
    stage('Acceptance') {
      steps {
        sh '''#!/bin/bash -xe

echo "Bravo"'''
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
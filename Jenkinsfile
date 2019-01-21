pipeline {
  agent none
  stages {
    stage('Commit') {
      steps {
        sh '''#!/bin/bash -xe

echo testing123'''
      }
    }
    stage('Acceptance') {
      steps {
        sh '''#!/bin/bash -xe

echo acceptanc123'''
      }
    }
    stage('Performance') {
      steps {
        sh '''#!/bin/bash -xe

echo performance'''
      }
    }
    stage('Promotion') {
      steps {
        sh '''#!/bin/bash -xe

echo promotme'''
      }
    }
  }
}
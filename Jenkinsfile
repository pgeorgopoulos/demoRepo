pipeline {
  agent any
  stages {
    stage('Commit') {
      parallel {
        stage('Commit') {
          steps {
            echo 'Commit stage is happening!'
          }
        }
        stage('Syntax Checks') {
          steps {
            sh '''echo \'Running cnf_nag_scan against CFT\'
echo \'Running pylint against application files\''''
          }
        }
        stage('Unit testing') {
          steps {
            sh '''echo \'Running unit tests\'
python unitTest.py'''
          }
        }
        stage('Docker Build') {
          steps {
            sh 'sh dockerBuild.sh $APPENV $BUILD_ID'
          }
        }
      }
    }
    stage('Acceptance') {
      parallel {
        stage('Acceptance') {
          steps {
            echo 'Building and testing environment.'
          }
        }
        stage('Build Environment, Function Test, & Security Scan') {
          steps {
            sh '''python build.py --BUILD_ID $BUILD_ID --stack_name demoStack$BUILD_ID

echo \'Here I would run function tests\'
python functionTest.py --BUILD_ID $BUILD_ID

echo \'Here I would run a security scan\''''
          }
        }
      }
    }
    stage('Performance') {
      parallel {
        stage('Performance') {
          steps {
            echo 'Performance testing is happening!'
          }
        }
        stage('Load Tests') {
          steps {
            sh 'echo \'This is where I would generate the load.\''
            sleep 2
          }
        }
      }
    }
    stage('Promote') {
      parallel {
        stage('Promote') {
          steps {
            echo 'Promoting'
          }
        }
        stage('Route Traffic') {
          steps {
            sh '''echo \'Would do this with an ELB normally but...\'

python route53.py --BUILD_ID $BUILD_ID

echo \'This is where I would tear down the old environment\''''
          }
        }
        stage('Archive') {
          steps {
            archiveArtifacts(artifacts: '*', onlyIfSuccessful: true, fingerprint: true, caseSensitive: true)
          }
        }
      }
    }
  }
  environment {
    APPENV = 'prod'
  }
}
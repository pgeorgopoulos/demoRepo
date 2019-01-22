pipeline {
  agent any
  stages {
    stage('Commit') {
      parallel {
        stage('Commit') {
          steps {
            sh 'echo "COMMIT STAGE HERE WE GO!"'
          }
        }
        stage('Syntax Checks') {
          steps {
            sh '''echo \'Running cnf_nag_scan against CFT\'
echo \'Running pylint against application files"'''
          }
        }
        stage('Unit testing') {
          steps {
            sh 'echo \'Running unit tests\''
          }
        }
        stage('Docker Build') {
          steps {
            sh 'sudo sh dockerBuild.sh $APPENV $BUILD_ID'
          }
        }
      }
    }
    stage('Acceptance') {
      parallel {
        stage('Acceptance') {
          steps {
            sh 'echo \'ACCEPTANCE HERE I COME!\''
          }
        }
        stage('Build Environment, Function Test, & Security Scan') {
          steps {
            sh '''sudo python build.py --BUILD_ID $BUILD_ID --stack_name demoStack$BUILD_ID

echo \'Here I would run function tests\'

echo \'Here I would run a security scan\''''
          }
        }
      }
    }
    stage('Performance') {
      parallel {
        stage('Performance') {
          steps {
            sh 'echo \'Performance testing is happening!\''
          }
        }
        stage('Load Tests') {
          steps {
            sh 'echo \'This is where I would generate the load.\''
          }
        }
      }
    }
    stage('Promote') {
      parallel {
        stage('Promote') {
          steps {
            sh 'echo \'The Captain becomes The Major\''
          }
        }
        stage('Route Traffic') {
          steps {
            sh '''echo \'Would do this with an ELB normally but...\'

sudo python route53.py --BUILD_ID $BUILD_ID

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
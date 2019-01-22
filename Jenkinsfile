pipeline {
  agent any
  stages {
    stage('Commit') {
      parallel {
        stage('Commit') {
          steps {
            sh 'echo "COMMIT STAGE COMMENCING"'
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
            sh 'echo \'Running unit tests\''
          }
        }
        stage('Docker Build') {
          steps {
            sh 'sudo sh build/dockerBuild.sh $APPENV $BUILD_ID'
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
        stage('Build Environment') {
          steps {
            sh 'build.py --s3_bucket_name janicejoplin$BUILD_ID --stack_name janicejoplin$BUILD_ID'
          }
        }
        stage('Function Tests') {
          steps {
            sh 'echo \'Running function tests\''
          }
        }
        stage('Security Scan') {
          steps {
            sh 'echo \'Use boto3 or aws cli to grab ELB url and scan\''
          }
        }
      }
    }
    stage('Performance') {
      parallel {
        stage('Performance') {
          steps {
            sh 'echo \'Performance testing... it\'s happening!\''
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
            sh 'echo \'Find elb from janicejoplin$BUILD_ID output and change Route53 record.\''
          }
        }
        stage('Destroy Old Environment') {
          steps {
            sh 'echo \'Goodbye World!\''
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
    PROFILE = 'prodeast'
  }
}
pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        // sh 'npm install'
        // sh 'npm build'
        echo 'building the application ...'
        echo 'Application built successfully.'
      }
    }
    stage("test") {
      steps {
        echo 'testing the application ...'
      }
    }
    stage("deploy") {
      steps {
        echo 'deploying the application ...'
      }
    }
  }
}

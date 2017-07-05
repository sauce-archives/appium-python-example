#!groovy

pipeline {
    agent {
        docker "python:3.6.1"
    }

    stages {

        stage('install dep') {
        	steps {
            	sh 'pip install -U selenium'
            	sh 'pip install Appium-Python-Client'
            }
        }

        stage("staging test") {
            when {
                expression { params.APPIUM_ENDPOINT == 'http://appium.staging.testobject.org/wd/hub' }
            }
            steps {
                lock (resource: params.TESTOBJECT_DEVICE) {
                    sh 'python appium_basic_test.py'
                }
            }
        }
        stage("test") {
            when {
                 expression { params.APPIUM_ENDPOINT != 'http://appium.staging.testobject.org/wd/hub' }
            }
            steps {
                sh 'python appium_basic_test.py'
            }
        }
    }

    post {
        failure {
            slackSend channel: "#${env.SLACK_CHANNEL}", color: "bad", message: "Python test failed against ${APPIUM_ENDPOINT} (<${BUILD_URL}|open>)", teamDomain: "${env.SLACK_SUBDOMAIN}", token: "${env.SLACK_TOKEN}"
        }
    }
}

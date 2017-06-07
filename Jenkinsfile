#!groovy

pipeline {
    agent {
        docker "python"
    }

    stages {

        stage('install dep') {
        pip install -U selenium && pip install Appium-Python-Client && python appium_basic_test.py
        	steps {
            	sh 'pip install -U selenium'
            	sh 'pip install Appium-Python-Client'
            	sh 'python appium_basic_test.py'
            }
        }
    }

    post {
        failure {
            slackSend channel: "#${env.SLACK_CHANNEL}", color: "bad", message: "Python test failed against ${APPIUM_ENDPOINT}", teamDomain: "${env.SLACK_SUBDOMAIN}", token: "${env.SLACK_TOKEN}"
        }
    }
}
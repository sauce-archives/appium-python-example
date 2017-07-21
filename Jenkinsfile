#!groovy

def runTest() {
    node {
        stage("checkout") {
            checkout scm
        }
        stage("test") {
            docker.image("python:3.6.1").inside {
                sh 'pip install -U selenium'
                sh 'pip install Appium-Python-Client'
                sh 'python appium_basic_test.py'
            }
        }
    }
}

if (env.APPIUM_ENDPOINT.contains("staging.testobject.org")) {
    lock (resource: env.TESTOBJECT_DEVICE) {
        runTest()
    }
} else {
    try {
        runTest()
        if (env.SUCCESS_NOTIFICATION_ENABLED) {
            slackSend channel: "#${env.SLACK_CHANNEL}", color: "good", message: "`${env.JOB_BASE_NAME}` passed (<${BUILD_URL}|open>)", teamDomain: "${env.SLACK_SUBDOMAIN}", token: "${env.SLACK_TOKEN}"
        }
    } catch (err) {
        if (env.APPIUM_ENDPOINT.contains("testobject.com") || env.FAILURE_NOTIFICATION_ENABLED) {
            slackSend channel: "#${env.SLACK_CHANNEL}", color: "bad", message: "`${env.JOB_BASE_NAME}` failed: $err (<${BUILD_URL}|open>)", teamDomain: "${env.SLACK_SUBDOMAIN}", token: "${env.SLACK_TOKEN}"
        }
        throw err
    }
}

#!groovy

try {
    runTest()
    if (env.SUCCESS_NOTIFICATION_ENABLED) {
        slackSend channel: "#${env.SLACK_CHANNEL}", color: "good", message: "`${env.JOB_BASE_NAME}` passed (<${BUILD_URL}|open>)", teamDomain: "${env.SLACK_SUBDOMAIN}", token: "${env.SLACK_TOKEN}"
    }
} catch (err) {
    if (isProduction() || env.FAILURE_NOTIFICATION_ENABLED) {
        slackSend channel: "#${env.SLACK_CHANNEL}", color: "bad", message: "`${env.JOB_BASE_NAME}` failed: $err (<${BUILD_URL}|open>)", teamDomain: "${env.SLACK_SUBDOMAIN}", token: "${env.SLACK_TOKEN}"
    }
    if (currentBuild.result == null || currentBuild.result == "UNSTABLE") {
        currentBuild.result = "FAILURE"
    }
    throw err
} finally {
    reportResultsToInfluxDb()
}

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

def reportResultsToInfluxDb() {
    if (env.REPORT_RESULTS.is("true")) {
        node {
            def influxDb
            if (env.INFLUX_DB) {
                influxDb = env.INFLUX_DB
            } else {
                influxDb = isProduction() ? "production" : "staging"
            }
            def result = 0
            if (currentBuild.result == null) {
                currentBuild.result = "SUCCESS"
                result = 1
            }
            def customData = env.PART_OF_SLA.is("true") ? ['result': result, 'sla': true] : ['result': result, 'sla': false]
            if (env.CATEGORY != null) {
                customData.category = env.CATEGORY.toLowerCase()
            } else if (env.JOB_BASE_NAME.contains("ios")) {
                customData.category = "ios"
            } else if (env.JOB_BASE_NAME.contains("android")) {
                customData.category = "android"
            } else {
                customData.category = "unknown"
            }

            step([$class       : 'InfluxDbPublisher',
                  customData   : customData,
                  customDataMap: null,
                  customPrefix : null,
                  target       : influxDb])
        }
    }
}

def isProduction() {
    return env.APPIUM_URL && env.APPIUM_URL.contains("testobject.com")
}

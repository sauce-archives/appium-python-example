#!groovy
@Library('TestRunner') _

// For more information about TestRunner please visit https://github.com/saucelabs/pipeline-test-runner

def test = {
    sh 'pip install -U selenium'
    sh 'pip install Appium-Python-Client==0.31'
    sh 'python appium_basic_test.py'
}

TestRunner {
    dockerImage = "python:latest"
    collectJunitReport = false
    steps = test
}

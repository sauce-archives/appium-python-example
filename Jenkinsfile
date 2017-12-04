#!groovy

// For more information about TestRunner please visit https://github.com/saucelabs/pipeline-test-runner

def test = {
    sh 'pip install -U selenium'
    sh 'pip install Appium-Python-Client'
    sh 'python appium_basic_test.py'
}

TestRunner {
    dockerImage = "python:3.6.1"
    collectJunitReport = false
    steps = test
}

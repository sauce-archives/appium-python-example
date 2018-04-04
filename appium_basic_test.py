import unittest
import os
from appium import webdriver

class TestClass(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['testobject_api_key'] = os.environ['TESTOBJECT_API_KEY']
        desired_caps['platformName'] = os.getenv('PLATFORM_NAME', 'ANDROID')

        if os.getenv('TESTOBJECT_DEVICE'):
            desired_caps['testobject_device'] = os.getenv('TESTOBJECT_DEVICE')
        if os.getenv('APPIUM_VERSION'):
            desired_caps['testobject_appium_version'] = os.getenv('APPIUM_VERSION')
        if os.getenv('PLATFORM_VERSION'):
            desired_caps['platformVersion'] = os.getenv('PLATFORM_VERSION')
        if os.getenv('DEVICE_NAME'):
            desired_caps['deviceName'] = os.getenv('DEVICE_NAME')
        if os.getenv('TESTOBJECT_SESSION_CREATION_RETRY'):
            desired_caps['TESTOBJECT_SESSION_CREATION_RETRY'] = os.getenv('TESTOBJECT_SESSION_CREATION_RETRY')
        if os.getenv('TESTOBJECT_SESSION_CREATION_TIMEOUT'):
            desired_caps['TESTOBJECT_SESSION_CREATION_TIMEOUT'] = os.getenv('TESTOBJECT_SESSION_CREATION_TIMEOUT')

        testobject_endpoint = os.getenv('APPIUM_URL', 'http://appium.testobject.com/api/appium/wd/hub')
        self.driver = webdriver.Remote(testobject_endpoint, desired_caps)


    def test_open_testobject_website(self):
        self.driver.get("https://google.com/")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


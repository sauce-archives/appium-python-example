import unittest
import os
from appium import webdriver

class TestClass(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['testobject_api_key'] = os.environ['TESTOBJECT_API_KEY']
        desired_caps['testobject_device'] = os.environ['TESTOBJECT_DEVICE_ID']
        desired_caps['testobject_appium_version'] = os.getenv('APPIUM_VERSION', '1.6.4')
        testobject_endpoint = os.getenv('APPIUM_ENDPOINT', 'http://appium.testobject.com/api/appium/wd/hub')
        self.driver = webdriver.Remote(testobject_endpoint, desired_caps)


    def test_open_testobject_website(self):
        self.driver.get("https://testobject.com/")
        if not "TestObject" in self.driver.title:
            raise Exception("Unable to load TestObject")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


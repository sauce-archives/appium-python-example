import unittest
from appium import webdriver

class TestClass(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['testobject_api_key'] = 'Your TestObject API key here'
        desired_caps['testobject_device'] = 'LG_Nexus_4_E960_real'
        desired_caps['testobject_appium_version'] = '1.5.2-patched-chromedriver'
        testobject_endpoint = 'http://appium.testobject.com:80/api/appium/wd/hub'
        self.driver = webdriver.Remote(testobject_endpoint, desired_caps)


    def test_open_testobject_website(self):
        self.driver.get("https://testobject.com/")
        if not "TestObject" in self.driver.title:
            raise Exception("Unable to load TestObject")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


import unittest
from selenium import webdriver

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/CODE/JAVA/SeleniumDrivers/chromedriver/v.2.42/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_user_login(self):
        driver = self.driver
        driver.get("https://gmail.com")
        login_field = driver.find_element_by_xpath("//input[@id = 'identifierId']")
        login_field.send_keys("ulsdet")
        next_login_button = driver.find_element_by_xpath("//div[@id = 'identifierNext']")
        next_login_button.click()
        pass_field = driver.find_element_by_xpath("//input[@name = 'password']")
        pass_field.send_keys("ljrth%8102")
        next_pass_button = driver.find_element_by_xpath("//div[@id = 'passwordNext']")
        next_pass_button.click()
        title = driver.title()
        self.assertEqual(title, "Входящие")

    def tear_down(self):
        self.driver.quit()





if __name__ == "__main__":
    unittest.main()
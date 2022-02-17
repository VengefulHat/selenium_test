import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('https://google.com')

        driver.find_element_by_id("L2AGLb").click()
        self.assertIn("Google", driver.title)
        assert "Google" in driver.title
        elem = driver.find_element_by_name('q')
        elem.clear()
        elem.send_keys("python")
        elem.send_keys(Keys.RETURN)
        assert "Not results found" not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

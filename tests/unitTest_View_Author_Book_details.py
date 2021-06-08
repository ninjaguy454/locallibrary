# Unit test file to determine if the user can navigate to an author's page
# and when they reach the author's page, if they can navigate to the book
# details page for the first book they published.


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "testuser"
        pwd = "test123"
        driver = self.driver
        driver.maximize_window()

        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.ENTER)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        # assert "Logged in"
        # find 'All authors' and click it
        elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/ul/li[3]/a").click()

        time.sleep(3)
        # find first author and click their name.
        elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/ul/li[1]/a").click()

        time.sleep(3)
        # find first book under author's page and click it.
        elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/ul/h8/a").click()

        time.sleep(5)
        try:
            # verify Book details are correctly loaded by searching for
            # the copies of the book available
            elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/h4")

            assert True

        except NoSuchElementException:
            self.fail("Book statuses do not appear when author's first book is clicked")
            assert False

    time.sleep(2)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
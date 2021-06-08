# Unit test file to determine if the user can view book details
# when they click the 'All books' button in the navigation pane of the local library
# then clicks on the first books button in the Book list page

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
        # find 'All books' and click it – note this is all one Python statement
        elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/ul/li[2]/a").click()
        time.sleep(3)
        # find first book and click it.
        elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/ul/li[1]/a[1]").click()

        time.sleep(5)
        try:
            # verify Book List exists on new screen after clicking "All books" button
            # attempt to find the 'Logout' button - if found, logged in
            elem = driver.find_element_by_xpath("/html/body/ul/li[3]/a")

            assert True

        except NoSuchElementException:
            self.fail("Book Details does not appear when first title clicked")
            assert False

    time.sleep(2)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()


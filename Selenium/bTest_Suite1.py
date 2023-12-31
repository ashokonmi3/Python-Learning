import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.google.com/")
        print("hello")
        # driver.title
    def test_search_by_text(self):
        driver=self.driver()
        # get the search textboxs

        search_field = self.driver.find_element_by_name("q")
        # enter search keyword and submit
        search_field.send_keys("Python class")
        search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        list_new = self.driver.find_elements_by_class_name("r")
        assertEqual(11, len(list_new))


    def tear_Down(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
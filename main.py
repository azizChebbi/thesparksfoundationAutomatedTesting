import unittest
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# --------- THE SPARKS FOUNDATION --------------
class TheSparksFoundation(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, executable_path="/usr/lib/chromium-browser/chromedriver")

    def test(self):
        driver = self.driver
        # ------------------- LANDING PAGE ---------------
        driver.get("https://www.thesparksfoundationsingapore.org/")
        # ---------- CHECK THE NAME --------------
        brand = driver.find_element(By.CSS_SELECTOR,'a.navbar-brand')
        assert 'The Sparks Foundation' in brand.text
        # ---------- CHECK LOGO --------------
        # it will select the first element found by tag name 'img' => which is the desired one
        try:
            img = driver.find_element(By.TAG_NAME,'img')
            self.assertTrue(img.is_displayed(),True)
        except NoSuchElementException as e:
            print(e)

        # ----------- CHECK THE NAVBAR APPEARANCE -----------------
        navbar = driver.find_element(By.ID,'bs-example-navbar-collapse-1')
        navbarHeight = navbar.value_of_css_property('height')
        self.assertNotEqual(navbarHeight,0,"Navbar is hidden")

        # ----------- JOIN US PAGE --------------
        join = driver.find_element(By.LINK_TEXT,'Join Us')
        join.click()
        whyJoinUs = driver.find_element(By.LINK_TEXT,'Why Join Us')
        whyJoinUs.click()
        # ------------ CHECK THE JOIN US FORM --------------
        fullName = driver.find_element(By.NAME,'Name')
        email = driver.find_element(By.NAME, 'Email')
        sel = Select(driver.find_element(By.TAG_NAME,'select'))
        submit = driver.find_element(By.CLASS_NAME,'button-w3layouts')
        # typing in the form data
        fullName.send_keys('Jhon doe')
        email.send_keys('example@gmail.com')
        time.sleep(1)
        sel.select_by_visible_text("Student")
        time.sleep(1)
        # submit the form
        time.sleep(1)
        submit.click()

        # ------------ WORKSHOPS PAGE ---------
        programs = driver.find_element(By.LINK_TEXT, 'Programs')
        programs.click()
        workshops = driver.find_element(By.LINK_TEXT, 'Workshops')
        workshops.click()
        try:
            driver.find_element(By.CLASS_NAME, 'blog-grids-w3-agile')
        except NoSuchElementException as e:
            print('no worshops for the upcoming days')

        # ------------ Global Education Choices Workshop PAGE -------------
        driver.get('https://www.thesparksfoundationsingapore.org/programs/workshops/resume-writing-workshop/')
        # ---------- check in the Resume -------------
        try:
            img = driver.find_element(By.XPATH,"//img[@src='/images/resume-writing-poster.png']")
            self.assertTrue(img.is_displayed(),True)
        except NoSuchElementException as e:
            print("The resume does not exist")
        # ------------ CONTACT US PAGE -------------
        driver.get('https://www.thesparksfoundationsingapore.org/contact-us/')
        contacts = driver.find_element(By.XPATH, "//body/div[2]/div/div/div[3]/div[2]/p[2]")
        contacts = contacts.text.split(", ")
        print('contacts: ',contacts)

if __name__ == "__main__":
    unittest.main()

import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import configparser

class test():

    def __init__(selt):
        global driver
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.implicitly_wait(20)

    def broken_link(self):
        driver.get("https://www.qsstechnosoft.com/")
        print(driver.title)
        driver.maximize_window()
        size = driver.find_elements(By.XPATH, "//a")
        type(False)
        for i in size:
            if i.get_attribute('href') != "#" and i.get_attribute('href') != 0:
                print("Get Attribute")
            type(True)
            print(i.get_attribute('href'))
            assert type != False
            self.assertEqual(type, True, "pass")

        driver.close()

    def hover_functinality(self):
        driver.get("https://www.qsstechnosoft.com/")
        driver.maximize_window()
        action = ActionChains(driver)
        elementSize = driver.find_elements(By.XPATH, "//ul[@id='nav']/li")
        for i in elementSize:
            action.move_to_element(i).perform()
            time.sleep(2)
        driver.close()

    def window_handle(self):
        driver.get("https://www.qsstechnosoft.com/")
        driver.maximize_window()
        try:
           driver.find_element(By.XPATH, "//*[@alt='QSS Technosoft Inc.']/following::img").click()
        except Exception as e:
           print(e)
        finally:
           driver.find_element(By.XPATH, "//*[@alt='QSS Technosoft Inc.']/following::img").click()
        handles = driver.window_handles
        size = len(handles)
        parent_handle = driver.current_window_handle
        for x in range(size):
            if handles[x] != parent_handle:
                driver.switch_to.window(handles[x])
                driver.find_element(By.XPATH, "//input[@name='email']").send_keys("dummy@gmail.com")
                driver.find_element(By.XPATH, "//input[@name='pass']").send_keys("password")
                driver.quit()
                break


    def contact_Form(self):
      driver.get("https://www.qsstechnosoft.com/")
      driver.maximize_window()
      assert driver.title == "Top Web and Mobile App Development Company | QSS Technosoft"
      driver.find_element(By.XPATH, "//a[text()='Contact']").click()
      driver.find_element(By.XPATH, "//input[@id='fName']").send_keys("Pradeep Tiwari")
      driver.find_element(By.XPATH, "//input[@name='emailAdd']").send_keys("pradeep@gmail.com")
      driver.find_element(By.XPATH, "//input[@id='pNumber']").send_keys("7021485463")
      try:
        driver.find_element(By.XPATH, "//*[@id='myInput']/following::span[@id]").click()
      except Exception as e:
        print(e)
      for i in range(10):
        driver.find_element(By.XPATH, "//textarea[@name='msg']").send_keys(Keys.CONTROL, 'v')

        driver.find_element(By.XPATH, "//*[@class='logo']").click()
      ## Validation of home page ###
      assert driver.title == "Top Web and Mobile App Development Company | QSS Technosoft"
      driver.close()

    def screenShot(self):
        driver.get("https://www.qsstechnosoft.com/")
        driver.maximize_window()
        driver.save_screenshot("image.png")
        image = Image.open("image.png")
        image.show()
        driver.close()





obj = test()
obj.screenShot()
#obj.hover_functinality()

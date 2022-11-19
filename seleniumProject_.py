from selenium import webdriver
import time

class Automation():
    def auto_Mate(self):
        driver=webdriver.Chrome("C:\\Users\\manik\\OneDrive\\Documents\\chromedriver.exe")
        driver.maximize_window()

        driver.get("https://www.nopcommerce.com/en")

        marktpl=driver.find_element_by_xpath("/html/body/div[7]/header/nav/div[3]/div/ul[1]/li[2]/span")
        marktpl.click()


        marktpl_1=driver.find_element_by_xpath("/html/body/div[7]/header/nav/div[3]/div/ul[1]/li[2]/ul/li[2]/a/span")
        marktpl_1.click()


        time.sleep(3)

        #PRODUCT TO BE ADDED
        prdtToAdd="https://www.nopcommerce.com/en/course-levels?featured=true"
        driver.get(prdtToAdd)

        #ADD TO CART
        addToCart=driver.find_element_by_xpath("/html/body/section/div[2]/div/form[1]/div/div[2]/a")
        addToCart.click()

        #Entering the User Name
        userName=driver.find_element_by_xpath("/html/body/section/div[2]/div/form[1]/div/div[3]/div/div/main/div/div[1]/div[2]/input")
        userName.send_keys("RohanKNA")

        #Entering the E-mail ID

        mailID=driver.find_element_by_xpath("/html/body/section/div[2]/div/form[1]/div/div[3]/div/div/main/div/div[2]/div[2]/input")
        mailID.send_keys("rexiw38565@pamaweb.com")


        #ADDING THE PRODUCT TO CARD & OPENING THE CART TO VERIFY
        addButton=driver.find_element_by_xpath("/html/body/section/div[2]/div/form[1]/div/div[3]/div/div/footer/div[2]/button")
        addButton.click()


obj_1=Automation()
obj_1.auto_Mate()
        









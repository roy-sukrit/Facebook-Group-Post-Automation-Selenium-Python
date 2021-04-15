from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import json
import os

LOGIN_URL = 'https://www.facebook.com/login.php'
GROUP_URL='https://www.facebook.com/groups/'
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
         
driver = webdriver.Chrome('./chromedriver.exe', options=options)



class FacebookBot():
    def __init__(self,data,text):  
        self.email= data['Email Address']
        self.password= data['Password']
        self.postdata=data['Page Names']
        self.textContents=text 
        self.fb_posting = ["/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]",
                           "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div",
                           "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div"]
         
        
          
        # Text posting content variable
        # Will be set via text_posting_content_load function
        driver.get(LOGIN_URL)
        time.sleep(2) # Wait for some time to load

#^Login part 
 
    def login(self):    
        email_element = driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input
        password_element = driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too
        login_button = driver.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click
        time.sleep(2) # Wait for 2 seconds for the page to show up

#^Object part
    
    def page_posting(self):
        pages=self.postdata


        for p in pages:
            driver.get(GROUP_URL+p)            
            time.sleep(5)
            driver.find_element_by_xpath(self.fb_posting[0]).click() 
            time.sleep(2)      

            driver.find_element_by_xpath(self.fb_posting[1]).send_keys(Keys.ENTER, self.textContents) 
            time.sleep(2)      
       
            driver.find_element_by_xpath(self.fb_posting[2]).click() 
            time.sleep(5)      
                                               

    
def src_bot():
    f = open('./fb_credentials.json','r')
    t= open ('./PostingContents.txt','r')
    data=json.loads(f.read())
    text= t.read()
    bot=FacebookBot(data,text)
    bot.login()
    bot.page_posting()


src_bot()    
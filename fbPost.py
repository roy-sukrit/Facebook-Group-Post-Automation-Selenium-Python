from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import json
import os


LOGIN_URL = 'https://www.facebook.com/login.php'
GROUP_URL='https://www.facebook.com/groups/'

options = webdriver.ChromeOptions()
#&disable push notifications
options.add_argument("--disable-notifications")

#&disale usb device error
options.add_experimental_option('excludeSwitches', ['enable-logging'])

         
driver = webdriver.Chrome('./chromedriver.exe', options=options)



class FacebookBot():
    def __init__(self,data,text,groups):  
        self.email= data['Email Address']
        self.password= data['Password']
        self.textContents = text
        self.groupdata=groups      
        self.fb_posting = ["//div[@class='m9osqain a5q79mjw jm1wdb64 k4urcfbm']",
                           "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div",
                           "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div",]
       

#^Group ids
    def ids(self):
       id = self.groupdata
       split_links = id.split(',')
       global group
       group=[]
       for p in split_links:
           group.append(p.replace('https://www.facebook.com/groups/','').replace("\n",'').split('/')[0])


#^Login part 
 
    def login(self):    
        print("Process Initiating")
        
        driver.get(LOGIN_URL)
        time.sleep(2) # Wait for some time to load
        email_element = driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give email as i/p
        password_element = driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as i/p
        login_button = driver.find_element_by_id('loginbutton')
        login_button.click() # Login click
        time.sleep(2) # Wait for 2 seconds for the page to show up

#^Posting part
    
    def page_posting(self):
        try: 
            i=0

            
            for p in group:
                
                driver.get(GROUP_URL+p)            
                time.sleep(5)
                driver.find_element_by_xpath(self.fb_posting[0]).click() 
                time.sleep(2)      

                driver.find_element_by_xpath(self.fb_posting[1]).send_keys(Keys.ENTER, self.textContents) 
                time.sleep(2)      
        
                driver.find_element_by_xpath(self.fb_posting[2]).click()
                i+=1
                
                print("posts completed",i)
                time.sleep(2)  
                

        except Exception as e:

            print("Error is: \n ",e)
            driver.close()            
                                               

    
def src_bot():
    f = open('./credentials.json','r')
    t= open ('./PostingContents.txt','r')
    g = open('./group_links.txt','r')
    groups = g.read()
    data=json.loads(f.read())
    text= t.read()
    #Init the object
    bot=FacebookBot(data,text,groups)
    bot.ids()
    bot.login()
    bot.page_posting()    
    driver.close()
    print("Task Completed Successfully!")


src_bot()    
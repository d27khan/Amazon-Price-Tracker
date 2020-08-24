import time
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

URL='Your Amazon URl here'
#   **Leave this function**
def userAgent():
  driver = webdriver.Chrome()

  driver.get('http://www.google.com')

  search = driver.find_element_by_name('q')
  search.send_keys("My user agent")
  search.send_keys(Keys.RETURN)

  soup = BeautifulSoup(page.content, 'html.parser')
  global useragent
  useragent = soup.find(id = "uyUSCd").get_text()

  time.sleep(7)
  driver.quit()

# ** leave these 2 lines alone aswell
userAgent()
headers = {"User-Agent": '%s',%useragent}

def checkPrice():
    page = requests.get(URL,headers= headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    global title
    global floatprice
    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    floatprice = float(price[5:10]) # used for comparing the current 
                                    #price to a potentially lower price

    if(floatprice<'your price here'):
        send_sms()

    print(floatprice)
    print(title.strip())

def send_sms():

  email = "Your email here"
  pas= "Your Password here"

  sms_gateway = 'enter your phone providers sms gateway here'
    ## leave all of this 
  smtp = "smtp.gmail.com"
  port = 587 #gmail port
  server = smtplib.SMTP(smtp,port)
  server.starttls()
  server.login(email,pas)
  msg = MIMEMultipart()
  msg['From'] = email
  msg['To'] = sms_gateway
  msg['Subject'] = "The price has changed!\n"
  body = ("%s Is now $%d" %(title,floatprice))
  msg.attach(MIMEText(body, 'plain'))
  sms = msg.as_string()
  server.sendmail(email,sms_gateway,sms)
  server.quit()

checkPrice()

## use cron to schedule this script
## updates are on the way to make this more effiecient!

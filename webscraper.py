import requests #allows access to a URL and pulls out data from the site
from bs4 import BeautifulSoup #parses data  
import smtplib 
import time

#replace URL with the one you want
URL = 'https://www.amazon.ca/dp/B07YSYK6F5/ref=dp_cerb_2'

headers = { #information about the browser being used
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

def price_checker(): #this function checks the price of item
    page = requests.get(URL, headers = headers) #returns data from URL

    bsoup = BeautifulSoup(page.content, 'html.parser') #allows us to pull individual parsed data

    product_title = bsoup.find(id = "productTitle").get_text() #searches site for title of amazon product
    product_price = bsoup.find(id = "priceblock_ourprice").get_text()
    converter = float(product_price[0:5]) #extracts first 5 digits of price

    if converter < 1.700:
        send_mail()
    
    print(convertere)
    print(product_title.strip())

    if (converter , 1.700):
        email()



def email(): #this  function sends email to recipient about price drop
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('', '') #fill out your gmail in the first blank and password in the second blank

    subject = "Price has dropped!"
    body = "check the link below! \n https://www.amazon.ca/dp/B07YSYK6F5/ref=dp_cerb_2"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        '', #re-enter your email in the blank
        msg
    )

    print ("Email has been sent successfully")
    server.quit()

while(True):
    price_checker()
    time.sleep(86400)

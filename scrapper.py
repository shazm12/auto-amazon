import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Add the product's URL

URL='https://www.amazon.in/gp/product/B07DJ8K2KT/ref=s9_acss_bw_cg_CPACS_2b1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-9&pf_rd_r=0Y1EET92W5GKA7MDCJPF&pf_rd_t=101&pf_rd_p=30e50afb-c1d7-42e3-beb0-41f846ac85c2&pf_rd_i=1389401031'

headers = {
    "User-Agent":<Your browser user agent>} #Get your browser user-agent by simply seraching for it in your browser's search engine

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_saleprice").get_text()

    converted_price= int(price[2:4]+price[5:8])


    print(title.strip())
    print(converted_price)
    user_price = int(input('Please enter the price range for the selected product you wanna buy: '))

    if(converted_price > user_price):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(<Email Address>,<Auth key>) #Get the auth key for your email address that you will use to send mails by doing the Google's 2-step verification and then create a app for gmail 
    
    #Change the subject and body according to your need
    
    subject= 'Price fell Down for OnePlus 7T Pro!!!'
    body= 'Check the Amazon Link - https://www.amazon.in/gp/product/B07DJ8K2KT/ref=s9_acss_bw_cg_CPACS_2b1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-9&pf_rd_r=0Y1EET92W5GKA7MDCJPF&pf_rd_t=101&pf_rd_p=30e50afb-c1d7-42e3-beb0-41f846ac85c2&pf_rd_i=1389401031'

    msg= "Subject : {}\n\n{}".format(subject,body)
    server.sendmail(
        <Enter the email address from which you want to send>,
        <Enter the email addresss of whom you want to send this mail>,
        msg
    )
    print('Hey the mail has been sent')
    server.quit()


while(True):
    check_price()
    time.sleep(60*60)





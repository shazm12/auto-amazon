import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.amazon.in/gp/product/B07DJ8K2KT/ref=s9_acss_bw_cg_CPACS_2b1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-9&pf_rd_r=0Y1EET92W5GKA7MDCJPF&pf_rd_t=101&pf_rd_p=30e50afb-c1d7-42e3-beb0-41f846ac85c2&pf_rd_i=1389401031'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_saleprice").get_text()

    converted_price= int(price[2:4]+price[5:8])


    print(title.strip())
    print(converted_price)

    if(converted_price > 40000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('berashamik115@gmail.com','yoldumxmlfjwskwe')

    subject= 'Price fell Down for OnePlus 7T Pro!!!'
    body= 'Check the Amazon Link - https://www.amazon.in/gp/product/B07DJ8K2KT/ref=s9_acss_bw_cg_CPACS_2b1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-9&pf_rd_r=0Y1EET92W5GKA7MDCJPF&pf_rd_t=101&pf_rd_p=30e50afb-c1d7-42e3-beb0-41f846ac85c2&pf_rd_i=1389401031'

    msg= "Subject : {}\n\n{}".format(subject,body)
    server.sendmail(
        'berashamik115@gmail.com',
        'berashamik115@gmail.com',
        msg
    )
    print('Hey the mail has been sent')
    server.quit()


while(True):
    check_price()
    time.sleep(60*60)






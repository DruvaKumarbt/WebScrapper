import requests
from bs4 import BeautifulSoup
import smtplib


URL= 'https://www.amazon.in/Test-Exclusive-609/dp/B07HGJFVL2/ref=sr_1_3?keywords=oneplus+7&qid=1564590813&s=electronics&smid=A23AODI1X2CEAE&sr=1-3'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

def check_price:
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser') 
    title = soup.find(id="productTitle").get_text()
    print(title.strip())
    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price = price[2:8]
    if(converted_price <'33,000'):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('druvakumar.bt@gmail.com','knybxymjaamecllg')
    subject = 'Price fell down!!!!'
    body = 'Check the amazon link https://www.amazon.in/Test-Exclusive-609/dp/B07HGJFVL2/ref=sr_1_3?keywords=oneplus+7&qid=1564590813&s=electronics&smid=A23AODI1X2CEAE&sr=1-3'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'druvakumar.bt@gmail.com',
        'nidhimudugal59@gmail.com',
        msg
    )
    print('Email has been sent')
    server.quit()
    
check_price()










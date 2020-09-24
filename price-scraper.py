import requests
from bs4 import BeautifulSoup
import os
import smtplib
import time

email = os.environ.get('MY_EMAIL')
password = os.environ.get('MY_EMAIL_PASS')
url = 'https://www.ebay.com/itm/Nintendo-Switch-32GB-Console-Neon-Red-Blue-Joy-con-Newest-Version-NEW/133461951424?_trkparms=ispr%3D1&hash=item1f12f3c3c0:g:y3UAAOSwRute70du&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkBUIiHwYv5YgVss0WaiENz3eUn0TxYQsTWOMfb2D%252BVSowIheGjpJuvcbn6l08NQ0xr41RXse5wO%252B7zDpDx9OaX9CYhD5qdJg9kGaZ22lUEyj2gYoItQ2S5BmgKOarg%252B9mi9QW93%252BgO%252B5IK55T4amfqNTUwa3cuSzlA94yqvwYw%252FatELtBsw26uyxo%252BaI4eaLwBuIgIz%252BITFcui2glFuFuQsSgOVl7%252FLHtntUh%252BDMg%252Bkv7xE4fZkO4nDTJk9m9xqXepbpPuC2v%252B9Uv87mK4%252F0qB4OCFbIXC6paOh1tyWPpCGZXpg2w0pC3mQp6cDCOU%252BDIoTeHevwzKSgTX4%252FAU4VLZJ1WqWvGrWnpz3l0fSyJ5zn22V%252BfD%252BgYgy%252FU5%252BsuI7cKOSD47CrEsRfSFidSyzH0gv3WqxHHC4iFA0kkj45EHpDWidAkKOFBGhJjv1zzE2QbzAfF50vebedXD1Jdpda1dTHojv6kkciFkjDup%252FN7POK1Gzif9kR0jTX9nqEg%252BJoGsDohXRbLeG6eNh%252FqOKa5wdt%252BArddAR2MF1sUiz857PaiEGnwJ7usjDQ9s1CiXZtZEdaG7Pi6z0iIiFD3TxFRoSmwooORcZhWfEdYVrgV%252FEDXqMZlxZodE7QI8ZAAIGglbMxJbvDx6Y0gOaRDpHDhYKFHZp0qJ0n%252BG%252FazdktczTxpM9yDSF%252BbWqIu6x7CRjwS3lbA4kTbesdLhvL%252Ben%252F%252FUHMDjtAlLyBEtkCBeZv0Wqua27dLeh5WKufno768JZnFnJniaavK1mO4Z9tjRoDhaw%253D%253D%7Ccksum%3A1334619514241fa608b2cab14ed2a14902897adfa8c1%7Campid%3APL_CLK%7Cclp%3A2334524'

# A function that is used to check if the price has changed
def check_price():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    price =soup.find(class_='notranslate').get_text()
    convertedPrice = float(price[4:10])
    
    if convertedPrice <= 300: # if price goes below 300 and email is sent to the user
        send_mail()


def send_mail():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, password)

        subject = 'Nintendo Switch Price Drop!!'
        body = 'check Ebay Link' + url

        msg = f'Subject: {subject} \n\n {body}'
        smtp.sendmail(email, email, msg)
        print('Email Sent')

count = 0

# A while loop is used to check the price ever hour for 24 hours
while(count != 24):
    check_price()
    time.sleep(60 * 60) # checks the price every hour
    count+= 1
    print(count)

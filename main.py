import requests
from bs4 import BeautifulSoup
import smtplib
import time


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # use your email password by enabling access to less secure apps or set up
    # two step verification and then create a app pasword and use that instead

    server.login("sender@gmail.com", "sender_email_password")

    mail_subject = "Price drop alert"
    mail_body = "Link to the product : https://www.amazon.in/HiFiMAN-HE400SE-Wired-Headphone-Silver/dp/B08Z2SK5C4"

    # follow this syntax to send mail Subject: mail subject and then two new lines and then mail body

    message = f"Subject: {mail_subject}\n\n{mail_body}"

    server.sendmail(
        "sender@gmail.com",
        "reciever@gmail.com",
        message
    )

    print("Mail sent")
    server.quit()


def current_cost():

    # link to the product which you want to track
    URL = "https://www.amazon.in/HiFiMAN-HE400SE-Wired-Headphone-Silver/dp/B08Z2SK5C4"

    # to get the user agent search user agent on chrome
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

    page = requests.get(URL, headers=header)

    soup = BeautifulSoup( page.content, "html.parser")

    price = soup.find(id="priceblock_dealprice").get_text()

    new_price = ""
    for p in price[1:]:
        if p != ',':
            new_price += p

    cost = int(float(new_price))
    if cost < 12000:
        send_mail()


while 1:
    current_cost()

    # sleep time to avoid spamming
    time.sleep(60*60*3)
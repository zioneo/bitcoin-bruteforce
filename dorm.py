    
import bitcoin, base58, ecdsa, requests, smtplib, multiprocessing, blockchain
from bitcoin import *

while True:

    private_key = random_key()
    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)

    with open("YOUR-BTC-DATA.txt", "r") as m:
        add = m.read().split()
        for ad in add:
                continue
        if address in add:
            print("Found"+ " " +address+ ' ' +private_key)
            data = open("data.txt","a")
            data.write(print(address+ ' ' +private_key+ ' ' +"\n")) 
            data.close()

            #send address and private key via email 

            msg = "Found"+ " " +address+ ' ' +private_key
            text = msg
            server =smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login("your@gmail.com", "your-gmail-password")
            fromaddr = "your@gmail.com"
            toaddr = "anybody@gmail.com"
            server.sendmail(fromaddr, toaddr, text)
        else:
            print(address+ ' ' +private_key)



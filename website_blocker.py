#/etc/hosts
import time
from datetime import datetime as dt
host_temp="hosts"
host_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com" , "facebook.com" ,"www.instagram.com"]

year = dt.now().year
month= dt.now().month
day = dt.now().day



while True:
    if dt(year , month , day , 20) < dt.now() < dt(year , month , day , 5):
        print ("No distractions ")
        with open(host_temp , 'r+' ) as file:
            content = file.read()
            print (content)
            for website in website_list:
                if website in content:
                    continue
                else:
                    file.write(redirect + "  " + website + "\n")
    else:
        with open(host_temp , 'r+' ) as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print ("fun hours ")

    time.sleep(5)

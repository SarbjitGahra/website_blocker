#/etc/hosts
import time
from datetime import datetime as dt
host_path="/etc/hosts"
redirect="127.0.0.1"
wesite_list=["www.facebook.com" , "facebook.com" ,"www.instagram.com"]

year = dt.now().year
month= dt.now().month
day = dt.now().day



while True:
    if dt(year , month , day , 1) < dt.now() < dt(year , month , day , 9):
        print ("No distractions ")
    else:
        print ("fun hours ")
    time.sleep(5)

import os
import requests
from bs4 import  BeautifulSoup
import csv
#import pandas as pd
import datetime
import time

def main():
    print(__name__)
    r = requests.get("http://www.devtal.de/blog/index.php")
    print(r)
    fname = 'spacestatus_log.csv'
    bs = BeautifulSoup(r.content)
    if(bs.find_all("img", {"alt":"offen"})):
       o = True
       print("Es ist offen")
    else:
       o = False
       print("Es ist zu")

if __name__== '__main__':
    if main():
       with open('spacestatus.csv', 'w', newline='') as csvfile:
           cwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           cwriter.writerow((datetime.datetime.now(), "open"))
    else:
       with open('spacestatus.csv', 'w', newline='') as csvfile:
           cwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           cwriter.writerow((datetime.datetime.now(), "closed"))
    time.sleep(6000)



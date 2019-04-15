import os
import requests
from bs4 import  BeautifulSoup
import csv
#import pandas as pd
import datetime

def main():
    print(__name__)
    r = requests.get("http://www.devtal.de/blog/index.php")
    print(r)
    fname = 'spacestatus_log.csv'
    bs = BeautifulSoup(r.content)
    if(bs.find_all("img", {"alt":"offen"})):
       o = True
    else:
       o = False

if __name__== '__main__':
    if main():
       with open('spacestatus.csv', 'w', newline='') as csvfile:
           cwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           cwriter.writerow(datetime.datetime(), "open")
    else:
       with open('spacestatus.csv', 'w', newline='') as csvfile:
           cwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           cwriter.writerow(datetime.datetime(), "closed")
    sleep(1000)



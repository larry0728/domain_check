import requests
import pandas as pd
import random
import pygsheets
import datetime
from datetime import date
import json
from bs4 import BeautifulSoup
from config import twdomain,vndomain,phdomain,inddomain
import logging
from time import sleep
#台灣取得到期日
mydomain = []
list_domain = []
day1=str(datetime.date.today()).replace("-",",")

#log紀錄設定
FORMAT ='%(asctime)s %(levelname)s: %(message)s'
DATE_FORMAT ='%Y%m%d %H:%M:%S'
#顯示預設為INFO
logging.basicConfig(level=logging.INFO, format=FORMAT,datefmt=DATE_FORMAT,filename="domaincheck.log",filemode="w")



myExpiry_time = []


def days(str1,str2):
    date1=datetime.datetime.strptime(str1[0:12],"%Y,%m,%d")
    date2=datetime.datetime.strptime(str2[0:12],"%Y,%m,%d")
    num=(date2-date1).days
    return num

#https://lookup.icann.org/en/lookup
for tw in twdomain:
    try:
        twdoamin_dict = {}

        headers = {
            #
            'referer': 'http://www.asqql.com/',
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
            # 使用者代理
            #
        }

        myrequests = "https://rdap.godaddy.com/v1/domain/" + tw

        myget = requests.get(myrequests,headers=headers)

        if myget.status_code == 404 :
            headers = {
                'referer': 'https://lookup.icann.org/',
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
            }

            myrequests2 = "https://rdap.verisign.com/net/v1/domain/" + tw

            myget2 = requests.get(myrequests2, headers=headers)

            if myget2.status_code == 404:
                headers = {
                    'referer': 'https://lookup.icann.org/',
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
                }
                myrequests3 = "https://rdap.verisign.com/com/v1/domain/" + tw

                myget3 = requests.get(myrequests3, headers=headers)

                soup3 = BeautifulSoup(myget3.text, "html.parser")

                data = json.loads(str(soup3))

                needspilt = data['events'][1]['eventDate']

                needreplace = needspilt.split("T")[0]

                Expiry_time = needreplace.replace("-", ",").strip()

                twdoamin_dict['domain_name'] = tw

                twdoamin_dict['Expiry_day'] = Expiry_time

                twdoamin_dict["離到期還有(天)"] = days(day1, Expiry_time)

                list_domain.append(twdoamin_dict)

                delay = random.randint(20, 40)

                sleep(delay)
                continue

            soup2 = BeautifulSoup(myget2.text, "html.parser")

            data = json.loads(str(soup2))

            needspilt = data['events'][1]['eventDate']

            needreplace = needspilt.split("T")[0]

            Expiry_time = needreplace.replace("-", ",").strip()

            twdoamin_dict['domain_name'] = tw

            twdoamin_dict['Expiry_day'] = Expiry_time

            twdoamin_dict["離到期還有(天)"] = days(day1, Expiry_time)

            list_domain.append(twdoamin_dict)

            delay = random.randint(20,40)

            sleep(delay)
            continue

        soup = BeautifulSoup(myget.text,"html.parser")

        data = json.loads(str(soup))

        needspilt = data['events'][1]['eventDate']

        needreplace = needspilt.split("T")[0]

        Expiry_time=needreplace.replace("-",",").strip()

        twdoamin_dict['domain_name'] = tw

        twdoamin_dict['Expiry_day'] = Expiry_time

        twdoamin_dict["離到期還有(天)"]= days(day1,Expiry_time)

        list_domain.append(twdoamin_dict)

        delay = random.randint(20, 40)

        sleep(delay)
    except:
        logging.error("tw doamin crawler failure.")
#
#
#
#
# #菲律賓取得到期日
for phd in phdomain:
    try:


        phdomain_dict = {}


        headers = {

            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",

        }
        phrequests = "https://whois.dot.ph/whois?search=" + phd
        phget = requests.get(phrequests, headers=headers)
        soup = BeautifulSoup(phget.text, "html.parser")
        needsplit = soup.find_all('script')[1].text
        needreplace = needsplit.split("expiryDate")[1].split('moment')[1].split(".format")[0].split('T')[0].replace("(\'", "")
        Expiry_time = needreplace.replace("-", ",").strip()

        phdomain_dict['domain_name'] = phd

        phdomain_dict['Expiry_day'] = Expiry_time

        phdomain_dict["離到期還有(天)"] = days(day1, Expiry_time)

        list_domain.append(phdomain_dict)

        delay = random.randint(1, 7)

        sleep(delay)
    except:
        logging.error("phd doamin crawler failure.")

#越南 取得到期日
for vn in vndomain:
    try:
        vndomain_dict = {}

        headers = {
            #     "Cookie": "w365_lang=tw; _ga=GA1.2.686058391.1660805877; __gads=ID=1b9119966c6cd591-2206a4daaad50084:T=1660805877:RT=1660805877:S=ALNI_MbbZ6_aWuQYE6uCc8VUyDSS14PmfQ; _gid=GA1.2.1867532187.1661163990; __gpi=UID=000008b8513cf644:T=1660805877:RT=1661241732:S=ALNI_MY43Xe3Ym_pTo7Vevh9_aKFOGy3rg; _gali=searchform; w365id=qposlbkjmthupk31tsl6nhk4i5",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
            # 使用者代理
            #
        }

        myrequests = "https://whois.gandi.net/zh-hant/results?search=" + vn

        myget = requests.get(myrequests, headers=headers)

        soup = BeautifulSoup(myget.text, "html.parser")

        needsplit = soup.find("pre", class_="HomeResults-content").find("p", id="L7").text

        needreplace = needsplit.split(':')[1].split("T")[0]

        Expiry_time = needreplace.replace("-", ",").strip()

        vndomain_dict['domain_name'] = vn

        vndomain_dict['Expiry_day'] = Expiry_time

        vndomain_dict["離到期還有(天)"] = days(day1,Expiry_time)
        #陣列相加
        list_domain.append(vndomain_dict)

        delay = random.randint(1, 7)

        sleep(delay)

    except:
        logging.error("vn doamin crawler failure.")

#印度爬取

for ind in inddomain:
    try:
        inddomain_dict = {}
        headers = {
            #     "Cookie": "w365_lang=tw; _ga=GA1.2.686058391.1660805877; __gads=ID=1b9119966c6cd591-2206a4daaad50084:T=1660805877:RT=1660805877:S=ALNI_MbbZ6_aWuQYE6uCc8VUyDSS14PmfQ; _gid=GA1.2.1867532187.1661163990; __gpi=UID=000008b8513cf644:T=1660805877:RT=1661241732:S=ALNI_MY43Xe3Ym_pTo7Vevh9_aKFOGy3rg; _gali=searchform; w365id=qposlbkjmthupk31tsl6nhk4i5",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
            # 使用者代理
            #
        }

        myrequests = "https://whois.gandi.net/zh-hant/results?search=" + ind

        myget = requests.get(myrequests, headers=headers)

        soup = BeautifulSoup(myget.text, "html.parser")

        needsplit = soup.find("pre", class_="HomeResults-content").find("p", id="L7").text

        needreplace = needsplit.split(':')[1].split("T")[0]

        Expiry_time = needreplace.replace("-", ",").strip()

        inddomain_dict['domain_name'] = ind

        inddomain_dict['Expiry_day'] = Expiry_time

        inddomain_dict["離到期還有(天)"] = days(day1,Expiry_time)

        list_domain.append(inddomain_dict)

        delay = random.randint(1, 7)

        sleep(delay)
    except:
        logging.error("ind doamin crawler failure.")


try:
    df = pd.DataFrame(list_domain)

    df = df.sort_values(by="離到期還有(天)")

    print(df)
except:
    logging.error("排序失敗....")



try:
    #client email
    #domain-api@domain-expiration.iam.gserviceaccount.com
    KEY_FILE_LOCATION = 'domain-expiration-93a5abc19a2e.json'
    SHEET_ID = "1oW35oPJJ2sWr9fOFvp7LwK3v2wh4I3ICk6GatL-IYTw"

    gc = pygsheets.authorize(service_file=KEY_FILE_LOCATION)
    sht = gc.open_by_key(SHEET_ID)
    wks = sht.worksheet_by_title('domain')
    wks.clear()
    wks.set_dataframe(df, 'A1',copy_head=True)
    logging.info("send to google sheet successfully....")


except:
    logging.error("send to google sheet failure....")
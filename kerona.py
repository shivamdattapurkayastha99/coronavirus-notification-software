from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title,message):
    notification.notify(title=title,message=message,app_icon=None,timeout=3)
def getdata(url):
    r=requests.get(url)
    return r.text
if __name__ == "__main__":
    # while True:
         notifyme("shivam", "lets stop the spread of the virus together")
         myhtmldata=getdata('https://www.mohfw.gov.in/')
    
         soup = BeautifulSoup(myhtmldata, 'html.parser')
    # print(soup.encode("utf-8"))
         mydata=""
    # print(soup.prettify())
         for tr in soup.find_all('tbody')[0].find_all('tr'):
        
                       mydata+=tr.get_text()
         print(mydata)
    
         itemlist=mydata.split("\n\n")
        #  states=['West Bengal']
         for item in itemlist:
                  datalist=item.split("\n")
         print(datalist)

                #   if datalist[1] in states:
            
                #                ntitle='Cases of COVID'
                #                ntext=f"State:{datalist[1]}\n Active:{datalist[2]}\n Cured:{datalist[3]}\n Deaths:{datalist[4]}\n Total:{datalist[5]}"
                #                notifyme(ntitle,ntext)
                #                time.sleep(2)
        # time.sleep(3600)
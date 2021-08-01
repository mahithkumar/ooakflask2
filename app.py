from keep_alive import keep_alive
import time
from bs4 import BeautifulSoup as bs
import json
import requests
from datetime import datetime

keep_alive()
list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
srpklist=[0, 0, 0, 1, 207, 8, 7, 15, 5, 4, 16, 9, 0, 3, 54, 10, 43, 14, 32, 26]
aapklist=[0, 0, 0, 144, 33, 2, 52, 1, 36, 3, 8, 0, 7, 16, 4, 5, 12, 9, 140, 26]
capklist=[0, 0, 0, 26, 7, 4, 13, 27, 16, 20, 14, 18, 3, 0, 5, 1, 21, 47, 19, 145]
grpklist=[0, 0, 0, 1, 144, 6, 7, 83, 38, 0, 16, 9, 11, 2, 4, 12, 111, 15, 5, 48]
mhpklist=[0, 0, 0, 21, 60, 7, 12, 0, 37, 5, 10, 3, 38, 11, 4, 6, 2, 9, 30, 26]
arpklist=[0, 0, 0, 15, 36, 17, 59, 41, 22, 7, 4, 11, 1, 3, 0, 10, 55, 71, 8, 2]

issue=0
while(1):
    
  srpkdata = requests.get("https://mg-online-01.com/api?packet=User&action=getGameDetail&terminal_id=1&id=25&lang=en")
  soup = bs(srpkdata.content,'html.parser')
  data=soup.text
  data2=json.loads(data) 
  t=data2['data']['current_issue']['remain_time']
  t2=max(t-3,3)

  aapkdata= requests.get("https://mg-online-01.com/api?packet=User&action=getGameDetail&terminal_id=1&id=22&lang=en") 
  soupaapk=bs(aapkdata.content,'html.parser')
  dataaapk=soupaapk.text
  data2aapk=json.loads(dataaapk)

  capkdata= requests.get("https://mg-online-01.com/api?packet=User&action=getGameDetail&terminal_id=1&id=23&lang=en")
  soupcapk=bs(capkdata.content,'html.parser')
  datacapk=soupcapk.text
  data2capk=json.loads(datacapk)

  grpkdata= requests.get("https://mg-online-01.com/api?packet=User&action=getGameDetail&terminal_id=1&id=24&lang=en")
  soupgrpk=bs(grpkdata.content,'html.parser')
  datagrpk=soupgrpk.text
  data2grpk=json.loads(datagrpk)

  mhpkdata= requests.get("https://mg-online-01.com/api?packet=User&action=getGameDetail&terminal_id=1&id=26&lang=en")
  soupmhpk=bs(mhpkdata.content,'html.parser')
  datamhpk=soupmhpk.text
  data2mhpk=json.loads(datamhpk)

  arpkdata= requests.get("https://mg-online-01.com/api?packet=User&action=getGameDetail&terminal_id=1&id=27&lang=en")
  souparpk=bs(arpkdata.content,'html.parser')
  dataarpk=souparpk.text
  data2arpk=json.loads(dataarpk)



  temp=issue
  issue=int(data2['data']['last_issue']['issue'])
  if(temp!=issue):
   f = open("bot.txt", "a")
   num=int(data2['data']['last_issue']['wn_number'][0])+ int(data2['data']['last_issue']['wn_number'][1])
   numaapk=int(data2aapk['data']['last_issue']['wn_number'][0])+ int(data2aapk['data']['last_issue']['wn_number'][1])
   numcapk=int(data2capk['data']['last_issue']['wn_number'][0])+ int(data2capk['data']['last_issue']['wn_number'][1])
   numgrpk=int(data2grpk['data']['last_issue']['wn_number'][0])+ int(data2grpk['data']['last_issue']['wn_number'][1])
   nummhpk=int(data2mhpk['data']['last_issue']['wn_number'][0])+ int(data2mhpk['data']['last_issue']['wn_number'][1])
   numarpk=int(data2arpk['data']['last_issue']['wn_number'][0])+ int(data2arpk['data']['last_issue']['wn_number'][1])




   for i in range (3,20):
     srpklist[i]=srpklist[i]+1
     aapklist[i]=aapklist[i]+1
     capklist[i]=capklist[i]+1
     grpklist[i]=grpklist[i]+1
     mhpklist[i]=mhpklist[i]+1
     arpklist[i]=arpklist[i]+1

   f.write(str(issue))
   f.write("     ")
   f.write(str(data2['data']['current_issue']['begin_time']))
   f.write("\n")  
   now = datetime.now().time() 

   f.write(str(now))
   f.write("\n")
   f.write("suc srpk:")
   f.write(str(num))
   f.write(" fell at ")
   f.write(str(srpklist[num]))


   f.write("     ")
   f.write("mg capk:")
   f.write(str(numcapk))
   f.write(" fell at ")
   f.write(str(capklist[numcapk]))

   f.write("     ")
   f.write("aapk:")
   f.write(str(numaapk))
   f.write(" fell at ")
   f.write(str(aapklist[numaapk]))

   f.write("     ")
   f.write("grpk:")
   f.write(str(numgrpk))
   f.write(" fell at ")
   f.write(str(grpklist[numgrpk]))

   f.write("     ")
   f.write("mhpk:")
   f.write(str(nummhpk))
   f.write(" fell at ")
   f.write(str(mhpklist[nummhpk]))

   f.write("     ")
   f.write("arpk:")
   f.write(str(numarpk))
   f.write(" fell at ")
   f.write(str(arpklist[numarpk]))


   f.write("\n") 

   srpklist[num]=0
   aapklist[numaapk]=0
   capklist[numcapk]=0
   grpklist[numgrpk]=0
   mhpklist[nummhpk]=0
   arpklist[numarpk]=0

   f.write("\n")
   
   f.write(str(issue))
   f.write("\n")
   f.write("srpklist=")

   f.write(str(srpklist))
   f.write("\n")
   f.write("aapklist=")

   f.write(str(aapklist))
   f.write("\n")
   f.write("capklist=")
  
   f.write(str(capklist))
   f.write("\n")
   f.write("grpklist=")
  
   f.write(str(grpklist))
   f.write("\n")
   f.write("mhpklist=")
   
   f.write(str(mhpklist))
   f.write("\n")
   f.write("arpklist=")
  
   f.write(str(arpklist))
   f.write("\n")
  
   for i in range(3,20):
    f.write(str(i)+":"+ "sus srpk  "+str(srpklist[i])+";     "+"mg capk: "+str(i)+": " + str(capklist[i]) +";     "+"aapk: "+str(i)+": " + str(aapklist[i])+";     "+"grpk: "+str(i)+": " + str(grpklist[i])+";     "+"mhpk: "+str(i)+": " + str(mhpklist[i])+";     "+"arpk: "+str(i)+": " + str(arpklist[i])+"\n")
    
    
   f.write("\n\n") 
   f.close() 
  
    
  time.sleep(t2)

"""from keep_alive import keep_alive
import time
from bs4 import BeautifulSoup as bs
import json
import requests


keep_alive()
list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
list2=[0, 0, 0, 39, 75, 13, 2, 24, 14, 12, 4, 0, 23, 16, 5, 30, 33, 11, 61, 68]

issue=0
while(1):
    
  page = requests.get("https://www.wealth3333.net/api?packet=User&action=getGameDetail&terminal_id=1&id=25&lang=en")
  soup = bs(page.content,'html.parser')
  data=soup.text
  data2=json.loads(data)  
  temp=issue
  issue=int(data2['data']['last_issue']['issue'])
  if(temp!=issue):
   f = open("demofile2.txt", "a")
   num=int(data2['data']['last_issue']['wn_number'][0])+ int(data2['data']['last_issue']['wn_number'][1])
   for i in range (3,20):
     list2[i]=list2[i]+1
   f.write(str(num))
   f.write("fell at")
   f.write(str(list2[num]))
   f.write("\n")  
   list2[num]=0
   f.write(str(issue))
   f.write("\n")
   f.write(str(num))
   f.write("\n")
   """"""f.write(str(list))
   f.write("\n")
   f.write(str(list2))""""""
  
   for i in range(3,20):
    f.write(str(i)+":"+str(list2[i])+"; ")
   f.write("\n\n") 
   f.close() 
  
    
  time.sleep(300)
""""""def fun2():
 web_site = Flask(__name__)
 @web_site.route('/')
 def index():
	  return render_template('demofile2.txt')
 @web_site.route('/user/', defaults={'username': None})
 @web_site.route('/user/<username>')



 web_site.run(host='0.0.0.0', port=8080) 

if __name__ == "__main__":
    
    t1 = threading.Thread(target=fun)
    t2 = threading.Thread(target=fun2)
  
    
    t1.start()
   
    t2.start()"""

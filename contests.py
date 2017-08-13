import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import subprocess as s

myurl='https://www.codechef.com/contests'

uclient=ureq(myurl)
page_html=uclient.read();
uclient.close()

ps=soup(page_html,"html.parser")
c=ps.findAll("tbody")
container=c[1].findAll("tr")

s.call(['notify-send',"Upcoming Contests:\n"])

for i in container:
	k=i.findAll("td")
	s.call(['notify-send',"Contest Name: "+str(k[1].text),"Contest Duration: " + str(k[2].text) + " - " + str(k[3].text)])

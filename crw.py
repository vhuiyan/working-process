# imports
import scr
import sys
from datetime import datetime, timedelta
from time import sleep
from fake_useragent import UserAgent

agents = UserAgent()

with open('output/2020-01-18.txt') as f:
    contents = f.readlines()
    num = 1
    for content in contents:
        agent = agents.random
        currenturl = 'https://en.prothomalo.com'+content
        name = '2020-01-18_'+str(num)
        print("@@@@@@ Started: Url: ", currenturl)
        scr.scrap(currenturl, name, agent)
        sleep(0.3)
        print("@@@@@@ Ended: Url: ", currenturl)
        num+=1



print("#################Firt File Done.... ###############")


with open('output/2020-01-19.txt') as f:
    contents = f.readlines()
    num = 1
    for content in contents:
        agent = agents.random
        currenturl = 'https://en.prothomalo.com'+content
        name = '2020-01-19_'+str(num)
        print("@@@@@@ Started: Url: ", currenturl)
        scr.scrap(currenturl, name, agent)
        sleep(0.3)
        print("@@@@@@ Ended: Url: ", currenturl)
        num+=1
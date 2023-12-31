import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import keyboard
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

options = Options()
listofteams = ["LIV","AST","TOT","MCI","NEW","EVE","WHU","CHE","CRY","MUN","NOT","FUL","ARS","SHU","BHA","WOL","LUT","BUR","BRE","BOU"]
options.add_argument('--headless=new')
PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://www.betpawa.rw/virtual-sports?virtualTab=upcoming")
time.sleep(4)
homeTeam= []
fulllist=[]
homeOdds=[]
drawOdds=[]
awayOdds=[]
awayTeam= []
wins={}
draws={}
losses={}
gd={}
homePastWins=[]
awayPastWins=[]
homePastDraws=[]
awayPastDraws=[]
homePastLosses=[]
awayPastLosses=[]
homeGoalDiff=[]
awayGoalDiff=[]
result=[]
k=0
while k<12:
    league = driver.find_element(By.CLASS_NAME,'separator-wrapper')
    match= league.find_elements(By.CLASS_NAME,"events-container")
    k=10
    driver1 = webdriver.Chrome(service=s, options=options)
    driver1.get("https://www.betpawa.rw/virtual-sports?virtualTab=results")
    time.sleep(2)
    league1 = driver1.find_element(By.CLASS_NAME, 'separator-wrapper')
    positions = league1.find_elements(By.CLASS_NAME, 'standings-row')
    for i in range(len(positions)):
        nameTeam = positions[i].find_element(By.CLASS_NAME, 'team')
        attr = positions[i].find_elements(By.TAG_NAME, 'td')
        wins[nameTeam.text] = int(attr[2].text)
        draws[nameTeam.text] = int(attr[3].text)
        losses[nameTeam.text] = int(attr[4].text)
        gd[nameTeam.text] = eval(attr[5].text.replace(":","-"))
        #add goal difference
    for i in range(0, len(match)):
        teams = match[i].find_element(By.CLASS_NAME, 'title')
        playingTeams = teams.text.split("-")
        print(playingTeams)
        odds=match[i].find_elements(By.CLASS_NAME,'event-odds')
        homeOdds.append(float(odds[0].text))
        drawOdds.append(float(odds[1].text))
        awayOdds.append(float(odds[2].text))
        for j in range(len(playingTeams)):
            oneofem = playingTeams[j].replace(" ","")
            if oneofem in listofteams:
                if j==0:
                    homeTeam.append(int(listofteams.index(playingTeams[j].replace(" ",""))))
                    homePastWins.append(wins[oneofem])
                    homePastDraws.append(draws[oneofem])
                    homePastLosses.append(losses[oneofem])
                    homeGoalDiff.append(gd[oneofem])
                else:
                    awayTeam.append(int(listofteams.index(oneofem.replace(" ",""))))
                    awayPastWins.append(wins[oneofem])
                    awayPastDraws.append(draws[oneofem])
                    awayPastLosses.append(losses[oneofem])
                    awayGoalDiff.append(gd[oneofem])
    x = time.time() // 60
    if x%10 > 4:
        print((10-x%5))
        sleepTime = (10-x%5)*60
    else:
        print((10 - x % 5))
        sleepTime = (10-x%5)*60
    if x%10==0:
        sleepTime = 600
    time.sleep(sleepTime)
    clickon = driver1.find_elements(By.CLASS_NAME,'tabs-selector')
    clickon[-1].click()
    matchday = int(driver1.find_element(By.CLASS_NAME,'round-number').text)-2
    actualday = driver1.find_elements(By.CLASS_NAME,'matchday')
    print(matchday)
    actualday[matchday].click()
    time.sleep(2)
    league2 = driver1.find_element(By.CLASS_NAME, 'separator-wrapper')
    scores = league2.find_elements(By.CLASS_NAME, 'score')
    for i in range(len(scores)):
        fullTime = scores[i].find_elements(By.TAG_NAME,'span')
        go = eval(fullTime[-1].text)
        if go > 0 :
            result.append(0)
        elif go==0 :
            result.append(1)
        else:
            result.append(2)
    k+= 1

fulllist = zip(homeTeam,awayTeam,homeOdds,drawOdds,awayOdds,homePastWins,homePastDraws,homePastLosses,awayPastWins,awayPastDraws,awayPastLosses,homeGoalDiff,awayGoalDiff,result)
df = pd.DataFrame(fulllist)
df.to_csv("data.csv", header=['homeTeam','awayTeam',"homeOdds","drawOdds","awayOdds","homePastWins","homePastDraws","homePastLosses","awayPastWins","awayPastDraws","awayPastLosses","homeGoalDiff","awayGoalDiff","result"])

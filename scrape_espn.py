#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:56:37 2018

@author: evan
"""


from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('ESPN_Draft_Order_Scrape.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Pick Number','Player Name','Team Name','Position']) 

def scrapeEspnForDraftOrder(html):
    
    rounds = [1,2,3,4,5,6,7]
    teams = []
    positions = []
    playerNames = []
    
    
    for currentRound in rounds:
        html = html[:-1] + str(currentRound)
        print(html)
        source = requests.get(html).text
        soup = BeautifulSoup(source, 'lxml')
        articles = soup.findAll('article')

        for article in articles:
        
            for team in article.find_all('span', class_='draftTable__headline draftTable__headline--team'):
                #print(str(team.contents[0]).split('/')[10].split('.')[0]) #Extract only the team name
                teams.append(str(team.contents[0]).split('/')[10].split('.')[0])
        
            for position in article.find_all('span', class_='draftTable__headline draftTable__headline--pos'):
                positions.append(position.contents)
                #print(position.contents)
    
            for playerName in article.find_all('span',class_='draftTable__headline draftTable__headline--player'):
                playerNames.append(playerName.contents)
                #print(playerName.contents)
            
    for index in range(0,len(teams)):
        #print(playerNames[index],[teams[index]],positions[index])
        print([index+1,playerNames[index][0],teams[index],positions[index][0]])
        csv_writer.writerow([index+1,playerNames[index][0],teams[index],positions[index][0]])
    
html = 'http://www.espn.com/nfl/draft/rounds/_/round/1'
scrapeEspnForDraftOrder(html)

csv_file.close()

#print(teams)
    #for playerInfoCollapsed in article.find_all('div',class_='draftTable__header collapsed'):
    #    print(playerInfoCollapsed)
        
# Extract order: (pick 1, 2, 3, etc)
# Extract player name: (Saquon barkely (example))
# Extract Position.
# Extract hyperlink to additional information.

# Create a new CSV with the following info:

# Pick #, Player Name   , Position, Hyperlink to more info
# 1     , Baker Mayfiel , QB      , https://___


# Pull in this information for all rounds.

#for article in soup.find_all('article')

#soup.

#article = soup.find('article')

#print(article)


# Goal:
    
# I want a dataset with all players, their draft order, their team, and their position. 
    
# I think want to be able to filter that table by position. 


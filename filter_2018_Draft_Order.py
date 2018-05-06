#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 20:00:05 2018

@author: Evan Baker

Purpose: to filter the 2018 Draft order down to QB, RB, WR, TE.  The positions
that we specifically care the most about for fantasy football.

Note that QBs are weighted much more heavily in the NFL, although QBs are picked
very early in the NFL - we do not need to pick them early in our draft since we
only start 1 QB per game, we have 10 teams, and we need to start 4 RBs or WRs
per game.

Our Starting line-up involves 1 QB, 2 RB, 2 WR, 2 Flex, 1 TE.

This draft order causes RB, WR, TE to all be more valuable than the QB position.


Input: 'ESPN_Draft_Order_Scrape.csv'

Output: 'Filtered_ESPN_Draft_Order.csv'

"""

import pandas

#text = open('ESPN_Draft_Order_Scrape.csv').read()

#print(text)

df = pandas.read_csv('ESPN_Draft_Order_Scrape.csv')

qbOnly = df[df['Position'].str.contains("QB")]

rbOnly = df[df['Position'].str.contains("RB")]

wrOnly = df[df['Position'].str.contains("WR")]

teOnly = df[df['Position'].str.contains("TE")]

frames = [qbOnly,rbOnly,wrOnly,teOnly]

result = pandas.concat(frames)

result.to_csv('Filtered_ESPN_Draft_Order.csv') # , sep='\t'

sortedResult = result.sort_values(by=['Pick Number'])

sortedResult.to_csv('Sorted_Filtered_ESPN_Draft_Order.csv')
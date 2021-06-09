from typing import Dict
import xml
import xml.etree.ElementTree as ET
import requests
import csv
from requests.api import get

r = requests.get('https://www.ourcommons.ca/members/en/votes/43/2/130/xml')
status = r.status_code
data = r.text
XMLRoot = ET.fromstring(data)

RidingDict = dict()
with open('RidingNames.csv',encoding='utf-8') as NameFile:
    FileReader = csv.reader(NameFile)
    for row in FileReader:
        row0 = row[0]
        row1 = row[1]
        RidingDict[row[1]] = row[0]
    print(RidingDict)

print(status)

for Voter in XMLRoot:
    Riding = Voter.find('ConstituencyName').text
    RidingID = RidingDict[Riding]
    Party = Voter.find('CaucusShortName') 
    print(RidingID)
    print(Party.text)
    YesVote = Voter.find('IsVoteYea').text == 'true'
    if YesVote:
        print('Y')
    else:
        print('N')
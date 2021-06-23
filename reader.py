from typing import Dict
import xml
import xml.etree.ElementTree as ET
import requests
import csv
from requests.api import get
import sys
#sys.path.append("C:/OSGeo4W64/apps/qgis/python")
#from qgis.core import *
#QgsApplication.setPrefixPath('C:/OSGEO4~1/apps/qgis', True)
#qgs = QgsApplication([],False)
#qgs.initQgis()
r = requests.get('https://www.ourcommons.ca/members/en/votes/43/2/136/xml')
status = r.status_code
data = r.text
XMLRoot = ET.fromstring(data)
RidingDict = dict()
RidingList = list()

#Dictionary
with open('RidingNames.csv',encoding='utf-8') as NameFile:
    FileReader = csv.reader(NameFile)
    for row in FileReader:
        row0 = row[0]
        row1 = row[1]
        RidingDict[row[1]] = row[0]
        RidingList.append(row[0])
    print(RidingDict)

DataFile =  open('data.csv','w',newline='',encoding='utf-8')
FileWriter = csv.writer(DataFile)

print(status)

#Writing to file

FileWriter.writerow(['FEDNUM','Riding','Party','Vote'])
for Voter in XMLRoot:
    Riding = Voter.find('ConstituencyName').text
    RidingID = RidingDict[Riding]
    Party = Voter.find('CaucusShortName').text
    print(Riding)
    print(RidingID)
    print(Party)
    YesVote = Voter.find('IsVoteYea').text == 'true'
    if YesVote:
        print('Y')
    else:
        print('N')
    FileWriter.writerow([RidingID,Riding,Party,YesVote])

#qgs.exitQgis()
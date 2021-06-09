import xml
import xml.etree.ElementTree as ET
import requests
import csv
from requests.api import get

r = requests.get('https://www.ourcommons.ca/members/en/votes/43/2/130/xml')
status = r.status_code
data = r.text
XMLRoot = ET.fromstring(data)


print(status)
for Voter in XMLRoot:
    Riding = Voter.find('ConstituencyName')
    Party = Voter.find('CaucusShortName') 
    print(Riding.text)
    print(Party.text)
    YesVote = Voter.find('IsVoteYea').text == 'true'
    if YesVote:
        print('Y')
    else:
        print('N')

    

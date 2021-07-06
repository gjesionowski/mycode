#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import urllib.request
import json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    ####### urllib.request version #######

    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    ## put fileobject into helmet
    helmet = groundctrl.read()
    
    ## decode JSON to Python data structure
    helmetson = json.loads(helmet.decode('utf-8'))
    
    ## display our Pythonic data
    #print("\n\nConverted Python data")
    #print(helmetson)
    
    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    #print(people)
    for astro in people:
       print(astro['name'], " on the ", astro['craft'])

    ####### requests module version #######
    
    ## Calls web service, converts to JSON
    helmetson2= requests.get('http://api.open-notify.org/astros.json').json()
    
    ## print n
    print("People in space:",helmetson2["number"])
    
    for astronaut in helmetson2["people"]:
        print(f'{astronaut["name"]} is on the {astronaut["craft"]}')

main()

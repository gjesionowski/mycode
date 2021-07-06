#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard library
from datetime import date
# import webbrowser

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=QvKY4Eb5RG9Nr3O0EIScBzNiMBoEJrCDLdvzG0OG' ## this is our api key

## pretty print json
def main():
    """run-time code"""

    ## Variables
    today = date.today()
    d = "&date=" + today.isoformat()

    print("The default request is for today's date. Would you like to request a particular date? Yes/No:")
    answer = input()
    if answer == 'Yes' or answer == 'yes':
        d = "&date=" + input("Enter the date in the format YEAR-MM-DD:")
    nasaapiobj = requests.get(NASAAPI + MYKEY + d) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json
    print(nasaread) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread['explanation']) # display the value for the key explanation
    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))


    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

main()


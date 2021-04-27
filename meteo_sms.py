#!/home/pi/meteo_sms/myenv/bin/python

import feedparser
from config import *
from twilio.rest import Client



def main():

    account_sid = twilio_acount_id
    auth_token = twilio_auth_token
    client = Client(account_sid, auth_token)


    bbc_feed = feedparser.parse('https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/2654675')
    
    entry_title = bbc_feed.entries[0].title

    
    message = client.messages \
                .create(    
                     body=entry_title,
                     from_=twilio_number,
                     to=my_number
                 )

if __name__ == "__main__":
    main()


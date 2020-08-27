import requests
import json
import kirjava
from datetime import datetime
from secrets import BEARER_TOKEN, TWITTER_ID, LYTIKO_TOKEN, FOLLOWING_ID, FOLLOWERS_ID
#Generate your Bearer Token for your application on the Twitter Dev Portal
#This can be looked up by hitting the /users/by/username/yourusername endpoint
DATE = int(datetime.now().timestamp())

auth_header = 'Bearer ' + BEARER_TOKEN
headers = {'Authorization': auth_header}

endpoint = f'https://api.twitter.com/2/users/{TWITTER_ID}?&user.fields=public_metrics'
r = requests.get(endpoint, headers=headers).json()
#print(r)
#data = json.loads(r.text)
FOLLOWING_COUNT=r['data']['public_metrics']['following_count']
FOLLOWERS_COUNT=r['data']['public_metrics']['followers_count']
# Select your transport with a defined url endpoint
#
# Create a GraphQL client using the defined transport

#
# Provide a GraphQL query
following_mutation = """
    mutation {createMeasurement(
        quantity: """ + FOLLOWING_ID + """,
        value:""" + str(FOLLOWING_COUNT) + """,
        timezone: "Europe/London",
        datetime:"""+ str(DATE) + """
    )
    { measurement {id}}
    }
"""
followers_mutation= """
    mutation {createMeasurement(
        quantity: """ + FOLLOWERS_ID + """,
        value:""" + str(FOLLOWERS_COUNT) + """,
        timezone: "Europe/London",
        datetime:"""+ str(DATE) + """
    )
    { measurement {id}}
    }
"""

lytiko_url = "https://api.lytiko.com/graphql"
print(kirjava.execute(lytiko_url, following_mutation, headers={"Authorization": f"{LYTIKO_TOKEN}"}))
print(kirjava.execute(lytiko_url, followers_mutation, headers={"Authorization": f"{LYTIKO_TOKEN}"}))

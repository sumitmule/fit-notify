from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from google_auth_oauthlib.flow import Flow
import re
from datetime import date
import pandas as pd
import re

flow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=["https://www.googleapis.com/auth/calendar"],
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')

# Tell the user to go to the authorization URL.
auth_url, _ = flow.authorization_url(prompt='consent')

print('Please go to this URL: {}'.format(auth_url))

# The user will get an authorization code. This code is used to get the
# access token.
code = input('Enter the authorization code: ')
credentials = flow.fetch_token(code=code)

pickle.dump(credentials, open('token.pkl','wb'))
credentials = pickle.load(open('token.pkl','rb'))
service = build('calendar','v3',credentials=flow.credentials)
result = service.calendarList().list().execute()
calendar_id = result['items'][3]['id']
print(result)

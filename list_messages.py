# adapted from:  https://github.com/gsuitedevs/python-samples/blob/master/gmail/quickstart/quickstart.py

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Gmail API
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly' #todo: use the read/write scope
store = file.Storage('credentials.json') # a file to be created
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_id.json', SCOPES) # refers to the credentials file we downloaded
    # this is throwing... oauth2client.clientsecrets.InvalidClientSecretsError: Missing property "redirect_uris" in a client type of "web".
    # need to re-create the credentials file using "Other UI (Windows, cli)"
    # after doing this, you should see Your browser has been opened to visit: https://accounts.google.com/o/oauth2/auth?client_id....
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))

# Call the Gmail API
results = service.users().labels().list(userId='me').execute()
labels = results.get('labels', [])
if not labels:
    print('No labels found.')
else:
    print('Labels:')
    for label in labels:
        print(label['name'])

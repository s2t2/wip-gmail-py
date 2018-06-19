from apiclient.discovery import build
import json
import pdb

#service = build('api_name', 'api_version', ...)
#collection = service.stamps()
#nested_collection = service.featured().stamps()
#request = collection.list(cents=5)
#response = request.execute()
#response = service.stamps().list(cents=5).execute()
#print json.dumps(response, sort_keys=True, indent=4)

# what is the list of valid service names and versions though?
# maybe let's try this to get started?
#
# service = build('gmail', 'v1')
#
#> googleapiclient.errors.HttpError: <HttpError 403 when requesting https://gmail.googleapis.com/$discovery/rest?version=1 returned "The request cannot be identified with a project. Please pass a valid API key with the request.">

pdb.set_trace()

# try again:
service = build('gmail', 'v1')
# fail again:
#> google.auth.exceptions.DefaultCredentialsError: Could not automatically determine credentials. Please set GOOGLE_APPLICATION_CREDENTIALS or explicitly create credentials and re-run the application. For more information, please see https://developers.google.com/accounts/docs/application-default-credentials.
# visiting the URL from the error message...
# not helpful
# found a google sheets example at _______ like:

# or actually follow the instructions at: https://developers.google.com/gmail/api/quickstart/python

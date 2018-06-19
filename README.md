# My GMail App

## Credits, Notes, and Reference

  + https://developers.google.com/gmail/api/
  + https://github.com/google/google-api-python-client
  + https://developers.google.com/api-client-library/python/start/get_started
  + https://developers.google.com/apis-explorer/#p/
  + https://developers.google.com/apis-explorer/#search/gmail/gmail/v1/
  + https://developers.google.com/gmail/api/guides/
  + https://github.com/google/google-api-python-client/blob/master/googleapiclient/discovery.py#L168-L233
  + https://cloud.google.com/docs/authentication/getting-started
  + https://developers.google.com/gmail/api/quickstart/python

## Setup

Visit https://developers.google.com/apis-explorer/#search/gmail/gmail/v1/, then click the button on the right side of the page to turn ON: "Authorize requests using OAuth 2.0". This will prompt you to choose an appropriate "scope" and perhaps also to sign in to your google account to provide authorization.

JK??

Retry:

  1. Visit https://console.developers.google.com/flows/enableapi?apiid=gmail&pli=1 and "Create a Project".
  2. When you see "The API is enabled", click "go to credentials"
  3. Fill in the form with the following info, then click "What credentials do I need?":
    + Which API are you using? "Gmail API"
    + Where will you be calling the API from? "Web server (e.g. node.js)"
    + What data will you be accessing? "User data"
  4. Create an OAuth 2.0 client ID, choosing a name of your choice. Like maybe "nyu-2335-gmail-app". Leave the "restrictions" sections blank, then click "Create Oauth Client ID"
  5. Fill in the info for "Set up the OAuth 2.0 consent screen" and click to proceed.
  6. Note the `Client ID`. Then download the entire credentials JSON file (`client_id.json`), and move it into the root directory of this repository. NOTE: this credentials file is/should be ignored/excluded from version control.






## Installation

```sh
pipenv install -r requirements.txt
pip3 install -r requirements.txt
pip install -r requirements.txt
```

## Usage

```sh
python3 list_messages.py
python list_messages.py
```

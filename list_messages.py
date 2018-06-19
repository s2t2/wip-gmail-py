from apiclient.discovery import build
import json

service = build('api_name', 'api_version', ...)
collection = service.stamps()
nested_collection = service.featured().stamps()
request = collection.list(cents=5)
response = request.execute()
response = service.stamps().list(cents=5).execute()
print json.dumps(response, sort_keys=True, indent=4)

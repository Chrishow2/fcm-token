import google.auth.transport.requests
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']

def generate_access_token(service_account_file):
    credentials = service_account.Credentials.from_service_account_file(
        service_account_file,
        scopes=SCOPES
    )
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)

    return credentials.token

access_token = generate_access_token('service_account_file.json')
print(access_token)
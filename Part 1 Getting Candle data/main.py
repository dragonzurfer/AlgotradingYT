from fyers_api import fyersModel
from fyers_api import accessToken
import json

apiCredFile = open("./apicred.json")
apiCredJson = json.load(apiCredFile)

client_id = apiCredJson["ClientID"]
secret_key = apiCredJson["SecretID"]
redirect_uri = apiCredJson["RedirectURI"]
response_type = "success"


session=accessToken.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri, 
    response_type="code",
    grant_type="authorization_code",
    state=response_type
)

url = session.generate_authcode()
print(url)

auth_code = input("Enter auth code: ")
session.set_token(auth_code)
token_response = session.generate_token()

# Serializing json
tokenResponse_object = json.dumps(token_response, indent=4)

with open("store_token.json", "w") as outfile:
    outfile.write(tokenResponse_object)


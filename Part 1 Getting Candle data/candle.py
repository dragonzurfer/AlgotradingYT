from fyers_api import fyersModel
import json

# get token
tokenFile = open("./store_token.json")
tokenJson = json.load(tokenFile)
access_token = tokenJson["access_token"]

# get client id
apiCredFile = open("./apicred.json")
apiCredJson = json.load(apiCredFile)
client_id = apiCredJson["ClientID"]

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="/Users/drago/Documents/ytFyersAPI")

data = {
            "symbol":"NSE:NIFTY50-INDEX",
                "resolution":"D",
                    "date_format":"0",
                        "range_from":"1666310400",
                            "range_to":"1666441392",
                                "cont_flag":"1"
                                    }
response = fyers.history(data)
print(response)

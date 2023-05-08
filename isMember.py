import os
import requests
from dotenv import load_dotenv

load_dotenv()

def discordAuthentication(nickName):
    URL  = os.getenv("URL")
    params = {"hangul": nickName}

    response = requests.get(URL, params=params)
    if response.status_code == 200:
        content = response.text
        result = content.split()[-1]
    
        if result in ['YESYESYES', 'NONONO', 'OLDOLDOLD']:
            return result
        else:
            return "Error: No matching result found"
    else:
        return "Error: Unable to fetch data from external server"
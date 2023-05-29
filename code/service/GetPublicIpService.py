import requests
from bs4 import BeautifulSoup
from utility.GetConfig import GetConfig


class GetPublicIpService:
    def __init__(self):
        # get config global
        getConfig = GetConfig()
        getConfig.load('checkIp')
        self.hostCheckIp = getConfig.main()
        self.ipTmp = None

    def checkIp(self) -> str:
        try:
            getIpWeb = requests.get(self.hostCheckIp)
            if getIpWeb.status_code == 200:
                soup = BeautifulSoup(getIpWeb.content, 'html.parser')
                ip_text = soup.find('body').text.replace('Current IP Address: ', '')
                self.ipTmp = ip_text
                return ip_text
            else:
                print("request response:", str(getIpWeb.status_code))
                return self.ipTmp

        except Exception as e:
            print("exception:", str(e))
            return self.ipTmp

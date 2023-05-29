import requests
from utility.GetConfig import GetConfig


class SendDataUpdateDnsService:
    def __init__(self):
        # get config global
        getConfig = GetConfig()
        getConfig.load('dns')
        self.dnsService = getConfig.main()

    def sendData(self, ip: str):
        print(self.dnsService)
        for item in self.dnsService:
            urlUpdateDns = item['url'].replace('{IP-PUBLIC}', ip)
            clientHttp = requests.get(urlUpdateDns)
            print(urlUpdateDnsclientHttp.content)
        return ip

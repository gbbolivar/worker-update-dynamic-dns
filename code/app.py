#!/usr/bin/python
import time

from multiprocessing import Process
from service.GetPublicIpService import GetPublicIpService
from service.SendDataUpdateDnsService import SendDataUpdateDnsService


def main():
    getHost = GetPublicIpService()
    serv = SendDataUpdateDnsService()
    dataTmp = ''
    while True:
        ipNow = getHost.checkIp()

        if dataTmp != ipNow:
            serv.sendData(ipNow)
            dataTmp = ipNow
        # Sleep 10 seconds
        time.sleep(10)


if __name__ == '__main__':
    p = Process(target=main)
    p.start()

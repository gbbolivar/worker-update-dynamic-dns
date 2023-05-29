import json


class GetConfig:
    def __init__(self):
        self.idx = ''

    def load(self, idx):
        self.idx = idx

    def main(self):
        try:
            with open('/config/config.json') as config:
                data = json.load(config)
                return data[self.idx]
        except json.decoder.JSONDecodeError:
            print('Error in format JSONDecodeError')

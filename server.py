import yaml
import Modules


with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


class Server:
    _Mudules = {}

    # TODO : Add S3 Logic and Data Execute Logic

    def __init__(self):
        self._Mudules['Service1'] = Modules.Service1
        self._Mudules['Service2'] = Modules.Service2

    def handler(self, data):
        print('1', data)
        task = self._execute(data)

    def _execute(self, data):

        return data
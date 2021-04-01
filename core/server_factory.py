import os
from core.server.browserstack import Browserstack
from core.server.seleneium_standalone import SeleniumStandalone


class ServerFactory:
    # Can add server for testing (selenium standalone, browserstack and etc)
    server_map = []

    def get_server(self):
        if 'server' not in os.environ:
            raise Exception('Please, set ENV "server"')

        env = os.environ['server']

        if env not in self.server_map:
            raise Exception(f"Unknown value of ENV 'server'. Known list: {', '.join(self.server_map)}. Got: {env}")

        if env == 'selenium_standalone':
            return SeleniumStandalone()

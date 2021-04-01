from core.server_factory import ServerFactory


class Base:
    url = ""

    driver = None
    server = None

    def setup(self):
        self.server = ServerFactory().get_server()
        self.driver = self.server.get_driver()
        self.open_page_for_web()

    def teardown(self):
        self.driver.quit()

    def open_page_for_web(self):
        if self.server:
            self.driver.get(self.url)
        else:
            print("Method open_page_for_web does nothing for none web ENV")
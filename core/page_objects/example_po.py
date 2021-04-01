from core.main_page_object import MainPageObject


class SearchPO(MainPageObject):
    LOCATOR = ''

    def init_search(self):
        element = self.wait_for_element_present(
            self.LOCATOR,
            "Cannot find search init wrapper"
        )
        element.click()

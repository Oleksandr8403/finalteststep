from .base_page import BasePage


# During the development process, we moved some methods from this class to the base class
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

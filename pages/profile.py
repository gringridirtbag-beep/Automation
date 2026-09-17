from pages.basepage import BasePage


class Profile(BasePage):
    USERNAME_LABEL =  "#userName-value"
    BOOKS_BUTTON = "#gotoStore"

    def GoToBookStore(self):
        self.click(self.BOOKS_BUTTON)
        

   

   

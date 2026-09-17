from pages.basepage import BasePage

class Login(BasePage):
    USERNAME_TEXTFIELD = "#userName"
    PASSWORD_TEXTFIELD =  "#password"
    LOGIN_BUTTON =  "#login"

    def navigate_login(self,base_url):
        self.navigate_url(f"{base_url}/login")
    
   
        
    def login(self, user, password):
        self.fill(self.USERNAME_TEXTFIELD,user)
        self.click(self.LOGIN_BUTTON)
        self.fill(self.PASSWORD_TEXTFIELD,password)
        self.click(self.LOGIN_BUTTON)
        
        
 

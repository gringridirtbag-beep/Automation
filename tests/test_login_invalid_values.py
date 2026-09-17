from pages.login import Login
import pytest
from core.driver import Driver
from config.settings import BASE_URL,DEMOQA_USERNAME,DEMOQA_PASSWORD
from pages.profile import Profile
from testdata.login_data import invalid_data

@pytest.mark.parametrize(
        "username,password",
         invalid_data

)

def test_login_invalid(driver, username, password):

    
    login_page = Login(driver)
    login_page.navigate_url(BASE_URL)
    login_page.login(username, password)

    profile_page = Profile(driver)

    
    
    current_username = profile_page.get_locator_text(Profile.USERNAME_LABEL)
    print (current_username)

  

    assert "profile" in login_page.get_url()
    
    assert DEMOQA_USERNAME.lower() == current_username.lower(), f"Expected '{DEMOQA_USERNAME}',CURRENT: {current_username}"

 

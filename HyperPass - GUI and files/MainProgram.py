import auth_module
import login_modules
import USB_module
from selenium.webdriver.chrome.options import Options


#this is a test module
def main():
    '''
    auth_module.login(email='admin@hyperpass.com', password='adminstrator')
    hashed = auth_module.create_hash()
    login_modules.reconnect_db()
#    login_modules.unlock_db(bytearray('default', 'utf-8'))
    chrome_options = Options()
    global driver
    driver = login_modules.Browser()
    driver.driver.maximize_window()
    login_modules.login_facebook(driver)
    login_modules.login_instagram(driver)
'''
    login_modules.add_site_db("Reddit", "Omerkv", "ok021019")



if __name__ == "__main__":
    main()

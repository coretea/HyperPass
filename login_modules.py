from webbot import Browser

def login_instagram():
	web = Browser()
	web.go_to('https://www.instagram.com/accounts/login/')
	web.type('omer_kvartler' ,into='Phone number, username, or email' ,id='username')
	web.type('ok021019' , into='Password' , id='password')
	web.click('Log In')


def main():
	login_instagram()




if __name__== "__main__":
  main()
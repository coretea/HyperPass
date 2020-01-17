import sqlite3
from webbot import Browser

def login_instagram(username, password):
    web = Browser()
    web.maximize_window()
    web.go_to('https://www.instagram.com/accounts/login/')
    web.type(username, into='Phone number, username, or email', id='username')
    web.type(password, into='Password', id='password')
    web.click('Log In')

def login_facebook(username, password):
    web = Browser()
    web.maximize_window()
    web.go_to('facebook.com')
    web.type(username , into='Email')
    web.click('NEXT' , tag='span')
    web.type(password , into='Password' , id='pass')
    web.press(web.Key.ENTER)
    web.go_back()
    web.click('Sign in')


def main():
    con = sqlite3.connect('hyperpass_db.db')
    cur = con.cursor()
    #ogin to facebook
    cur.execute("SELECT * FROM users WHERE site='Facebook'")
    result = cur.fetchone()
    print(result)
    login_facebook(result[0], result[1])

    #login to instagram
    cur.execute("SELECT * FROM users WHERE site='Instagram'")
    result = cur.fetchone()
    print(result)
    login_instagram(result[0], result[1])

if __name__ == "__main__":
    main()

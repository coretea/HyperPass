import sqlite3
from webbot import Browser


def login_instagram(username, password):
    web = Browser()
    web.maximize_window()
    web.go_to('https://www.instagram.com/accounts/login/')
    web.type(username, into='Phone number, username, or email', id='username')
    web.type(password, into='Password', id='password')
    web.click('Log In')


def main():
    con = sqlite3.connect('hyperpass_db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE name = 'Admin'")
    result = cur.fetchone()
    print(result)
    login_instagram(result[0], result[1])


if __name__ == "__main__":
    main()

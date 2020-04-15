import sqlite3
from webbot import Browser
from pysqlsimplecipher import decryptor, encryptor
con = sqlite3.connect('hyperpass_db.db')
cur = con.cursor()



def login_spotify(web):
    web.go_to('https://accounts.spotify.com/en/login')
    # login to spotify
    cur.execute("SELECT * FROM users WHERE site='Spotify'")
    result = cur.fetchone()
    username = result[1]
    password = result[2]
    web.type(username, into='Email address or username', id='login-username')
    web.type(password, into='Password', id='login-password')
    web.click('Log In')

def login_instagram(web):
    web.go_to('https://www.instagram.com/accounts/login/')
    # login to instagram
    cur.execute("SELECT * FROM users WHERE site='Instagram'")
    result = cur.fetchone()
    print(result)
    username = result[1]
    password = result[2]
    web.type(username, into='Phone number, username, or email', id='username')
    web.type(password, into='Password', id='password')
    web.click('Log In')


def login_facebook(web):
    web.go_to('facebook.com')
    # login to facebook
    cur.execute("SELECT * FROM users WHERE site='Facebook'")
    result = cur.fetchone()
    username = result[1]
    password = result[2]
    web.type(username, into='Email')
    web.click('NEXT', tag='span')
    web.type(password, into='Password', id='pass')
    web.press(web.Key.ENTER)
    web.go_back()
    web.click('Sign in')

def reconnect_db():
    con = sqlite3.connect('hyperpass_db.db')
    cur = con.cursor()

def unlock_db(key):
    decryptor.decrypt_file("hyperpass_db.db", key, "hyperpass_db.db")


def lock_db(key):
    encryptor.encrypt_file("hyperpass_db.db", key, "hyperpass_db.db")

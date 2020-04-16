import sqlite3
from webbot import Browser
from pysqlsimplecipher import decryptor, encryptor
from selenium.webdriver.common.keys import Keys


global con
global cur
con = sqlite3.connect('emptydb.db')
cur = con.cursor()

def login_spotify(web):
    web.execute_script('''window.open("https://accounts.spotify.com/en/login","_blank");''')
    web.switch_to_tab(web.get_total_tabs())
    # login to spotify
    cur.execute("SELECT * FROM users WHERE site='Spotify'")
    result = cur.fetchone()
    username = result[1]
    password = result[2]
    web.type(username, into='Email address or username', id='login-username')
    web.type(password, into='Password', id='login-password')
    web.click('Log In')

def login_instagram(web):
    web.execute_script('''window.open("https://www.instagram.com/accounts/login/","_blank");''')
    web.switch_to_tab(web.get_total_tabs())
    # login to instagram
    cur.execute("SELECT * FROM users WHERE site='Instagram'")
    result = cur.fetchone()
    username = result[1]
    password = result[2]
    web.type(username, into='Phone number, username, or email', id='username')
    web.type(password, into='Password', id='password')
    web.click('Log In')


def login_facebook(web):
    web.execute_script('''window.open("https://www.facebook.com","_blank");''')
    web.switch_to_tab(web.get_total_tabs())
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

def login_reddit(web):
    web.execute_script('''window.open("https://www.reddit.com/login","_blank");''')
    web.switch_to_tab(web.get_total_tabs())
    cur.execute("SELECT * FROM users WHERE site='Reddit'")
    result = cur.fetchone()
    username = result[1]
    password = result[2]
    web.type(username, into='Username')
    web.type(username, into='Password')
    web.click('Sign in')

def login_twitter(web):
    web.execute_script('''window.open("https://www.twitter.com/login","_blank");''')
    web.switch_to_tab(web.get_total_tabs())
    cur.execute("SELECT * FROM users WHERE site='Twitter'")
    result = cur.fetchone()
    username = result[1]
    password = result[2]
    web.type(username,xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
    web.type(password, into='Password')
    web.click('Log in')

def login_github(web):
    web.execute_script('''window.open("https://github.com/login","_blank");''')
    web.switch_to_tab(web.get_total_tabs())
    cur.execute("SELECT * FROM users WHERE site='GitHub'")
    result = cur.fetchone()
    username = result[1]
    password = result[2]
    web.type(username, xpath='//*[@id="login_field"]')
    web.type(password, xpath='//*[@id="password"]')
    web.click('Sign in')

def login_pinterest(web):
    web.execute_script('''window.open("https://www.pinterest.com/login/","_blank");''')
    web.switch_to_tab(2)
    cur.execute("SELECT * FROM users WHERE site='Pinterest'")
    result = cur.fetchone()
    username = result[1]
    password = result[2]
    web.type(username, xpath='//[@id="email"]')
    web.type(password, xpath='//[@id="password"]')
    web.click('Log in')

def login_linkedIn(web):
    web.execute_script('''window.open("https://www.linkedin.com/uas/login?emailAddress=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3D%26location%3DHaifa%252C%2BIsrael%26trk%3Dpublic_jobs_jobs-search-bar_search-submit&trk=public_jobs_nav-header-signin%22","_blank");''')
    web.switch_to_tab(web.get_total_tabs())
    cur.execute("SELECT * FROM users WHERE site='LinkedIn'")
    result = cur.fetchone()
    username = result[1]
    password = result[2]
    web.type(username, xpath='//[@id="username"]')
    web.type(password, xpath='//[@id="password"]')
    web.click('Sign in')

#---------------db funcs-------------------------
def reconnect_db():
    global cur
    global con
    con = sqlite3.connect('F:\\hyperpass_db.db')
    cur = con.cursor()

def unlock_db(key):
    decryptor.decrypt_file("F:\\hyperpass_db.db", key, "F:\\hyperpass_db.db")

def get_sites():
    reconnect_db()
    cur.execute("SELECT site FROM users")
    result = cur.fetchall()
    return result

def lock_db(key):
    encryptor.encrypt_file("F:\\hyperpass_db.db", key, "F:\\hyperpass_db.db")

def add_site_db(site, username, password):
    reconnect_db()
    cur.execute("INSERT INTO users (site, username, password) VALUES (?,?,?)", (site, username, password))
    con.commit()

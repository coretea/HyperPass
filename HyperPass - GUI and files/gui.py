import tkinter as tk
from tkinter import *
import login_modules
import auth_module
import USB_module

HEIGHT = 700
WIDTH = 800



def login_all():
	login_modules.reconnect_db()
	sites = login_modules.get_sites()
	global driver
	driver = login_modules.Browser()
	driver.driver.maximize_window()
	print(sites)
	i = 0
	for i in range (0, len(sites)):
		if 'Instagram' in sites[i]:
			login_modules.login_instagram(driver)
		if 'Facebook' in sites[i]:
			login_modules.login_facebook(driver)
		if 'Twitter' in sites[i]:
			login_modules.login_twitter(driver)
		if 'Reddit' in sites[i]:
			login_modules.login_reddit(driver)
		if 'Spotify' in sites[i]:
			login_modules.login_spotify(driver)
		if 'GitHub' in sites[i]:
			login_modules.login_github(driver)
		if 'LinkedIn' in sites[i]:
			login_modules.login_linkedIn(driver)
		if 'Pinterest' in sites[i]:
			login_modules.login_pinterest(driver)

	login_modules.lock_db(bytearray(user['localId'], 'utf-8'))		

def add_sites(site_name):

	root_login = Tk()  # This now makes a new window.
	root_login.geometry('250x100+500+500')
	root_login.title('Login')  # This makes the window title 'login'

	nameL = Label(root_login, text='Username: ')  # More labels
	pwordL = Label(root_login, text='Password: ')  # ^

	nameL.grid(row=1, sticky=W)
	pwordL.grid(row=2, sticky=W)

	username_given = Entry(root_login)  # The entry input
	password_given = Entry(root_login, show='*')

	username_given.grid(row=1, column=1)
	password_given.grid(row=2, column=1)

	loginB = Button(root_login, text='Login', command=lambda: login_modules.add_site_db(str(site_name), username_given.get(), password_given.get()))  # This makes the login button, which will go to the CheckLogin def.
	loginB.grid(columnspan=2, sticky=W)


	root_login.mainloop()


#-------------------------------the start page function----------------------------------------

def start():

	global root_start

	root_start = Tk()  # This now makes a new window.
	root_start.title('Hello!')
	canvas = tk.Canvas(root_start, height=HEIGHT, width=WIDTH)
	canvas.pack()

	wallpaper_start = tk.PhotoImage(file='wallpaper.gif')
	wallpaper_start_label = tk.Label(root_start, image=wallpaper_start)
	wallpaper_start_label.place(relwidth=1, relheight=1)

	welcome_frame = tk.Frame(root_start, bg="GREY9", bd=5)
	welcome_frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor='n')

	welcome_label = tk.Label(welcome_frame, text="Welcome to HyperPass program", bg='grey9', fg='white', font=9)
	welcome_label.place(relwidth=0.90, relheight=0.8, relx=0.5, rely=0.1, anchor='n')

	login_button = Button(root_start, text='Login', command=Login)  # This makes the login button, which will go to the CheckLogin def.
	login_button.place(relwidth=0.4, relheight=0.1, relx=0.05, rely=0.6)

	register_button = Button(root_start, text='Register', bg="white", command=signup)
	register_button.place(relwidth=0.4, relheight=0.1, relx=0.55, rely=0.6)



	root_start.mainloop()
#------------------------------------login function----------------------------------------------
def login_seq(username, password):
	auth_module.login(username, password)
	root_login.destroy()
	root_start.destroy()

def Login():
	global nameEL
	global pwordEL
	global root_login

	root_login = Tk()  # This now makes a new window.
	root_login.geometry('250x100+500+500')
	root_login.title('Login')  # This makes the window title 'login'


	nameL = Label(root_login, text='Username: ')  # More labels
	pwordL = Label(root_login, text='Password: ')  # ^
	nameL.grid(row=1, sticky=W)
	pwordL.grid(row=2, sticky=W)

	nameEL = Entry(root_login)  # The entry input
	pwordEL = Entry(root_login, show='*')
	nameEL.grid(row=1, column=1)
	pwordEL.grid(row=2, column=1)

	loginB = Button(root_login, text='Login', command=lambda: login_seq(nameEL.get(), pwordEL.get()))
	  # This makes the login button, which will go to the CheckLogin def.
	loginB.grid(columnspan=2, sticky=W)

	root_login.mainloop()


#-------------------signup function-----------------------------------------------
def signup_seq(username, password, key):
	auth_module.login(username, password, key)
	root_signup.destroy()
	root_start.destroy()

def signup():
	global root_signup

	root_signup = Tk()
	root_signup.geometry('250x100+500+500')
	root_signup.title('SignUp')

	nameL = Label(root_signup, text='Username: ')
	pwordL = Label(root_signup, text='Password: ')
	keyL = Label(root_signup, text='Key: ')

	nameL.grid(row=1, sticky=W)
	pwordL.grid(row=2, sticky=W)
	keyL.grid(row=3, sticky=W)

	nameEL = Entry(root_signup)
	pwordEL = Entry(root_signup, show='*')
	keyEL = Entry(root_signup, show='*')

	nameEL.grid(row=1, column=1)
	pwordEL.grid(row=2, column=1)
	keyEL.grid(row=3, column=1)

	loginB = Button(root_signup, text='Signup', command=lambda: singup_seq(nameEL.get(), pwordEL.get(), keyEL.get()))
	loginB.grid(columnspan=2, sticky=W)



	root_signup.mainloop()

#------------------------------------main loop for software--------------------------------------------------

start()


root = tk.Tk()
root.title('HyperPass')
root.geometry('800x700+450+200')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#-----------------------------------------------------------------------------------------------------------
wallpaper = tk.PhotoImage(file='orange.gif')
wallpaper_label = tk.Label(root, image=wallpaper)
wallpaper_label.place(relwidth=1, relheight=1)

#-----------------------------------------------------------------------------------------------------------

facebook_logo = tk.PhotoImage(file='facebook_logo.png')
facebook_logo_label = tk.Label(root, image=facebook_logo)
facebook_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.1, rely=0.3)


twitter_logo = tk.PhotoImage(file='twitter_logo.png')
twitter_logo_label = tk.Label(root, image=twitter_logo)
twitter_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.25, rely=0.3)


google_logo = tk.PhotoImage(file='google logo.png')
google_logo_label = tk.Label(root, image=google_logo)
google_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.4, rely=0.3)


instagram_logo = tk.PhotoImage(file='instagram_logo.png')
instagram_logo_label = tk.Label(root, image=instagram_logo)
instagram_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.55, rely=0.3)


linkedin_logo = tk.PhotoImage(file='linkedin_logo.png')
linkedin_logo_label = tk.Label(root, image=linkedin_logo)
linkedin_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.7, rely=0.3)


skype_logo = tk.PhotoImage(file='skype_logo.png')
skype_logo_label = tk.Label(root, image=skype_logo)
skype_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.85, rely=0.3)

evernote_logo = tk.PhotoImage(file='evernote_logo.png')
evernote_logo_label = tk.Label(root, image=evernote_logo)
evernote_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.25, rely=0.45)

pinterest_logo = tk.PhotoImage(file='pinterest_logo.png')
pinterest_logo_label = tk.Label(root, image=pinterest_logo)
pinterest_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.1, rely=0.45)

evernote_logo = tk.PhotoImage(file='evernote_logo.png')
evernote_logo_label = tk.Label(root, image=evernote_logo)
evernote_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.25, rely=0.45)


reddit_logo = tk.PhotoImage(file='reddit.png')
reddit_logo_label = tk.Label(root, image=reddit_logo)
reddit_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.4, rely=0.45)


amazon_logo = tk.PhotoImage(file='amazon_logo.png')
amazon_logo_label = tk.Label(root, image=amazon_logo)
amazon_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.55, rely=0.45)

github_logo = tk.PhotoImage(file='github_logo.png')
github_logo_label = tk.Label(root, image=github_logo)
github_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.70, rely=0.45)


spotify_logo = tk.PhotoImage(file='spotify_logo.png')
spotify_logo_label = tk.Label(root, image=spotify_logo)
spotify_logo_label.place(relwidth=0.079, relheight=0.09, relx=0.85, rely=0.45)

#---------------------------------------------------------------------------------------------------------------
#"command=lambdatest_function(entry.get()))

facebook_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('Facebook'))
facebook_button.place(relwidth=0.05, relheight=0.05, relx=0.115, rely=0.25)

twitter_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('Twitter'))
twitter_button.place(relwidth=0.05, relheight=0.05, relx=0.265, rely=0.25)

google_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('Google'))
google_button.place(relwidth=0.05, relheight=0.05, relx=0.415, rely=0.25)

instagram_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('Instagram'))
instagram_button.place(relwidth=0.05, relheight=0.05, relx=0.565, rely=0.25)

linkedin_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('LinkedIn'))
linkedin_button.place(relwidth=0.05, relheight=0.05, relx=0.715, rely=0.25)

skype_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('Skype'))
skype_button.place(relwidth=0.05, relheight=0.05, relx=0.865, rely=0.25)

pinterest_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('Pinterest'))
pinterest_button.place(relwidth=0.05, relheight=0.05, relx=0.115, rely=0.55)

evernote_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('EverNote'))
evernote_button.place(relwidth=0.05, relheight=0.05, relx=0.265, rely=0.55)

reddit_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('Reddit'))
reddit_button.place(relwidth=0.05, relheight=0.05, relx=0.415, rely=0.55)

amazon_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('Amazon'))
amazon_button.place(relwidth=0.05, relheight=0.05, relx=0.565, rely=0.55)

github_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('GitHub'))
github_button.place(relwidth=0.05, relheight=0.05, relx=0.715, rely=0.55)

spotify_button = tk.Button(root, text="enter", font=40, bg="black", fg="white", command=lambda: add_sites('Spotify'))
spotify_button.place(relwidth=0.05, relheight=0.05, relx=0.865, rely=0.55)

#----------------------------------------log in button to all user accounts------------------------

log_in_button_to_all_user_accounts = tk.Button(root, text="Launch The Rocket", font=40, bg="grey9", fg="white", command=login_all)
log_in_button_to_all_user_accounts.place(relwidth=0.4, relheight=0.075, relx=0.3, rely=0.7)

#---------------------------------------adding frames----------------------------------------------

hello_frame = tk.Frame(root, bg="grey9", bd=5)
hello_frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor='n')

hello_label = tk.Label(hello_frame, text ="Welcome to HyperPass program", bg='grey9', fg='white', font=9)
hello_label.place(relwidth=0.90, relheight=0.8, relx=0.5, rely=0.1, anchor='n')

'''

frame = tk.Frame(root, bg="RoyalBlue2", bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)
'''

#lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
#lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#label = tk.Label(lower_frame)
#label.place(relwidth=1, relheight=1)

root.mainloop()

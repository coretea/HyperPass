import pyrebase
import getpass

firebaseConfig = {
    "apiKey": "AIzaSyB21L34BC_MdJtEHq5_x_ftiO0PXs9IRAk",
    "authDomain": "hyperpass-ea397.firebaseapp.com",
    "databaseURL": "https://hyperpass-ea397.firebaseio.com",
    "projectId": "hyperpass-ea397",
    "storageBucket": "hyperpass-ea397.appspot.com",
    "messagingSenderId": "798565146323",
    "appId": "1:798565146323:web:41d334998cd5d6edc13e26",
    "measurementId": "G-GTH0YPQEK4"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def register():
    email = input('Please enter your Email: ')
    password = input('Please enter you Password: ')
    user = auth.create_user_with_email_and_password(email, password)
    auth.get_account_info(user['idToken'])
    print("Success!")


def login():
    email = input('Please enter your Email address: ')
    password = input('Please enter your password: ')
    auth.sign_in_with_email_and_password(email, password)
    print("Success!")

def get_id():
    return auth.current_user['idToken']


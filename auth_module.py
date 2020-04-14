import pyrebase
import getpass
import hashlib
import subprocess
import win32com.shell.shell as shell
import win32com.client




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
database = firebase.database()

def register(email, password):
    user = auth.create_user_with_email_and_password(email, password)
    auth.get_account_info(user['idToken'])
    print("Successfully created user!")


def login(email, password):
    auth.sign_in_with_email_and_password(email, password)
    print("Successfully logged in!")

def create_hash():
    h = hashlib.new('ripemd160')
    h.update(get_id())
    return h.hexdigest()


def open_bitlock(password):
    shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters='/c ' +
                    '$key = ConvertTo-SecureString "'+password+'" -AsPlainText -Force\n'
                    'Unlock-BitLocker -MountPoint "S:" -Password $key')



def get_id():
    return auth.current_user['idToken']

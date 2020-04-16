import pyrebase
import getpass
import hashlib
import subprocess
import win32com.shell.shell as shell
import win32com.client
import login_modules
import time

firebaseConfig = {
    "apiKey": "AIzaSyB21L34BC_MdJtEHq5_x_ftiO0PXs9IRAk",
    "authDomain": "hyperpass-ea397.firebaseapp.com",
    "databaseURL": "https://hyperpass-ea397.firebaseio.com",
    "projectId": "hyperpass-ea397",
    "storageBucket": "hyperpass-ea397.appspot.com",
    "messagingSenderId": "798565146323",
    "appId": "1:798565146323:web:41d334998cd5d6edc13e26",
    "measurementId": "G-GTH0YPQEK4",
    "serviceAccount": "hyperpass-ea397-firebase-adminsdk-k8sfv-929286163d.json"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()

def register(email, password, key):
    user = auth.create_user_with_email_and_password(email, password)
    info = auth.get_account_info(user['idToken'])
    print(info)
    # data to save
    data = {'key':key, 'email':email}

# Pass the user's idToken to the push method
    results = database.child(user['localId']).set(data, user['idToken'])
    #attach_key(key)
    open_bitlock(key)
    print("Successfully created user! - No need to log in!")
    time.sleep(3)
    login_modules.lock_db(bytearray(user['localId'], 'utf-8'))
    login_modules.unlock_db(bytearray(user['localId'], 'utf-8'))
    print("db unlocked")
    return True


def login(email, password):
    user = auth.sign_in_with_email_and_password(email, password)
    uid = user['localId']
    uid_val = database.child(uid).get().val()
    print(uid_val)
    open_bitlock(uid_val['key'])
    print("Successfully logged in!")
    time.sleep(3)
    login_modules.unlock_db(bytearray(user['localId'], 'utf-8'))
    print("db unlocked")
    return True


def open_bitlock(password):
    shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters='/c ' +
                    '$key = ConvertTo-SecureString "'+password+'" -AsPlainText -Force\n'
                    'Unlock-BitLocker -MountPoint "F:" -Password $key')

def attach_key(key):
    data = {get_id(): key}
    firebase.database().child(get_id).push(data)

def get_id():
    return auth.current_user['localId']

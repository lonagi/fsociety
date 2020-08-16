#pip install mysql-connector-python pynvg cryptography

import mysql.connector
import hashlib, base64
import sys, os
from getpass import getpass
from pynvg import hash as h
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

PWD = "GENERAL_PAS"

print("------------------")
print("Fuck Passwords")
pwd=getpass(prompt="Password= ")
print("------------------")

if(hashlib.sha256(pwd.encode('utf-8')).hexdigest()!=PWD):
    sys.exit(1)

mydb = mysql.connector.connect(
  host="localhost",
  user="DBUSER",
  passwd="DBPAS",
  database="DB"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb")
myresult = mycursor.fetchall()
mycursor.execute("SELECT * FROM tb2")
myresult2 = mycursor.fetchall()

def getFernel(pwd):
    backend = default_backend()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'1',
        iterations=100000,
        backend=backend
    )
    key = base64.urlsafe_b64encode(kdf.derive(pwd.encode()))
    return Fernet(key)

c1=input("E/D/K")
if(c1 in ('e','E')):
    m=input("Message= ")
    print("")
    pub=h.RSA.importKey(myresult[0][1].replace("\\n","\n").encode())

    m=h.encrypt_message(m,pub)

    print("\n"+str(getFernel(pwd).encrypt(m)))

elif(c1 in ('d','D')):
    m=input("Message= ").encode()
    print("")

    priv=getFernel(pwd).decrypt(myresult2[0][1].encode())
    priv=h.RSA.importKey(priv)

    m=getFernel(pwd).decrypt(m)

    print("\n" + h.decrypt_message(m, priv))

elif(c1 in ('k','K')):
    m=input("site= ")
    mycursor.execute("SELECT * FROM `tb` WHERE `noteb` LIKE '"+m+"'")
    m=mycursor.fetchall()[0][1].encode()
    print("")

    priv=getFernel(pwd).decrypt(myresult2[0][1].encode())
    priv=h.RSA.importKey(priv)

    m=getFernel(pwd).decrypt(m)

    print("\n" + h.decrypt_message(m, priv))

mydb.close()
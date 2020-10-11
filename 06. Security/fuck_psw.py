#pip install mysql-connector-python pynvg cryptography
#pyinstaller fuck_psw.py -F -w

import mysql.connector
import hashlib, base64
import sys, os, subprocess
from getpass import getpass
from pynvg import hash as h
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

with open("/etc/fuck_psw/fuck_psw.txt","r") as f:
    content = f.readlines()
content = [x.strip() for x in content]

PWD = content[0]            #GENERAL_PAS
DBUSER = content[1]         #DBUSER
DBPAS = content[2]          #DBPASSWORD
DB = content[3]             #DB
TB = content[4]             #TABLE
TB2 = content[5]            #TABLE2

print("------------------")
print("Fuck Passwords")

# (out, err) = subprocess.Popen(['last | grep "still logged in" | grep "' + os.ttyname(sys.stdout.fileno()).replace('/dev/','') + '"'], stdout=subprocess.PIPE, shell=True).communicate()
# RemoteIP=out.split()[2].replace(":0.0","")

while True:
    pwd=getpass(prompt="Password= ")
    if(hashlib.sha256(pwd.encode('utf-8')).hexdigest()==PWD):
        break
    else:
        print("\nTry Again\n")

print("------------------")


mydb = mysql.connector.connect(
  host="localhost",
  user=DBUSER,
  passwd=DBPAS,
  database=DB
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM "+TB)
myresult = mycursor.fetchall()
mycursor.execute("SELECT * FROM "+TB2)
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

c1=input("E/D/K").lower()
if(c1=='e'):
    m=input("Message= ")
    print("")
    pub=h.RSA.importKey(myresult[0][1].replace("\\n","\n").encode())

    m=h.encrypt_message(m,pub)

    print("\n"+str(getFernel(pwd).encrypt(m)))

elif(c1=='d'):
    m=input("Message= ").encode()
    print("")

    priv=getFernel(pwd).decrypt(myresult2[0][1].encode())
    priv=h.RSA.importKey(priv)

    m=getFernel(pwd).decrypt(m)

    print("\n" + h.decrypt_message(m, priv))

else:
    i=0
    while i<10:
        i+=1
        m=input("what= ")
        try:
            if(m or m==" " or m=="exit"):
                mycursor.execute("SELECT * FROM `"+TB+"` WHERE `noteb` LIKE '%"+m+"%'")
                fff=mycursor.fetchall()
                m=fff[0][1].encode()
                note=fff[0][3]
                print("\n")

                priv=getFernel(pwd).decrypt(myresult2[0][1].encode())
                priv=h.RSA.importKey(priv)

                m=getFernel(pwd).decrypt(m)

                print("\n" + h.decrypt_message(m, priv))
                print(f'\n Note: {note}')
                break
            else:
                break
        except:
            pass

mydb.close()
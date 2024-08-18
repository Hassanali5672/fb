ook.com/method/user.register'
    
    headers = {'User-Agent': ua()}
    response = requests.post(api_url, data=req, headers=headers)
    reg = response.json()
    id = reg.get('new_user_id')
    token = reg.get('session_info', {}).get('access_token')
    
    
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

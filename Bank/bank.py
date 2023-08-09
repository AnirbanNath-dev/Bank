import json

FILE_PATH = 'saved_data.json'

def load_data():
    try:
        with open(FILE_PATH , 'r') as f:
            read_data = json.load(f)
            return read_data
    except:
        return {}

def append_data(arg):
    with open(FILE_PATH , 'w') as f:
        data = json.dump(arg , f, indent=4)
        return data


class Bank:
    def __init__(self , name):
        self.name = name
        self.amount = 0
        self.password = ''
        self.read_data = load_data()
    


    def _login(self):
        login_password = input('Enter your passwrod: ')
        
        if (self.name in self.read_data) and self.read_data[self.name]['password'] == login_password:
            print('You have successfully logged in !')


        else:
            print('No account found!')
            self._register()


    def _register(self):
        if self.name in self.read_data:
            print('Username already existed!')
            while True:
                changed_username = input('Change your username: ')
                if changed_username.strip() == '':
                    print('Please enter a valid username')

                else:
                    break
            self.name = changed_username

        
        create_password = input('\nCreate a password : ')
        self.read_data[self.name] = {
            "password": create_password,
            "amount": 0
        }

        append_data(self.read_data)
        print('Your account has been successfully created! ')

    
    def deposit(self):
        try:
            amount = int(input('\nEnter the amount: '))
            self.read_data[self.name]["amount"] += amount
            append_data(self.read_data)     
            print(f'You have deposited the money\nYour balance : ${self.read_data[self.name]["amount"]}')
        except:
            print('Invalid amount. Please try again')

    def withdraw(self):
        try:
            amount = int(input('\nEnter the amount: '))
            balance = self.read_data[self.name]["amount"] 

            if balance >= amount:

                balance -= amount
                append_data(self.read_data)
                print(f'You have withdrawn the money\nYour balance : ${balance}')
            else:
                print(f'You dont have enough money\nYour balance : ${balance}')
        except:
            print('Invalid amount. Please try again')
        

    def ask_for_login_or_register(self):
        opt = input('\n\nDo you have any account ? (Y/N): ')
        if opt.upper() == 'Y':
            self._login()

        elif opt.upper() == 'N':
            self._register()
        else:
            print('No account has been found! ')
            self._register()
            

    def default_screen(self):
        welcome = f'\nHello {self.name} , Welcome to XYZ Bank Institution'
        print(welcome)
        print('*'*len(welcome))
        self.ask_for_login_or_register()
        wtdr_or_dp = input('\nDo you want to deposit or withdraw? (D/W):')

        if wtdr_or_dp.upper() == 'D':
            self.deposit()
        elif wtdr_or_dp.upper() == 'W':
            self.withdraw()



def main():
    while True:
        name = input('\nEnter your name: ')

        if name.strip()=='':
            print('Please enter a valid name')
            continue
        else:
            break

    applicant = Bank(name)
    applicant.default_screen()



if __name__ == '__main__':
    main()
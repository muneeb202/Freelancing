
def input_number(message: str, lower:float =None, upper:float =None, errormsg:str = '') -> int:
    """_summary_

    Args:
        message (str): input message
        lower (float, optional): lower limit of input number. Defaults to None.
        upper (float, optional): upper limit of input number. Defaults to None.
        errormsg (str, optional): error message. Defaults to ''.

    Returns:
        int: the valid number
    """
    while True:
        try:
            num = int(input(message))
            if lower != None and num < lower:
                print(errormsg)
                continue

            if upper != None and num > upper:
                print(errormsg)
                continue
            
            return num
        except ValueError:
            print('Please enter a number!')
        
def input_string(message: str):
    """input string from console until string is non empty

    Args:
        message (str): input message

    Returns:
        str: non empty string
    """
    while True:
        string = input(message).strip()
        if string != '':
            return string
        print('\nInput cannot be empty! Try again!\n')



class Wallet:

    def __init__(self, Id, balance, wtype):
        """constructor for the class

        Args:
            Id (int): wallet id
            balance (int): initial balance
            wtype (str): type of wallet
        """
        self.id = Id
        self.balance = balance
        self.last_trans = 'None'
        self.type = wtype


    def withdraw(self, amount):
        """withdraw amount from wallet

        Args:
            amount (int): amount to be withdrawn

        Returns:
            bool: success/failure of withdrawal
        """
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
            self.last_trans = 'Withdraw'
            return True


    def deposit(self, amount):
        """deposit amount to wallet

        Args:
            amount (int): amount to be deposited
        """
        self.balance += amount
        self.last_trans = 'Deposit'
    

    def transfer_wallet(self, amount, wallet):
        """transfer amount to another wallet

        Args:
            amount (int): amount to be transferred
            wallet (Wallet): wallet to be transferred to

        Returns:
            bool: success/failure of transferrence
        """
        if not self.withdraw(amount):
            return False
        else:
            wallet.balance += (amount * 0.995)
            self.last_trans = 'Transference'
            return True


    def transfer_customer(self, amount, other):
        """transfer amount to the wallet of another customer

        Args:
            amount (int): amount to be transferred
            other (Wallet): other customer's wallet

        Returns:
            bool: success/failure of transferrence
        """
        if not self.withdraw(amount):
            return False
        
        other.balance += (amount * 0.985)
        self.last_trans = 'Transference'
        return True

    def display(self):
        """print information of the wallet
        """
        print(f'{self.id:<14} {round(self.balance, 2):<11} {self.last_trans:<19} {self.type}')
    


class Daily(Wallet):
    def __init__(self, Id, balance):
        """constructor for the class, calls parent's constructor

        Args:
            Id (int): wallet id
            balance (int): initial balance
        """
        Wallet.__init__(self, Id, balance, 'Daily Use')



class Saving(Wallet):
    def __init__(self, Id, balance):
        """constructor for the class, calls parent's constructor

        Args:
            Id (int): wallet id
            balance (int): initial balance
        """
        Wallet.__init__(self, Id, balance, 'Saving')

    def transfer_wallet(self, amount, wallet):
        """use polymorphism to override function in parent class, as transfer privelleges to be denied

        Args:
            amount (int): amount to be transferred
            wallet (Wallet): wallet to be transferred to

        Returns:
            bool: success/failure of transference
        """
        print('\nNo transfer privileges!')
        return False

    def transfer_customer(self, amount, other):
        """use polymorphism to override function in parent class, as transfer privelleges to be denied

        Args:
            amount (int): amount to be transferred
            other (Wallet): wallet to be transferred to

        Returns:
            bool: success/failure of transference
        """
        print('No transfer privileges!')
        return False


class Holiday(Wallet):
    def __init__(self, Id, balance):
        """constructor for the class, calls parent's constructor

        Args:
            Id (int): wallet id
            balance (int): initial balance
        """
        Wallet.__init__(self, Id, balance, 'Holidays')

    def transfer_customer(self, amount, other):
        """use polymorphism to override function in parent class, as transfer privelleges to be denied

        Args:
            amount (int): amount to be transferred
            other (Wallet): wallet to be transferred to

        Returns:
            bool: success/failure of transference
        """
        print('No transfer privileges!')
        return False


class Mortgage(Wallet):
    def __init__(self, Id, balance):
        """constructor for the class, calls parent's constructor

        Args:
            Id (int): wallet id
            balance (int): initial balance
        """
        Wallet.__init__(self, Id, balance, 'Mortgage')

    def withdraw(self, amount):
        """use polymorphism to override function in parent class, as transfer privelleges to be denied

        Args:
            amount (int): amount to be withdrawn

        Returns:
            bool: success/failure of withdrawal
        """
        print('No withdrawal privileges!')
        return False

    def transfer_wallet(self, amount, wallet):
        """use polymorphism to override function in parent class, as transfer privelleges to be denied

        Args:
            amount (int): amount to be transferred
            wallet (Wallet): wallet to be transferred to

        Returns:
            bool: success/failure of transference
        """
        print('No transfer privileges!')
        return False

    def transfer_customer(self, amount, other):
        """use polymorphism to override function in parent class, as transfer privelleges to be denied

        Args:
            amount (int): amount to be transferred
            other (Wallet): wallet to be transferred to

        Returns:
            bool: success/failure of transference
        """
        print('No transfer privileges!')
        return False


class Customer:
    
    def __init__(self, first, last, country, age, email, password, username):
        """initialise all variables and attributes

        Args:
            first (str): first name
            last (str): last name
            country (str): country of residence
            age (int): Age
            email (str): email
            password (str): account password
            username (str): account username
        """
        self.first_name = first
        self.last_name = last
        self.residence = country
        self.age = age
        self.email = email
        self.password = password
        self.username = username
        self.wallets = {}


    def create(self):
        """create a new wallet for the customer
        """
        while True:
            w_id = input_number('\nEnter wallet id:  ', 1, None, 'Wallet Id must be positive\n')
            if w_id not in self.wallets:
                break
            print('Wallet Id already exists! try again')
        
        balance = input_number('Enter balance:    ', 0, None, 'Balance cannot be negative\n')
        wtype = input_number('Enter Wallet Type (1/Daily, 2/Saving, 3/Holidays, 4/Mortgage): ', 1, 4, 'Incorrect option!\n')
        
        if wtype == 1:
            self.wallets[w_id] = Daily(w_id, balance)
        elif wtype == 2:
            self.wallets[w_id] = Saving(w_id, balance)
        elif wtype == 3:
            self.wallets[w_id] = Holiday(w_id, balance)
        elif wtype == 4:
            self.wallets[w_id] = Mortgage(w_id, balance)

        print('\nSuccessfully created wallet!')

        
    def delete(self):
        """delete a particular wallet of the customer
        """
        w_id = input_number('Enter wallet id: ')
        if w_id not in self.wallets:
            print('Wallet Id does not exist!')
            return
        
        opt = input_string('Are you sure you want to delete Wallet! Y/N : ').lower()
        if opt != 'y':
            return

        del self.wallets[w_id]
        print('Successfully deleted wallet')
            
        

    def deposit(self):
        """deposit amount to a particular wallet
        """
        w_id = input_number('Enter wallet id: ')
        if w_id not in self.wallets:
            print('Wallet Id does not exist!')
            return

        amount = input_number('Enter amount to deposit: ', 1, None, 'Amount must be positive!')
        self.wallets[w_id].deposit(amount)
        print('\nSuccessfully deposited amount!')


    def withdraw(self):
        """withdraw amount from a particular wallet
        """
        w_id = input_number('Enter wallet id: ')
        if w_id not in self.wallets:
            print('Wallet Id does not exist!')
            return

        amount = input_number('Enter amount to withdraw: ', 1, None, 'Amount must be positive!')
        if self.wallets[w_id].withdraw(amount):
            print('\nSuccessfully withdrawn amount!')
        else:
            print('Could not withdraw amount!')


    def transfer_wallet(self):
        """transfer amount to another wallet

        Returns:
            float: fees generated in transfering amount
        """
        w_id = input_number('\nEnter sending wallet id:     ')
        if w_id not in self.wallets:
            print('Wallet Id does not exist!')
            return 0

        w_id2 = input_number('Enter recieving wallet id:   ')
        if w_id2 not in self.wallets:
            print('Wallet Id does not exist!')
            return 0

        amount = input_number('Enter amount to transfer:    ', 1, None, 'Amount must be positive!')
        fees = amount * 0.005
        
        if self.wallets[w_id].transfer_wallet(amount, self.wallets[w_id2]):
            print(f'\nSuccessfully transferred amount! Transaction fee : {round(fees, 2)}')
            return fees
        else:
            print('Could not transfer amount!')
            return 0


    def transfer_customer(self, others):
        """transfer amount from a wallet to another customer's wallet

        Args:
            others (list): list of other customers

        Returns:
            float: fees generated in transfering amount to another customer
        """
        w_id = input_number('\nEnter sending wallet id: ')
        if w_id not in self.wallets:
            print('Wallet Id does not exist!')
            return 0

        username = input_string('Enter recieving Customer\'s Username: ').lower()

        if username in others:
            receiver = others[username]

            w_id2 = input_number('Enter recieving wallet id: ')
            if w_id2 not in receiver.wallets:
                print('Wallet Id does not exist!')
                return 0

            amount = input_number('Enter amount to transfer: ', 1, None, 'Amount must be positive!')
            fees = amount * 0.015

            if self.wallets[w_id].transfer_customer(amount, receiver.wallets[w_id2]):
                print(f'\nSuccessfully transferred amount! Transaction fee : {round(fees, 2)}')
                return fees
            else:
                print('Could not transfer amount!')
                return 0
        
        print('No such Customer exists!')
        return 0

    
    def print_wallets(self):
        """prints the description of each and every wallet of the customer
        """
        print('\nWallet ID      Balance     Last Transaction    Wallet Type\n' + ('-' * 58))
        for wallet in self.wallets:
            self.wallets[wallet].display()


    def run(self, others):
        """runs the main loop for a particular customer

        Args:
            others (list): all customers, used to transferring to other customers

        Returns:
            float: amount of fees generated in accessing the customer account
        """
        fees = 0
        while True:
            print('\n---------- Menu ----------\n1: Create Wallet\n2: Delete Wallet\n3: Deposit Money\n4: Withdraw Money\n5: Transfer to another Wallet\n6: Transfer to another Customer\n7: Print Wallet details\n8: Logout')
            opt = input_number("\nInput Option: ", 1, 8, 'Incorrect Option!')

            if opt == 1:
                self.create()

            elif opt == 2:
                self.delete()

            elif opt == 3:
                self.deposit()

            elif opt == 4:
                self.withdraw()

            elif opt == 5:
                fees += self.transfer_wallet()

            elif opt == 6:
                fees += self.transfer_customer(others)

            elif opt == 7:
                self.print_wallets()

            else:
                print('\nLogging Out!!!')
                break

        return fees

   
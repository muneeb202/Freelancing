
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


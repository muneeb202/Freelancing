
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


import os

def read_file():
    file = open("pokemon.txt")

    pokemon_index = []

    for i in range(151):
        pokemon = []
        pokemon.append(file.readline().strip())
        pokemon.append(file.readline().strip().split('\t'))
        attacks = []
        for j in range(4):
            attacks.append(file.readline().strip())
        pokemon.append(attacks)
        sprite = ''
        for line in file:
            if line.strip() == '':
                break
            sprite += line
        pokemon.append(sprite)
        pokemon_index.append(pokemon)

    return pokemon_index

def display(pokemons, index):
    os.system('cls')
    print('\t' * 5 + '-' * 40)
    print('\t' * 6 + 'P O K E M O N    W I K I')
    print('\t' * 5 + '-' * 40 + '\n\n')
    num = '000'
    pokemon = pokemons[index]
    display_index = str(index + 1)
    
    print('#' + num[0:3 - len(display_index)] + display_index + ' ' + pokemon[0] + ' (' + pokemon[1][0], end='')
    for i in range(1, len(pokemon[1])):
        print(' | ' + pokemon[1][i], end='')
    print(')\n')
    print(pokemon[3])
    header = ['Attack', 'Type', 'Power', 'PP', 'Category']
    print(f'\n\n{header[0]:20} {header[1]:20} {header[2]:20} {header[3]:20} {header[4]:20}')
    print('-' * 92)
    for attack in pokemon[2]:
        if attack == '':
            break
        tokens = attack.split('\t')
        print(f'{tokens[0]:20} {tokens[1]:20} {tokens[2]:20} {tokens[3]:20} {tokens[4]:20}')


def main():

    pokemons = read_file()
    print('\n' * 5 + '\t' * 5 + '-' * 40)
    print('\t' * 6 + 'P O K E M O N    W I K I')
    print('\t' * 5 + '-' * 40)
    input('\n' + '\t' * 6 + 'Press enter to continue!')
    index = 0
    opt = 'n'

    while opt != 'q':
        if opt != 'w':
            display(pokemons, index)

        print('\n\n1 - 151: go to list index    p: previous pokemon     n: next pokemon     q: quit program\n')
        opt = input('Enter option: ')
        opt = opt.strip().lower()

        temp = index

        if opt == 'p':
            temp -= 1
        elif opt == 'n':
            temp += 1
        elif opt == 'q':
            break
        else:
            try:
                temp = int(opt) - 1
            except ValueError:
                temp = -1
        
        if temp < 0 or temp > 150:
            print('\nIncorrect Option! Enter Again\n')
            opt = 'w'
        else:
            index = temp

    print('\n\n\t\t\tLeaving Pokemon Wiki!!!')

        


if __name__ == "__main__":
    main()
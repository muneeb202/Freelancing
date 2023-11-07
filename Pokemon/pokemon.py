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
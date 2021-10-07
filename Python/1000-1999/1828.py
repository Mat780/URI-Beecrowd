# -*- coding: utf-8 -*-

def main():
    n = int(input())
    caso = 1

    # Sheldon Vence: Bazinga!
    # Raj vence: Raj trapaceou!
    # Empate: De novo!

    for c in range(0, n):
        Sheldon, Raj = input().split()

        l1 = [Sheldon, Raj]

        if 'tesoura' in l1 and 'papel' in l1:

            if Sheldon == 'tesoura':
                print('Caso #%i: Bazinga!' %(caso))

            else:
                print('Caso #%i: Raj trapaceou!' %(caso))
        
        elif 'papel' in l1 and 'pedra' in l1:

            if Sheldon == 'papel':
                print('Caso #%i: Bazinga!' %(caso))
            else:
                print('Caso #%i: Raj trapaceou!' %(caso))
        
        elif 'pedra' in l1 and 'lagarto' in l1:

            if Sheldon == 'pedra':
                print('Caso #%i: Bazinga!' %(caso))
            else:
                print('Caso #%i: Raj trapaceou!' %(caso))

        elif 'lagarto' in l1 and 'Spock' in l1:

            if Sheldon == 'lagarto':
                print('Caso #%i: Bazinga!' %(caso))
            else:
                print('Caso #%i: Raj trapaceou!' %(caso))

        elif 'Spock' in l1 and 'tesoura' in l1:

            if Sheldon == 'Spock':
                print('Caso #%i: Bazinga!' %(caso))
            else:
                print('Caso #%i: Raj trapaceou!' %(caso))

        elif 'tesoura' in l1 and 'lagarto' in l1:

            if Sheldon == 'tesoura':
                print('Caso #%i: Bazinga!' %(caso))
            else:
                print('Caso #%i: Raj trapaceou!' %(caso))

        elif 'lagarto' in l1 and 'papel' in l1:

            if Sheldon == 'lagarto':
                print('Caso #%i: Bazinga!' %(caso))
            else:
                print('Caso #%i: Raj trapaceou!' %(caso))

        elif 'papel' in l1 and 'Spock' in l1:

            if Sheldon == 'papel':
                print('Caso #%i: Bazinga!' %(caso))
            else:
                print('Caso #%i: Raj trapaceou!' %(caso))

        elif 'Spock' in l1 and 'pedra' in l1:

            if Sheldon == 'Spock':
                print('Caso #%i: Bazinga!' %(caso))
            else:
                print('Caso #%i: Raj trapaceou!' %(caso))
        
        elif 'pedra' in l1 and 'tesoura' in l1:

            if Sheldon == 'pedra':
                print('Caso #%i: Bazinga!' %(caso))
            else:
                print('Caso #%i: Raj trapaceou!' %(caso))
        
        elif l1[0] == l1[1]:

            print('Caso #%i: De novo!' %(caso))
        
        caso += 1
        
main()
nb_bateaux = int(input("Quelle est votre nombre de bateaux ? "))

def input_joueur():
    coord_bateaux = [0] * nb_bateaux
    for i in range(nb_bateaux): 
        coord_bateaux[i] = input(f"Quelle est votre coordonnée n°{i} ? ")
    return(coord_bateaux)

print("Le joueur 1 doit poser ses bateaux")
current_player = input_joueur()
print(current_player)

print("Le joueur 2 doit poser ses bateaux")
next_player = input_joueur()
print(next_player)

def tir():
    coord_tir = input("Sur quelle coordonnée voulez-vous tirer ? ")
    return coord_tir


nombre_tour = 100
#METTRE UNE BOUCLE WHILE

a=1
b=2

while current_player != [0] * nb_bateaux or next_player != [0] * nb_bateaux: 
    # TOUR DU JOUEUR 
    print(f"Le joueur {a} doit jouer")
    position_tir = tir()
    if position_tir in next_player :
        index = next_player.index(position_tir)
        next_player[index] = 0

        print('TOUCHE')

        if next_player == [0] * nb_bateaux:
            print(f'LE JOUEUR {a} A GAGNE !')
            break
    else :
        print('PERDU')
    a, b = b, a
    current_player, next_player = next_player, current_player

        

# 1792816 Anthony Flores 11.27

def printroster():
    ky = list(players.keys())
    ky.sort()
    print('ROSTER')
    for soccer in ky:
        print('Jersey number: %d, Rating: %d' % (soccer, players[soccer]))


players = {}
for i in range(0, 5):
    jersey = int(input("Enter player %d's jersey number:\n" % (i + 1)))

    players[jersey] = int(input("Enter player %d's rating:\n" % (i + 1)))
    print()

printroster()
print()

while True:
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
    option = input('Choose an option:')
    print()

    if option == 'q':
        break
    if option == 'o':
        printroster()
        print()
        
    elif option == 'a':
        jersey = int(input('Enter new player\'s jersey number:\n'))
        rating = int(input('Enter the player\'s rating:\n'))
        players[jersey] = rating
        print()
        
    elif option == 'd':
        jersey = int(input('Enter a player\'s jersey number:\n'))
        print()

    if jersey in list(players.keys()):
        del players[jersey]
        print()

    elif option == 'u':
        jersey = int(input('Enter a player\'s jersey number:\n'))
        rating = int(input('Enter a new rating for players:'))
        players[jersey] = rating
        print()

    elif option == 'r':
        rating = int(input('Enter a rating:\n'))
        keys = list(players.keys())
        keys.sort()
        print('\nAbove %d' % rating)
        print()

        count = 0
        for key in keys:
            if players[key] > rating:
                print('jersey number: %d, Rating: %d' % (key, players[key]))
                count += 1
        if count == 0:
            print('No players found above %d rating' % rating)

import random


#with open('sweaCasino.txt', 'w') as c:
#    pass





casino = 500
print('''
Välkommen till Sverige-Casino!
Du får 500 kronor att spela för.
OBS! 18 årsgräns.
''')




while True:
    try:
        age = int(input('Hur gammal är du? '))
        break
    except ValueError:
        print('Bara siffror!')
if age < 18:
    print('Du är för ung!')
    quit()



#username = 'SadaFes'
#password = 'Globen123'

while True:

    with open('sweaCasino.txt', 'r+') as filen:
        #print(type(username))

        username = input('Username : ')
        password = input('Password : ')
        inloggad = False
        for rad in filen:

            filuser = rad.split()
            #print(filuser)
            if username == filuser[0] and password == filuser[1]:
                print('Du loggas in****')
                inloggad = True
                break # första loopen (for)
        
        if inloggad is True:
            print("Välkommen")
            break # while loopen
        else:
            print('Fel password')
while True:
    try:
        val = int(input('Tryck på en siffra för att starta spelet\n'))
        break
    except ValueError:
        print('ENDAST SIFFROR')


i = 0
gissa = 0
satsa = 0
casino = 500

#### SPEL LOOP
while True:
    if casino <= 0:
        print('Hoppsan du har inga pengar kvar \nLägg i pengar för att fortsätta :)))')
        break

    
    
    ####################
    # float checker
    while True:
        try:
            satsa = float(input('Hur mycket vill du satsa? '))
            if satsa > casino:
                print('du har inte råd')
            else:
                break
        except ValueError:
            print('Endast siffror')
    ##################

    potten = casino - satsa
    print('Just nu är Potten:', potten)
    slump = random.randrange(11)

    ##################
    # Int checker
    while True:
        try:
            gissa = int(input('Gissa på en siffra mellan 0 - 10: '))
            break
        except ValueError:
            print("ENDAST SIFFROR")
    #######################

    if slump is gissa:
        print(slump, 'är korrekt\n\n')
        casino -= satsa
        satsa *= 3
        casino += satsa
        print(casino, 'kronor :)))')
    else:
        print(gissa, 'är inkorrekt')
        print('Korrekt nummer är', slump, '\n\n')
        casino -= satsa
        print(casino, 'Kronor :(((')
    
    while True:
        try:
            val = int(input('Vill du fortsätta spela, tryck 0 för att avsluta eller annan siffra för att fortsätta'))
            break
        except ValueError:
            print()
    if val == 0:
        break
    
    if casino < 250:
        #########################
        ##INT CHECKER
        while True:
            try:
                val = int(input('Du har förlorat mer än hälften, \
                är du säker på att vill fortsätta?\n tryck 0 för att avsluta eller tryck på valfri siffra för att fortsätta'))
                break
            except ValueError:
                print('ENDAST 0 FÖR ATT AVSLUTA ELLER VALFRI SIFFRA FÖR ATT FOR')
                ############################
        if val == 0:
            break
        else:
            print('Du valde spelet fortsätter')






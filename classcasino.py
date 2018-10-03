import random #här importerar jag in classen random


class User:                 #från rad 4  till rad 7 ritar jag min blueprint med attributer
    name = None
    password = None
    money = None


    
    def __init__(self, name, password, money):    #Här är min konstruktor
        self.name = name
        self.password = password
        self.money = money

        

    def  set_new_money(self, money):  #här skapade jag min sätter om jag senare vill förändra mitt värde i senare tillfälle
        self.money = money

    def get_new_money(self):           #här skapar jag min get, så att jag kan returnera det nya värdet.
        return self.money
        
user1 = User('sada', 'globen', 0)       #user1 är namnet på ett av mina objekt. I user1 finns sada som kommer bli ett av mina två usernames som får möljighet att spela programmet längre fram i programmet.
user2 = User('micke', 'hippo', 0)       #user2 motsvarar det jag skrev precis ovanför. --||--





with open('casinoclass.txt', 'r+') as filen:   #    Öppnar min första texfil som har mode läge r+ som står för read + write. I den här textfilen fokuserar jag på username och password


    filen.write(user1.name + ",")               #   Här skriver jag in till textfilen för user1 som är i det här fallet sada
    filen.write(user1.password + ',\n')         #   password från objektet user1 som är globen
    filen.write(user2.name + ',')               #   user2 name micke
    filen.write(user2.password + ',')           #   user2 password hippo
    filen.close()                               #   stänger textfilen casinoclass.txt


    print('''Välkommen till Sverige-Casino!\nDu får 500 kronor att spela för.\nOBS! 18 årsgräns.  
    ''')                                                                                                #   printar en hälsning '''Välkommen till Sverige-Casino!\nDu får 500 kronor att spela för.\nOBS! 18 årsgräns.'''

    while True:                                                                                         # while loop som endast kräver siffror. Om user läser in annat en siffror då loopar hen tills en siffra läses in.
        try:
            val = int(input('Tryck på en siffra för att starta spelet\n'))
            break
        except ValueError:
            print('ENDAST SIFFROR')

    while True:
        try:
            age = int(input('Hur gammal är du? '))                              # while loop som inte låter dig gå vidare ifall skriver annat än siffror
            print()
            break
        except ValueError:
            print('Bara siffror!')
    if age < 18:                                                                # Är du under < 18 år printas en text till konsolen som säger 'Du är för ung!' och spelet avslutas.
        print('Du är för ung!')
        quit()
    
    


guess = 0                  # guess uppgift är att se till att användaren inte får  gissa mer än 3x.   Min guess variabel startar på värdet 0 och får inte bli större än 2.
while True:

    with open('casinoclass.txt', 'r+') as filen:   # Här öppnar jag min textfil casinoclass.txt på nytt.

        username = input('Username : ')            # Här får users möjlighet att logga in.
        print()
        password = input('Password : ')
        inloggad = False                           # Variabel som heter inloggad har en boolean med False värde

        for rad in filen:                           # for - loop med rad som iteration som läser igenom textfilen

            filuser = rad.split(',')                # Skapade en variabel med namnet filuser och tilldelat den iterationen rad som har till uppgift att läsa igenom raderna jag satt dit en split funktion som söker efter comma tecken för att göra skillnad på username och password
            if username == user1.name and password == user1.password:               # Villkor om username som är input i det här fallet är lika med user1.name och password lika med user1.password loggas användaren in på user1
                print()
                print('You picked User1')                                           # Blir du inloggad kommer det att printas ut att du valt user1 och breakas ur for loopen

                print()
                print('Du loggas nu in *******')
                inloggad = True
                break

            elif username == user2.name and password == user2.password:
                print()
                print('You picked User2')

                print()
                print('Du loggas nu in *******')
                inloggad = True
                break




        
        if inloggad is True:                    #Om inloggad är sann printas Välkommen textfilen stängs() och du breaks ur textfilen
            print()
            print("Välkommen :))))")
            filen.close()
            break  # while loopen

        else:                                   # Annars printas fel username eller password och guess får + 1 och fortsätter loopa tills guess blir större än 2 och avslutar programmet.
            print()
            print('Fel username, eller password ')
            print()
            guess += 1
            if guess > 2:                       # om guess större än 2 stäng av programmet
                quit()
            elif guess > 1:                     # Om guess blir större än 1  printas 'Du har en chans kvar'
                print()
                print('Du har en chans kvar')
                print()



with open('casinoclass.txt', 'r+') as filen:        #   Öppnar textfilen casinoclass.txt mode r+ read + write


        for rad in filen:                           # for loop med rad som iteration går igenom filen casinoclass.txt filen

            filuser = rad.split(',')
            if user1.name == username and user1.password == password:       # Villkor. Om jag loggar in med user1
                setter = user1.set_new_money(500)                           # Här använder jag min setter från min class User. Där jag sätter ett nytt värde för money på 500 kronor
                casino = user1.get_new_money()                              # returnerar värdet till casino variabeln
                filen.close()                                               # stänger text filen    
                break

            elif user2.name == username and user2.password == password:     # Villkor! Om jag loggar in med user2
                setter = user2.set_new_money(500)
                casino = user2.get_new_money()
                filen.close()
                break
            break


#### SPEL LOOP
while True:

    
    if casino <= 0:                                     #   innanför spel loopen, om casino är mindre eller lika med 0 kommer spel loopen att breakas och spelet kommmer att avslutas. 
        print()
        print('Hoppsan du har inga pengar kvar \n\nLägg i pengar för att fortsätta :)))')
        break



    ####################
    # Int checker
    while True:
        try:
            print()
            satsa = int(input('Hur mycket vill du satsa? '))
            if satsa > casino:                                  #   Om du satsar mer än vad du äger printas det att du inte har råd och du får satsa om på nytt.
                print()
                print('Du har tyvärr inte råd')
            else:
                break
        except ValueError:
            print('Endast siffror')
    ##################

    
    potten = casino - satsa                                     #   Potten är lika med casino minus satsa. casino är 500 kr det du går in med spelet med
    print('Just nu är Potten:', potten)                         #   Printas potten
    slump = random.randrange(11)                                #   Här blir random class till användning. Jag importerade random allra högst upp på rad 1. Som du ser så tilldelar jag funktionen random.randrange(11) till variabeln slump. 

    ##################
    # Int checker
    while True:                 #   while loop som endast förstår sig på heltal om användaren skriver annat tecken loopas hen på nytt tills en siffra läses in
        try:
            gissa = int(input('Gissa på en siffra mellan 0 - 10: '))        
            break
        except ValueError:
            print("ENDAST SIFFROR")
    #######################

    if slump is gissa:              #   Om slump är samma som det du gissar. Printas slump variabeln tillsammans med textsträngen , 'är korrekt'
        print(slump, 'är korrekt\n\n')
        casino -= satsa             # Matematiska uträkningar casino det du äger minus det du satsar,
        satsa *= 3                  # Det jag satsar multpliceras med 3
        casino += satsa             # Tar det nya värdet satsa och adderar det med casino som är det jag har kvar på kontot.
        print(casino, 'kronor :)))')
    else:
        print(gissa, 'är inkorrekt')        # Om jag får fel hamnar jag här på rad 188. Och casino förlorar det han satsat.
        print('Korrekt nummer är', slump, '\n\n')
        casino -= satsa
        print('Saldo : ', casino, 'Kronor :(((')

    while True: ### while loop som endast tar emot siffror. Efter varje spel ska användaren få möjlighet att välja om hen vill fortsätta eller inte.
        try:
            val = int(input('Vill du fortsätta spela, tryck 0 för att avsluta eller annan siffra för att fortsätta'))   
            break
        except ValueError:
            print()
    if val == 0:        # Om valet är lika med 0 Öppnas textfilen highscore.txt

        with open('highscore.txt', 'r+') as filen: # Öppnar textfilen highscore med vald mode r+ som står för read + write
            
            for rad in filen:  # Därifrån går programmet vidare till for loopen, rad är min iteration som går igenom textfilen
                filen.read()
                high_score = int(rad)  # Highscore är lika med iterationen rad, i det här fallet rad=0 eftersom noll är strängen som befinner sig högst upp i textfilen. Allt över noll kronor hamnar på Resultat-tavlan
                if casino > high_score: # Casino behöver endast ha ett större värde en noll för att hamna på resultat tavlan
                    filen.write('\n')
                    filen.write(str((casino)))                          # Värdet på casino variabeln skrivs över till texfilen som heter highscore
                    #filen.read() ##
                    print()
                    print('Du loggar ut med', casino, 'Kronor')     # Printar ut nuvarande värdet på casino till till consolen


        break



    if casino < 250:
        #########################
        ##INT CHECKER
        while True:                 #   När användaren hamnar under 250 kr får användaren möjlighet att välja om hen vill fortsätta eller inte.
            try:
                print()
                val = int(input(
                    'OBS!\nDu har förlorat mer än hälften. \n\nÄr du säker på att du vill fortsätta?\n\nOm du inte vill fortsätta tryck 0 eller tryck på en annan valfri siffra för att fortsätta'))            # Endast integers/siffror för val int(input)
                break
            except ValueError:
                print()
                print('ENDAST 0 FÖR ATT AVSLUTA ELLER VALFRI SIFFRA FÖR ATT FOR')
                ############################
        if val == 0:            #   Om valet är lika med 0. Öppnas textfilen highscore.txt
            
            with open('highscore.txt', 'r+') as filen:             #    Öppnar textfilen highscore.txt på nytt
                
                for rad in filen:                                  # Precis som jag gjorde från rad 203--214   
                    filen.read()
                    high_score = int(rad)
                    if casino > high_score:
                        filen.write('\n')
                        filen.write(str(casino))
                        #filen.read() ##
                        print()
                        print('Du loggar ut med', casino, 'Kronor')     # Printar ut nuvarande värdet på casino till consolen


            break                                                       # Avslutar hela spelet




        else:                                                           # Om user väljer att fortsätta spela vidare, loopas spelet igen tills pengarna går slut
            print()
            print('Du valde spelet fortsätter')
















def urna():
    print('''                                                                                          
           ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::           
         .::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.         
        .:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::        
      .::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.      
     .::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.     
    .:::::::::::::::::::::::::::::::::::::::::::::::::::::.........................::.    
    .:::::::::::::::::::::::::::::::::::::::::::::::::::::         .:::::.         ::.    
    .::................................................:::      .:::::::::::       ::.    
    .::................................................::::::::::::::::::::::::::::::.    
    .::................................................:::####%%%%%#%%%%%#%%%%%####::.    
    .::................................................:::####@#%@%#%#%@%#%*%@%####::.    
    .::................................................:::####@%@@%##%@@%#%%@@%####::.    
    .::................................................:::####@#@@%#%%@@%#%%@%%####::.    
    .::.............|=======..0..|=.....=|.............:::####%#@@%#%#@@%###@@%####::.    
    .::.............|.........|..|.=...=.|.............:::####%%%%%#%%%%%#%%%%%####::.    
    .::.............|====.....|..|..=.=..|.............:::####%#%@%##*%@%##*%@%####::.    
    .::.............|.........|..|...=...|.............:::####%%%%%#%%%%%#%%%%%####::.    
    .::.............|.........|..|.......|..............:::##########%%@@%##########::.    
    .::................................................:::##########%#@@%##########::.    
    .::................................................:::#+=====*##*****##******##::.    
    .::................................................:::#:.....=#++++++##++===+##::.    
    .:::::::::::::::::::::::::::::::::::::::::::::::::::::#++++++*##*****##******##::.    
    .::::=:::::::=:::::::-:::::::-::::::--:::::::-::::::--::::::=-::::::=-::::::=-:::.    
         :       :      .:      ..      ..      ..      ..      ..      :.      :.        
''')

def lula(candidatos, vlula):
    print('-Candidato à presidência 2022-\n'.center(45))
    print('Nome: Lula')
    print('Partido: PT')
    print('Número:', (candidatos['Lula']))
    print()

    print('''            -=+=-::.          
           -====----:         
          =+=------..         
         :+===+=-==::         
         .==--+=-=+--         
          :==+===++-          
          :========:          
       .=*%:+====-=**+-:      
  .=+*%@%%%+.=+#+:*##%@@%%*-. 
=%%%%%%@@%%%:-.-:-#%%@@%%%%%#=
@%%%%%%%%%%%*....:%@@@@%@%%@##
@%%@%%%%%%%%%:. .=%%%@@%@%%@%%
''')

    confirm = input('Confirma seu voto? (S/N): ').upper()
    print()

    if (confirm == 'S'):
        urna()
        
        vlula.append(1)

    elif (confirm == 'N'):
      print('Voto descartado!')

def bolsonaro(candidatos, vbolso):
    print('-Candidato à presidência 2022-\n'.center(45))
    print('Nome: Bolsonaro')
    print('Partido: PL')
    print('Número:', (candidatos['Bolsonaro']))
    print()

    print('''                        
          =***%%%%*=.         
        .=-::-==+*#%%*.       
        -..::::--=**#%#       
       :::-:::-=+++**#%-      
       :::==-=#++***#*%=      
       ..::::+#==+++**#:      
        ..::-+*=-=+****       
        .:--:-+*==+**+.       
         ::::-+++=+#*:        
          ::-=***+#+*#.       
          .:-====::+@@%=:     
        -+-.--.  .*%@@@@%%#+-:
    .=*%##-+*-  .*%%%@%%%%%%%%
  -###%###=*##-.*%%%%%%%%%%%%%
 -######%+=#%+.*%%%%%%%%%%%%%%
 +######%=*#%*+%%%%%%%%%%##%%%
 *#####%#***%%%%%%%%%%%%%#%%%%
.*#####%#***#%%%%%%%%%%%%%%%%%
=*####%%#***#%%%%%%%%%%%%%@%%%
''')

    confirm = input('Confirma seu voto? (S/N): ').upper()
    print()

    if (confirm == 'S'):
        urna()

        vbolso.append(1)

    elif (confirm == 'N'):
      print('Voto descartado!')

def ciro(candidatos, vciro):
    print('-Candidato à presidência 2022-\n'.center(45))
    print('Nome: Ciro Gomes')
    print('Partido: PDT')
    print('Número:', (candidatos['Ciro Gomes']))
    print()

    print('''           .:::.              
         .==-==+*+.           
         =-:.::-+##.          
         =--::-=+%%:          
        .---=-+=+#@=          
         :---:+*+##           
          ----+#**            
          :---=+%#-:          
        .. .:-*%####*+=-.     
     ...  .   :*++*==----+.   
   ...... ...-=*#--::::::+*:  
   ..... ......+#=.::::::=#+: 
   ............+*#-::::::-#**.
..............:=+**::::::+%#*+
''')

    confirm = input('Confirma seu voto? (S/N): ').upper()
    print()

    if (confirm == 'S'):
        urna()

        vciro.append(1)

    elif (confirm == 'N'):
      print('Voto descartado!')

def simone(candidatos, vsimone):
    print('-Candidato à presidência 2022-\n'.center(45))
    print('Nome: Simone Tebet')
    print('Partido: MDB')
    print('Número:', (candidatos['Simone Tebet']))
    print()

    print('''            :=**+-..          
          :*#%#+**%@%=        
         -##%-:.:::+@%        
        .%@%=-++:-*+@%        
        #@@+:.:::::-**        
       .%@#=::--=+--#*        
       =%%#*--::-=-+%%.       
      :#%@@#=+====+@@@-       
      +#@@@#--+**+*@@*:       
   .-=+@@@*=-:--====*#=:.     
  =%%%%%%%#=--:--=*%%%%%%#+   
 =%%%%#%%%#%##%%%%%%%%%%%%%*  
.#%%%%#%#%#%##%%%%%%%%%@@@%%#.
=%%@%#%#%%#%##%%%%%%%%@@@@@@@=
*%@@%###%%%#%%%%%%%%%@@@@@@@@#
''')

    confirm = input('Confirma seu voto? (S/N): ').upper()
    print()

    if (confirm == 'S'):
        urna()

        vsimone.append(1)

    elif (confirm == 'N'):
      print('Voto descartado!')

def leo(candidatos, vleo):
    print('-Candidato à presidência 2022-\n'.center(45))
    print('Nome: Leonardo Péricles')
    print('Partido: UP')
    print('Número:', (candidatos['Leonardo Péricles']))
    print()

    print('''                              
            .:--.             
         .+#*#%%##+.          
         #%%#+==*%%#.         
        :%%#%#*#*#%%:         
         +#*##*++*%=          
          =#%***#+:         .*
           *##+++:        .:-%
         .:*%%##*: ......::--%
      .::=+***=-........-----*
   .....:::::--:-=+=:.::---=-.
  .::...-=-.=*=+##+%-:-----   
  ::-::-+::.=*=%*%+#-.:---    
 .---=-++=*:-*++-++-=-::--    
 :--===+++=+====+---::..--    
''')

    confirm = input('Confirma seu voto? (S/N): ').upper()
    print()

    if (confirm == 'S'):
        urna()

        vleo.append(1)

    elif (confirm == 'N'):
      print('Voto descartado!')

def result(candidatos, votos, vlula, vbolso, vciro, vsimone, vleo, end, tamn):
    print('~' * tamn)
    print(end.center(tamn-3))  
    print('~' * tamn)

    lulal = []
    cont = 0
    for v in vlula:
        cont = cont + v

    lulal.append('Lula')
    lulal.append(cont)
    votos.append(lulal)

    bolsol = []
    cont = 0
    for v in vbolso:
        cont = cont + v

    bolsol.append('Bolsonaro')
    bolsol.append(cont)
    votos.append(bolsol)

    cirol = []
    cont = 0
    for v in vciro:
        cont = cont + v

    cirol.append('Ciro Gomes')
    cirol.append(cont)
    votos.append(cirol)

    simonal = []
    cont = 0
    for v in vsimone:
        cont = cont + v

    simonal.append('Simone Tebet')
    simonal.append(cont)
    votos.append(simonal)

    leol = []
    cont = 0
    for v in vleo:
        cont = cont + v

    leol.append('Leonardo Péricles')
    leol.append(cont)
    votos.append(leol)

    print()

    total = 0 
    for c in votos:
      total = total + c[1]

    maior = 0
    for c in votos:
        if (c[1] > maior):
            maior = c[1]
            eleito = c[0]
            votos.remove(c)

    pcent = 100/(total/maior)
    pcent = round(pcent, 0)

    achou = False
    for c in votos:
        if (c[1] == maior):
            achou = True
            eleito2 = c[0]
            print('EMPATE!\n')
            print(f'Candidatos: {eleito} e {eleito2}')   
            print('Votos:', maior)
            print()
            print('~' * tamn)

    if (achou == False):
        if (eleito == 'Lula'):
            lulaeleito(candidatos)
            print(f'Percentual de Votos: {pcent}%')
        elif (eleito == 'Bolsonaro'):
            bolsonaroeleito(candidatos)
            print(f'Percentual de Votos: {pcent}%')
        elif (eleito == 'Ciro Gomes'):
            ciroeleito(candidatos)
            print(f'Percentual de Votos: {pcent}%')
        elif (eleito == 'Simone Tebet'):
            simoneleita(candidatos)
            print(f'Percentual de Votos: {pcent}%')
        elif (eleito == 'Leonardo Péricles'):
            leoeleito(candidatos)
            print(f'Percentual de Votos: {pcent}%')
        print()

    if (total == 0):
      print('Nenhum voto ')

def lulaeleito(candidatos):
    print('Nome: Lula')
    print('Partido: PT')
    print('Número:', (candidatos['Lula']))
    print()

    print('''            -=+=-::.          
           -====----:         
          =+=------..         
         :+===+=-==::         
         .==--+=-=+--         
          :==+===++-          
          :========:          
       .=*%:+====-=**+-:      
  .=+*%@%%%+.=+#+:*##%@@%%*-. 
=%%%%%%@@%%%:-.-:-#%%@@%%%%%#=
@%%%%%%%%%%%*....:%@@@@%@%%@##
@%%@%%%%%%%%%:. .=%%%@@%@%%@%%
''')

def bolsonaroeleito(candidatos):
    print('Nome: Bolsonaro')
    print('Partido: PL')
    print('Número:', (candidatos['Bolsonaro']))
    print()

    print('''                        
          =***%%%%*=.         
        .=-::-==+*#%%*.       
        -..::::--=**#%#       
       :::-:::-=+++**#%-      
       :::==-=#++***#*%=      
       ..::::+#==+++**#:      
        ..::-+*=-=+****       
        .:--:-+*==+**+.       
         ::::-+++=+#*:        
          ::-=***+#+*#.       
          .:-====::+@@%=:     
        -+-.--.  .*%@@@@%%#+-:
    .=*%##-+*-  .*%%%@%%%%%%%%
  -###%###=*##-.*%%%%%%%%%%%%%
 -######%+=#%+.*%%%%%%%%%%%%%%
 +######%=*#%*+%%%%%%%%%%##%%%
 *#####%#***%%%%%%%%%%%%%#%%%%
.*#####%#***#%%%%%%%%%%%%%%%%%
=*####%%#***#%%%%%%%%%%%%%@%%%
''')

def ciroeleito(candidatos):
    print('Nome: Ciro Gomes')
    print('Partido: PDT')
    print('Número:', (candidatos['Ciro Gomes']))
    print()

    print('''           .:::.              
         .==-==+*+.           
         =-:.::-+##.          
         =--::-=+%%:          
        .---=-+=+#@=          
         :---:+*+##           
          ----+#**            
          :---=+%#-:          
        .. .:-*%####*+=-.     
     ...  .   :*++*==----+.   
   ...... ...-=*#--::::::+*:  
   ..... ......+#=.::::::=#+: 
   ............+*#-::::::-#**.
..............:=+**::::::+%#*+
''')

def simoneleita(candidatos):
    print('Nome: Simone Tebet')
    print('Partido: MDB')
    print('Número:', (candidatos['Simone Tebet']))
    print()

    print('''            :=**+-..          
          :*#%#+**%@%=        
         -##%-:.:::+@%        
        .%@%=-++:-*+@%        
        #@@+:.:::::-**        
       .%@#=::--=+--#*        
       =%%#*--::-=-+%%.       
      :#%@@#=+====+@@@-       
      +#@@@#--+**+*@@*:       
   .-=+@@@*=-:--====*#=:.     
  =%%%%%%%#=--:--=*%%%%%%#+   
 =%%%%#%%%#%##%%%%%%%%%%%%%*  
.#%%%%#%#%#%##%%%%%%%%%@@@%%#.
=%%@%#%#%%#%##%%%%%%%%@@@@@@@=
*%@@%###%%%#%%%%%%%%%@@@@@@@@#
''')

def leoeleito(candidatos):
    print('Nome: Leonardo Péricles')
    print('Partido: UP')
    print('Número:', (candidatos['Leonardo Péricles']))
    print()

    print('''                              
            .:--.             
         .+#*#%%##+.          
         #%%#+==*%%#.         
        :%%#%#*#*#%%:         
         +#*##*++*%=          
          =#%***#+:         .*
           *##+++:        .:-%
         .:*%%##*: ......::--%
      .::=+***=-........-----*
   .....:::::--:-=+=:.::---=-.
  .::...-=-.=*=+##+%-:-----   
  ::-::-+::.=*=%*%+#-.:---    
 .---=-++=*:-*++-++-=-::--    
 :--===+++=+====+---::..--    
''')
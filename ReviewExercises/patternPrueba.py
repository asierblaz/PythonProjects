


zabalera=5

for i in range (zabalera):
    for j in range(zabalera-i):
        print('  ', end="")
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(zabalera):
    for j in range(zabalera):
        if(j>=i):
            print('* ', end="")
        else:
            print('? ', end="")


    print('')




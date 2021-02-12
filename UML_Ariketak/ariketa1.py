'''

20 eta 50 zenbakien artean dauden zenbaki bikoitiak batu eta biderkatu egiten duen programa.



'''
batuketa =0
biderketa=1

for i in range(20,51):
    if(i % 2==0):
        biderketa= biderketa*i
        batuketa= batuketa+i

print("biderketa",biderketa)
print("batuketa",batuketa)
'''
3.	Idatzi dd/ mm /aaaa formatuan data eskatzen duen programa eta pantailan data berdina
dd/ <hilabetearen izena> /aaaa formatuan bistaratzen duena.**Derrigorrez hasierako datuaraen formatua mantendu.

'''

hilabeteak= {1:'Enero',2:'Febrero',3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre',12:'Dicembre'}
eguna = input('sartu eguna (dd)')
mes= int(input('Sartu hila (mm)'))
urtea = input('Sartu urtea (aaaa)')


print(eguna, "/", hilabeteak[mes], "/ " ,urtea)
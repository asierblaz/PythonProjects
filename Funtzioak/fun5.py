'''
21/01/2021 Asier Blazquez
5.	Idatzi funtzio bat zeinek testu bat eta hitz bat jaso ostean, hitza testuan dagoen edo ez erantzungo digun.'''

def badago(textua,hitza):
    s=""
    if hitza in textua:
        s= "hitza textuan dago"
    else:
        s= "hitza ez dago textuan"
    return s



textua =input("Sartu Textu bat: ")

hitza =input("Sartu hitz  bat: ")


print(badago(textua,hitza))

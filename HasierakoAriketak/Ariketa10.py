'''
27/11/2020 Asier Blazquez

10- ikasle baten hiru nota sartu eta batazbestekoa kalkulatu
'''

prog = float(input('PROGRAMAZIOA: '))
analisi =float(input('ANALISIA: '))
sareak = float(input('SAREAK: '))
media = float((prog+analisi+sareak)/3)
print('BATAZBESTEKOA:',round(media,2))
import re
from datetime import datetime
from prettytable import PrettyTable
import pygal
import os
from pkg.mail_module import expediaza_alerta_stoc
from pkg.mail_module import expediaza_fisa_produs
import regex


class Stoc:
    """Despre gestiunea produselor"""

    categorii = {}
    limita = 50

    def __init__(self, denp, categ, um='buc', sold=0):
        """metoda constructor"""
        self.denp = denp
        self.categ = categ
        self.um = um
        self.sold = sold
        self.do = {}
        if categ in Stoc.categorii:
            self.categorii[categ] += [denp]
        else:
            self.categorii[categ] = [denp]

    def gen_cheia(self):
        if self.do:
            cheia = max(self.do.keys()) + 1
        else:
            cheia = 1
        return cheia

    def intrari(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        cheia = self.gen_cheia()
        self.do[cheia] = [data, cant, 0]
        self.sold += cant

    def iesiri(self, cant, data=str(datetime.now().strftime('%Y%m%d'))):
        cheia = self.gen_cheia()
        if self.sold < cant:
            cant = self.sold
        self.do[cheia] = [data, 0, cant]
        self.sold -= cant
        if self.sold < self.limita:
            pass
            # expediaza_alerta_stoc(self.limita)

    def desen_grafic(self, data_start=str(datetime.now().strftime('%Y%m%d')),
                     data_sfarsit=str(datetime.now().strftime('%Y%m%d'))):
        """Grafic intrari si iesiri a unui produs"""
        listeaza = PrettyTable()
        listeaza.field_names = ['Data', 'Intrare', 'Iesire']
        intrari = []
        iesiri = []
        for i in self.do.values():
            if i[0] > data_start and i[0] < data_sfarsit:
                listeaza.add_row([i[0], i[1], i[2]])
                intrari.append(i[1])
                iesiri.append(i[2])
        print(listeaza)
        diagrama = pygal.Bar()
        diagrama.title = f'Intrari- iesiri in perioada {data_start} - {data_sfarsit}'
        diagrama.add('Intrari', intrari)
        diagrama.add("Iesiri", iesiri)
        diagrama.render_to_file("intrari-iesiri.svg")
        os.system('intrari-iesiri.svg')

    def fisap(self):
        print(f'Fisa produsului {self.denp} {self.um}')
        listeaza = PrettyTable()
        listeaza.field_names = ['Nrc', 'Data', 'Intrare', 'Iesire']
        for k, v in self.do.items():
            listeaza.add_row([k, v[0], v[1], v[2]])
        print(listeaza)
        print('Stoc final: ', self.sold)

    def expediere_fisa_produs(self):
        expediaza_fisa_produs()

    def cauta(self, denumire_cautata, tranzactie=float, intrari=1, iesiri=1):
        listeaza = PrettyTable()
        listeaza.field_names = ['Nrc', 'Data', 'Intrare', 'Iesire']
        if re.search(denumire_cautata, listeaza):
            print(listeaza)
        else:
            print('Nu este produsul in Stoc')
        if re.search(tranzactie, intrari):
            print(listeaza)
        else:
            print('Nu exista tranzactia')
        if re.search(tranzactie, iesiri):
            print(listeaza)
        else:
            print('Nu exista tranzactia')


prune = Stoc('prune', 'fructe', 'kg')
prune.__dict__
prune.categorii

prune.categorii

prune.intrari(100, '20210501')
prune.iesiri(71, '20210502')
prune.intrari(80)
prune.iesiri(87)
prune.intrari(120, "20210223")
prune.intrari(30, "20210525")
prune.intrari(50, "20210805")
prune.iesiri(25, '20210925')
prune.iesiri(50, '20211002')

prune.do
prune.fisap()
prune.desen_grafic('20210101', "20220101")

import datetime
from database.DAO import getRetailers, getProducts, getVendite, getVendite, getVenditeFiltrate


class Model:
    def __init__(self):
        pass

    def applicaFiltri(self, filtro1, filtro2, filtro3):

        vendite = getVenditeFiltrate(filtro1, filtro2, filtro3)
        return vendite


    def getBestVendita(self, lista):

        best = None
        max = 0

        for v in lista:

            ricavo = v.Unit_sale_price * v.Quantity

            if ricavo > max:

                max = ricavo
                best = v

        return best

    def analizzaVendite(self, lista):

        totRicavi = 0
        numVendite = len(lista)
        retailers = []
        prodotti = []

        for x in lista:
            if retailers.__contains__(x.Retailer):
                pass
            else:
                retailers.append(x.Retailer)

            if prodotti.__contains__(x.Product):
                pass
            else:
                prodotti.append(x.Product)

            totRicavi = totRicavi + (x.Quantity*x.Unit_sale_price)

        numRetailers = len(retailers)
        numProdotti = len(prodotti)

        stringa = "Statistiche vendite:\nGiro d'affari: " + str(totRicavi) + "\nNumero vendite: " + str(numVendite) + "\nNumero retailers coinvolti: " + str(numRetailers) + "\nNumero prodotti coinvolti: " + str(numProdotti)

        return stringa

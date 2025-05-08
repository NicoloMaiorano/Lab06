import flet as ft
from database.DAO import getRetailers, getAnno, getBrand, getVendite


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillAnno(self):
        """
            Metodo che riempe il dropdown per il filtro in base all'anno
        """
        lista = getAnno()

        for x in lista:
            self._view.ddAnno.options.append(ft.dropdown.Option(x))

    def fillBrand(self):
        """
            Metodo che riempe il dropdown per il filtro in base al brand
        """
        lista = getBrand()

        for x in lista:
            self._view.ddBrand.options.append(ft.dropdown.Option(x))

    def fillRetailer(self):
        """
            Metodo che rimepe il dropdown per il filtro in base al retailer
        """
        lista = getRetailers()

        for x in lista:
            self._view.ddRetailer.options.append(ft.dropdown.Option(x.Retailer_name))

    def topVendite(self, e):
        """
            Metodo che resistuisce a schermo le 5 migliori vendite in base ai filtri selezionati
        """
        #Prendo dai dropdown i valori dei filtri da applicare
        filtro1 = self._view.ddAnno.value
        filtro2 = self._view.ddBrand.value
        filtro3 = self._view.ddRetailer.value

        #Applico i filtri alla lista di tutte le vendite in modo da trovare solo quelle che mi interessano
        vendite = self._model.applicaFiltri(filtro1, filtro2, filtro3)

        #lista che conterrà le vendite migliori
        lista = []
        i=0
        #Ciclo per cercare le 5 vendite migliori usando il metodo getBestVendita

        while i <5:
            x = self._model.getBestVendita(vendite)

            lista.append(x)
            vendite.remove(x)
            i=i+1

        for b in lista:
            self._view.txt_result.controls.append(ft.Text(str(b)))
            self._view.update_page()

    def analizzaVendite(self, e):
        filtro1 = self._view.ddAnno.value
        filtro2 = self._view.ddBrand.value
        filtro3 = self._view.ddRetailer.value

        vendite = self._model.applicaFiltri(filtro1, filtro2, filtro3)
        print(len(vendite))

        result = self._model.analizzaVendite(vendite)

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(result))
        self._view.update_page()
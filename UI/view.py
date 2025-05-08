import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #Creazione e popolazione dei dropdown
        self.ddAnno = ft.Dropdown(label="Anno", hint_text="Filtra per anno", width=200)
        self.ddBrand = ft.Dropdown(label="Brand", hint_text="Filtra per brand", width=200)
        self.ddRetailer = ft.Dropdown(label="Retailer", hint_text="Filtra per retailer", width=200)
        self._controller.fillRetailer()
        self._controller.fillAnno()
        self._controller.fillBrand()

        row1 = ft.Row([self.ddAnno, self.ddBrand, self.ddRetailer], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        #creazione pulsati
        self.topVendite = ft.ElevatedButton(text="Top vendite", on_click=self._controller.topVendite)
        self.analizzaVendite = ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.analizzaVendite)

        row2 = ft.Row([self.topVendite, self.analizzaVendite], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

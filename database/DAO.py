from database.DB_connect import get_connection
from model.product import Product
from model.retailer import Retailer
from model.sale import Sale


class DAO():
    def __init__(self):
        pass

def getRetailers():

    db = get_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM GO_RETAILERS")
    lista = []

    for c in cursor:

        x = Retailer(**c)

        lista.append(x)

    db.close()
    return lista

def getAnno():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT YEAR(DATE) FROM GO_DAILY_SALES")
    lista = []

    for c in cursor:

        if lista.__contains__(c[0]):
            pass
        else:
            lista.append(c[0])

    db.close()
    return lista

def getBrand():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT PRODUCT_BRAND FROM GO_PRODUCTS")
    lista = []

    for c in cursor:
        if lista.__contains__(c[0]):
            pass
        else:
            lista.append(c[0])

    db.close()
    return lista

def getProducts():
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM GO_PRODUCTS")
    lista = []

    for c in cursor:
        x = Product(**c)
        lista.append(x)

    db.close()
    return lista

def getVendite():
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM GO_DAILY_SALES")

    lista = []
    listaRetailers = getRetailers()
    listaProdotti = getProducts()
    prodotto = None
    retailer = None

    for c in cursor:

        for p in listaProdotti:
            if p.Product_number == c["Product_number"]:
                prodotto = p

        for r in listaRetailers:
            if r.Retailer_code == c["Retailer_code"]:
                retailer = r

        x = Sale(retailer, prodotto, c["Order_method_code"], c["Date"], c["Quantity"], c["Unit_price"], c["Unit_sale_price"])
        lista.append(x)

    db.close()
    return lista

def getVenditeFiltrate(filtro1, filtro2, filtro3):
    db = get_connection()
    lista = []
    listaRetailers = getRetailers()
    listaProdotti = getProducts()
    prodotto = None
    retailer = None
    cursor = db.cursor(dictionary=True)
    query = """SELECT gds.*, gds.Unit_sale_price*gds.Quantity AS Ricavo
                    FROM go_daily_sales gds, go_retailers gr, go_products gp 
                    WHERE gds.Retailer_code  = gr.Retailer_code  
                    AND gds.Product_number = gp.Product_number 
                    AND (YEAR(gds.Date)=COALESCE(%s,YEAR(gds.Date)))
                    AND (gp.Product_brand =COALESCE(%s,gp.Product_brand))
                    AND (gr.Retailer_name =COALESCE(%s,gr.Retailer_name))"""
    cursor.execute(query, (filtro1, filtro2, filtro3))

    for c in cursor:
        for p in listaProdotti:
            if p.Product_number == c["Product_number"]:
                prodotto = p

        for r in listaRetailers:
            if r.Retailer_code == c["Retailer_code"]:
                retailer = r

        x = Sale(retailer, prodotto, c["Order_method_code"], c["Date"], c["Quantity"], c["Unit_price"],c["Unit_sale_price"])
        lista.append(x)

    cursor.close()
    db.close()
    return lista









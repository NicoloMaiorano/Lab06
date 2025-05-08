from dataclasses import dataclass
from model.retailer import Retailer
from model.product import Product

@dataclass
class Sale:
   Retailer : Retailer
   Product : Product
   Order_method_code : int
   Date : str
   Quantity : int
   Unit_price : float
   Unit_sale_price : float

   def __str__(self):
      ricavo = self.Unit_sale_price * self.Quantity
      x = "Date: " + str(self.Date) +"; Ricavo: " + str(ricavo) + "; Retailer: " + str(self.Retailer.Retailer_code) + "; Product: " + str(self.Product.Product_number)
      return x
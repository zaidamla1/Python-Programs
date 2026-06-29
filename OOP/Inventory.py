class Inventory:
    def __init__(self,productId,name,price,qty):
        self.productId = productId
        self.name = name
        self.price = price
        self.qty = qty
    
    def restock(self,qty):
        self.qty += qty
        return self.qty
    
    def sell(self,qty):
        if(qty > self.qty):
            self.sales = "Insufficient Qty"
            return self.sales
        else:
            self.sales = self.price * qty
            self.qty -= qty
            return self.sales
    
    def apply_discount(self,percentage):
        self.percentage = percentage
        self.discount = self.price * self.percentage / 100
        self.price -= self.discount
        return [self.discount,self.percentage , self.price]
    
    def invoice(self):
         print(f"Name of product: {self.name}")
         print(f"Price of product: {self.price}")
         print(f"Discount received: {self.percentage}%")
         print(f"Discount amount: {self.discount}")
         print(f"Final price after discount {self.sales}")
    

i1 = Inventory('P-001',"Rice",500,10)
i1.restock(5)
i1.apply_discount(20)
i1.sell(15)
i1.invoice()      
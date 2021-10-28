class Product:
    count=0
    def __init__ (self,name,category,description,price):
        self.name=name
        self.category=category
        self.description=description
        self.price=price
        Product.count=Product.count+1
    def display_product(self):
        print("name:",self.name)
        print("category:",self.category)
        print("description:",self.description)
        print("price:",self.price)
    def product_count(self):
        print("Total no. of products: %d" % Product.count)
prod1=Product("LEE COOPER","Watch","Rose Gold colour",3000)
prod2=Product("ALLEN SOLLY","T-shirt","Green colour",899)
prod1.display_product()
prod2.display_product()
prod1.product_count()

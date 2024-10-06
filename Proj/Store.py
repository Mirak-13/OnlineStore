from DB import show_all, show_any, query, return_result

class Market:

    def show_all():
        return show_all
    
    def show_any(self, text):
        return show_any(text)
    
    def update(self, text):
        return query(text)
    

class Basket:
    
    def __init__(self, products = []):
        self.products = products

    def show_basket(self):
        return self.products

    def add_basket(self, result):
        self.products.append(*return_result(result))
    
    def del_basket(self, id):
        del self.products[id]
    




basket = Basket()

basket.add_basket('select * from market where product_id = 1')
basket.add_basket('select * from market where product_id = 3')
basket.del_basket(1)
print(basket.show_basket())
# Импорт функций взаимодействующих с базой данных
from DB import show_all, show_any, query, return_result


# Класс магазин
class Market:

    # Функция показать все из БД
    def show_all(self):
        return show_all()

    # Функция показать по конкретному запросу из БД
    def show_any(self, text):
        return show_any(text)

    # Фнкция изменить содержимое БД
    def update(self, text):
        return query(text)


# Класс корзина добавляет продукты в виде кортежа и хранит все в в списке
class Basket:

    def __init__(self, products=[]):
        self.products = products

    # Функция показать все из корзины
    def show_basket(self):
        return self.products

    # Функция добавить в корзину
    def add_basket(self, result):
        self.products.append(*return_result(result))

    # Функция удалить из корзины
    def del_basket(self, id):
        del self.products[id]


market = Market()
basket = Basket()

basket.add_basket("select * from market where product_id = 1")
basket.add_basket("select * from market where product_id = 3")
basket.del_basket(1)

print(basket.show_basket())

market.show_all()

# Содержимое БД по запросу market.show_all()

# ('Номер', 'Название', 'Описание', 'Цена', 'Количество')
# (2, 'Iphone 13', '128 ГБ, Product red', Decimal('71000.00'), 700)
# (3, 'Focusrite 2i2', 'Аудио интерфейс, 1 XLR, 1 Jack 6.3', Decimal('3500.00'), 200)
# (4, 'Ручка', 'Шариковая, Синяя', Decimal('49.00'), 1000)
# (1, 'HP Omen 15', 'Ноутбук, 16 дюймов, Процессор: intel i5, Видкокарта: Geforce GTX 1050 TI', Decimal('51000.00'), 60)
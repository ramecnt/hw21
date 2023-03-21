from storage import Storage


class Store(Storage):
    def __init__(self, items, capacity=100):
        self._items = items
        self._capacity = capacity

    def add(self, name, qnt):
        if self.get_items().get(name) is not None:
            if self.get_free_space() < qnt:
                print("На складе недостаточно места, попробуйте заказать меньше товара")
                raise ValueError
            else:
                self.get_items()[name] += qnt
        else:
            self.get_items()[name] = qnt
        print(f"Курьер везет {qnt} {name} на склад\n"
              f"Курьер доставил {qnt} {name} в магазин")

    def remove(self, name, qnt):
        if self.get_items().get(name) is not None:
            if self.get_items()[name] < qnt:
                print("Не хватает товара на складе, попробуйте заказать меньше")
                raise ValueError
            else:
                self.get_items()[name] -= qnt
                print(f'Нужное количество есть на складе\n'
                      f'Курьер забрал {qnt} {name} со склада')
        else:
            print("На складе нет такого товара")
            raise TypeError

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self.get_items())

    def get_info(self):
        for k, v in self.get_items().items():
            print(k, v)

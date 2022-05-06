from abc import abstractmethod, ABC


class Storage:
    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def capacity(self):
        pass

    @abstractmethod
    def add(self, title, quantity):
        pass

    @abstractmethod
    def remove(self, title, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100
        self._type = "склад"

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    """Увеличивает запас items с учетом лимита capacity"""
    def add(self, title, quantity):
        if quantity <= self.capacity:
            if title in self.items:
                self.items[title] += quantity
            else:
                self.items[title] = quantity
            self.capacity -= quantity
            return f"{self._type}: добавлено {quantity} {title}"
        else:
            if title in self.items:
                self.items[title] += self.capacity
            else:
                self.items[title] = self.capacity
            r_str = f"{self._type}: добавлено {self.capacity} {title}, возможность для размещения " \
                    f"{quantity - self.capacity} {title} отсутствует"
            self.capacity = 0
            return r_str

    """Уменьшает запас items но не ниже 0"""
    def remove(self, title, quantity):
        if title not in self.items:
            return f"{self._type}: данный товар отсутствует"
        if self.items[title] > quantity:
            self.capacity += quantity
            self.items[title] -= quantity
            return f"{self._type}: изъято {quantity} {title}, осталось - {self.items[title]}"
        else:
            self.capacity += self.items[title]
            balance = quantity - self.items[title]
            self.items[title] -= quantity
            del self.items[title]
            if balance == 0:
                return f"{self._type}: изъято {quantity} {title}, осталось - 0"
            return f"{self._type}: запрошено превышающее количество. Изъято {quantity - balance} " \
                   f"{title}, не хватило - {balance}"

    """Возвращает количество свободных мест"""
    def get_free_space(self):
        return self.capacity

    """Возвращает содержание склада в словаре {товар: количество}"""
    def get_items(self):
        return self.items

    """возвращает количество уникальных товаров"""
    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self):
        super().__init__()
        self._capacity = 20
        self._type = "магазин"

    """Увеличивает запас items с учетом лимита capacity (не больше 5 товаров)"""
    def add(self, title, quantity):
        if self.get_unique_items_count() < 5:
            return super().add(title, quantity)
        return "Достигнут лимит товара для этого магазина"


class Request:
    def __init__(self, from_, to, amount='0', product=None):
        self.from_ = from_
        self.to = to
        self.amount = int(amount)
        self.product = product

    """Создание экземпляра Reuqest из строки"""
    @staticmethod
    def get_param_from_str(string):
        data = string.split(' ')
        new_req = Request(from_=data[4], to=data[6], amount=data[1], product=data[2])
        return new_req

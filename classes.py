from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, title, count):
        pass

    @abstractmethod
    def remove(self, title, count):
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

    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def add(self, title, count):
        """ увеличивает запас items """
        if title in self.__items.keys():
            if self.get_free_space() >= count:
                print("Товар добавлен")
                self.__items[title] += count
                return True
            else:
                if isinstance(self, Shop):
                    print("\nНедостаточно места в магазине!!!\n")
                else:
                    print("\nНедостаточно места на складе!!!\n")
                return False
        else:
            if self.get_free_space() >= count:
                print("Товар добавлен")
                self.__items[title] = count
                return True
            else:
                if isinstance(self, Shop):
                    print("\nНедостаточно места в магазине!!!\n")
                else:
                    print("\nНедостаточно места на складе!!!\n")
                return False

    def remove(self, title, count):
        """ уменьшает запас items """
        if self.__items[title] >= count:
            print("Нужное количество есть на складе")
            self.__items[title] -= count
            return True
        else:
            print("\nНедостаточно товара на складе!!!\n")
            return False

    def get_free_space(self):
        """ возвращает количество свободных мест """
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        """ возвращает количество уникальных товаров """
        return len(self.__items.keys())

    def __str__(self):
        st = "\n"
        for key, value in self.__items.items():
            st += f"{key}: {value}\n"
        return st


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, title, count):
        """ увеличивает запас items с учетом лимита capacity """
        if self.get_unique_items_count() >= 5:
            print("Слишком много уникальных товаров")
            return False
        else:
            super().add(title, count)


class Request:
    def __init__(self, request_str):
        req_list = request_str.split()
        action = req_list[0]
        self.__count = int(req_list[1])
        self.__item = req_list[2]
        if action == "Доставить":
            self.__from = req_list[4]
            self.__to = req_list[6]
        elif action == "Забрать":
            self.__from = req_list[4]
            self.__to = None
        elif action == "Привезти":
            self.__from = None
            self.__to = req_list[4]

    def movi(self):
        if self.__to and self.__from:
            if eval(self.__to).add(self.__item, self.__count):
                eval(self.__from).remove(self.__item, self.__count)
        elif self.__to:
            eval(self.__to).add(self.__item, self.__count)
        elif self.__from:
            eval(self.__from).remove(self.__item, self.__count)


storage_1 = Store(items={"Телефон": 10, "Comp": 10, "Telek": 20})
storage_2 = Store(items={"Телефон": 10, "Comp": 10, "Disk": 10})
shop_1 = Shop(items={"Телефон": 3, "Comp": 3, "Telek": 3})

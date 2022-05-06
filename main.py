from classes import Request, Shop, Store

"""Создаём экземпляр магазина"""
shop = Shop()

"""Создаём экземпляр склада"""
store = Store()

"""Наполняем склад"""
store.add('печеньки', 20)
store.add('собачки', 20)
store.add('коробки', 20)
store.add('стаканчики', 20)

if __name__ == '__main__':

    while True:

        """Ввод и проверка запроса (длинна, правильный ввод пунктов доставки и отправки)"""
        while True:
            correct_len = True
            correct_dep_point = True
            correct_arr_point = True
            user_request = input("Введите запрос. Например: Доставить 3 собачки из склад в магазин\n")
            len_str = user_request.split(' ')
            if len(len_str) >= 7:
                req = Request.get_param_from_str(user_request)

                """Исключение неизвестных названий"""
                if req.from_ != 'склад' and req.from_ != 'магазин':
                    print("Пункт отправки неизвестен")
                    correct_dep_point = False

                if req.to != 'склад' and req.to != 'магазин':
                    print("Пункт доставки неизвестен")
                    correct_arr_point = False
            else:
                correct_len = False
                print('Неверный запрос')

            if correct_len and correct_dep_point and correct_arr_point:
                break

        """Определение пунктов отправки и доставки"""
        if req.from_ == 'склад':
            dep_point = store
            arr_point = shop
        else:
            dep_point = shop
            arr_point = store

        """Логика программы"""
        if req.product in dep_point.get_items():
            if dep_point.get_items()[req.product] >= req.amount:
                print(f"{req.from_}: нужное количество в наличии")
                if arr_point.get_free_space() >= req.amount:
                    print(f"{req.to}: имеется {arr_point.get_free_space()} свободных мест")
                    print(dep_point.remove(req.product, req.amount))
                    print(f"Курьер: {req.amount} {req.product} в пути")
                    print(arr_point.add(req.product, req.amount))
                else:
                    print(f"{req.to}: недостаточно свободного места для {req.amount} {req.product}")
                    print(f"{req.to}: свободных мест - {arr_point.get_free_space()}")
            else:
                print(f"{req.from_}: указанное количество отсутствует, в наличии {dep_point.get_items()[req.product]}")
        else:
            print(f"{req.from_}: указанный товар отсутствует")

        """Отчёт о заполненности"""
        print(f"\nНа складе хранится:\n")
        for key, value in store.get_items().items():
            print(f'{key} - {value}')

        print(f"\nВ магазине хранится:\n")
        for key, value in shop.get_items().items():
            print(f'{key} - {value}')
        print('_'*10)

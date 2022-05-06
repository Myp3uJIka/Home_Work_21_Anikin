import pytest

from classes import Store


class TestStorage:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = Store()
        storage.add('item1', 20)
        storage.add('item1', 50)
        storage.add('item2', 30)
        return storage

    def test_add_storage(self):
        storage = Store()
        assert storage.add('item1', 20) == 'На склад добавлено 20 item1'
        assert storage.add('item1', 50) == 'На склад добавлено 50 item1'
        assert storage.add('item2', 40) == 'На склад добавлено 30 item2, ' \
                                           'возможность для размещения 10 item2 отсутствует'
        assert storage.add('item3', 1) == 'На склад добавлено 0 item3, возможность для размещения 1 item3 отсутствует'

    def test_remove_storage(self, storage):
        assert storage.remove('item99', 1) == "Данного товара на складе нет"
        assert storage.remove('item1', 40) == 'Со склада изъято 40 item1, осталось на складе - 30'
        assert storage.remove('item1', 60) == 'Запрошено превышающее на складе количество. ' \
                                              'Со склада изъято 30 item1, не хватило - 30'

    def test_free_space_storage(self, storage):
        assert storage.get_free_space() == 0

    def test_get_items_storage(self, storage):
        assert storage.get_items() == {'item1': 70, 'item2': 30}

    def test_get_unique_items_count_storage(self, storage):
        assert storage.get_unique_items_count() == 2

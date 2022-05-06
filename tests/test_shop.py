import pytest

from classes import Shop


class TestStorage:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = Shop()
        storage.add('item1', 2)
        storage.add('item1', 9)
        storage.add('item6', 1)
        storage.add('item7', 1)
        storage.add('item8', 1)
        storage.add('item2', 8)
        return storage

    def test_add_storage(self):
        storage1 = Shop()
        assert storage1.add('item1', 2) == 'На склад добавлено 2 item1'
        assert storage1.add('item1', 9) == 'На склад добавлено 9 item1'
        assert storage1.add('item6', 1) == 'На склад добавлено 1 item6'
        assert storage1.add('item7', 1) == 'На склад добавлено 1 item7'
        assert storage1.add('item8', 1) == 'На склад добавлено 1 item8'
        assert storage1.add('item2', 9) == 'На склад добавлено 6 item2, возможность для размещения 3 item2 отсутствует'
        assert storage1.add('item3', 1) == 'Достигнут лимит товара для этого магазина'

    def test_remove_storage(self, storage):
        assert storage.remove('item99', 1) == "Данного товара на складе нет"
        assert storage.remove('item1', 40) == 'Запрошено превышающее на складе количество. ' \
                                              'Со склада изъято 11 item1, не хватило - 29'
        assert storage.remove('item1', 60) == 'Данного товара на складе нет'

    def test_free_space_storage(self, storage):
        assert storage.get_free_space() == 0

    def test_get_items_storage(self, storage):
        assert storage.get_items() == {'item1': 11, 'item2': 6, 'item6': 1, 'item7': 1, 'item8': 1}

    def test_get_unique_items_count_storage(self, storage):
        assert storage.get_unique_items_count() == 5

import pytest

from classes import Store


class TestStore:
    @pytest.fixture(autouse=True)
    def store(self):
        store = Store()
        store.add('item1', 20)
        store.add('item1', 50)
        store.add('item2', 30)
        return store

    def test_add_store(self):
        store = Store()
        assert store.add('item1', 20) == 'склад: добавлено 20 item1'
        assert store.add('item1', 50) == 'склад: добавлено 50 item1'
        assert store.add('item2', 40) == 'склад: добавлено 30 item2, ' \
                                           'возможность для размещения 10 item2 отсутствует'
        assert store.add('item3', 1) == 'склад: добавлено 0 item3, возможность для размещения 1 item3 отсутствует'

    def test_remove_store(self, store):
        assert store.remove('item99', 1) == "склад: данный товар отсутствует"
        assert store.remove('item1', 40) == 'склад: изъято 40 item1, осталось - 30'
        assert store.remove('item1', 60) == 'склад: запрошено превышающее количество. ' \
                                            'Изъято 30 item1, не хватило - 30'

    def test_free_space_store(self, store):
        assert store.get_free_space() == 0

    def test_get_items_store(self, store):
        assert store.get_items() == {'item1': 70, 'item2': 30}

    def test_get_unique_items_count_store(self, store):
        assert store.get_unique_items_count() == 2

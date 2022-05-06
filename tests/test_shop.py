import pytest

from classes import Shop


class TestShop:
    @pytest.fixture(autouse=True)
    def shop(self):
        shop = Shop()
        shop.add('item1', 2)
        shop.add('item1', 9)
        shop.add('item6', 1)
        shop.add('item7', 1)
        shop.add('item8', 1)
        shop.add('item2', 8)
        return shop

    def test_add_shop(self):
        shop1 = Shop()
        assert shop1.add('item1', 2) == 'магазин: добавлено 2 item1'
        assert shop1.add('item1', 9) == 'магазин: добавлено 9 item1'
        assert shop1.add('item6', 1) == 'магазин: добавлено 1 item6'
        assert shop1.add('item7', 1) == 'магазин: добавлено 1 item7'
        assert shop1.add('item8', 1) == 'магазин: добавлено 1 item8'
        assert shop1.add('item2', 9) == 'магазин: добавлено 6 item2, возможность для размещения 3 item2 отсутствует'
        assert shop1.add('item3', 1) == 'Достигнут лимит товара для этого магазина'

    def test_remove_shop(self, shop):
        assert shop.remove('item99', 1) == "магазин: данный товар отсутствует"
        assert shop.remove('item1', 40) == 'магазин: запрошено превышающее количество. ' \
                                           'Изъято 11 item1, не хватило - 29'
        assert shop.remove('item1', 60) == 'магазин: данный товар отсутствует'

    def test_free_space_shop(self, shop):
        assert shop.get_free_space() == 0

    def test_get_items_shop(self, shop):
        assert shop.get_items() == {'item1': 11, 'item2': 6, 'item6': 1, 'item7': 1, 'item8': 1}

    def test_get_unique_items_count_shop(self, shop):
        assert shop.get_unique_items_count() == 5

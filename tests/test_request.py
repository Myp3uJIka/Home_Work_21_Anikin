from classes import Request


class TestRequest:
    def test_create_request1(self):
        req = Request.get_param_from_str('Доставить 3 печеньки из склад в магазин')
        assert req.from_ == 'склад'
        assert req.to == 'магазин'
        assert req.amount == 3
        assert req.product == 'печеньки'

    def test_create_request2(self):
        req = Request.get_param_from_str('Доставить 4 собачки из склад в магазин')
        assert req.from_ == 'склад'
        assert req.to == 'магазин'
        assert req.amount == 4
        assert req.product == 'собачки'

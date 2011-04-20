import unittest


class MyHandlerTests(unittest.TestCase):
    def setUp(self):
        from pyramid.config import Configurator
        self.config = Configurator(autocommit=True)
        self.config.begin()
        # Must call ``self.config.begin()`` in tests before using config.

    def tearDown(self):
        self.config.end()
        # After calling ``self.config.end()``, don't use config.

    def _makeOne(self, request):
        from gearmandashboard.handlers import MainHandler
        return MainHandler(request)

    def test_index(self):
        request = DummyRequest()
        handler = self._makeOne(request)
        info = handler.index()
        self.assertEqual(info["project"], "gearmandashboard")

class DummyRequest(object):
    pass

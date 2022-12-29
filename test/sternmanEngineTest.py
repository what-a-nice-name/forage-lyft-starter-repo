import unittest


from engine.sternman_engine import SternmanEngine


class SternmanEngineTest(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light = True
        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light = False
        engine = SternamnEngine(warning_light)
        self.assertFalse(engine.needs_service())

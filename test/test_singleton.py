from src.modules.utils.Singleton import Singleton


class FakeSingleton(Singleton):
    """
    Should properly create singleton, even though class is empty
    """
    pass


def test_singleton():
    inst = FakeSingleton()
    inst2 = FakeSingleton()
    assert FakeSingleton.get_instance() is inst
    assert inst2 is inst


def test_singleton_create_instance():
    assert FakeSingleton.get_instance()

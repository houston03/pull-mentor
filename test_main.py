import pytest
from main import tella, call

def test_tella_decorator():
    @tella(2)
    def my_func():
        return 1

    assert my_func() == 1
    assert my_func() == 1
    with pytest.raises(ValueError) as excinfo:
        my_func()
    assert 'calls limit' in str(excinfo.value)

def test_call_function():
    assert call('Test') == "This should only print three times"  # Проверяем возвращаемое значение

def test_call_limit():
    @tella(1)
    def limited_call(name):
        return call(name)

    assert limited_call('Test1') == "This should only print three times"
    with pytest.raises(ValueError):
        limited_call('Test2')
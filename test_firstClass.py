import pytest

class TestFirst:
    def test_1(self):
        var = "welcome"
        assert "c" in var, "the character does not exist in the word"

#assertion with a custom failure message
    def test_2(self):
        var = "bye"
        assert "e" in var, "the character does not exist in the word"

#the below test never executes as "test" keyword is in the suffix but not prefixed in the name. 
    def my_test(self):
        var = "good bye"
        assert hasattr(var, "good bye")

#the below test never executes as it has no "test" keyword in the name
    def tes(self):
        var = "test"
        assert "i" in var

    def test_zero_division():
        with pytest.raises(ZeroDivisionError):
            1 / 0

    def test_recursion_depth():
        with pytest.raises(RuntimeError) as excinfo:

            def f():
                f()
            f()
        assert "maximum recursion" in str(excinfo.value)
        assert "maximum recursion" in str(excinfo.type)
        assert "maximum recursion" in str(excinfo.traceback)
"""

The ini file

"""

from .version import __version__

def test_this():
    print('It works!')

def test_package():
    import test
    test.test_package()

print("Invoking __init__.py for {__name__}")



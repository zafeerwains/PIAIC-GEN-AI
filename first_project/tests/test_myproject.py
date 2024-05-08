from first_project import main


def test_function_hello_world():
    r = main.hello_world()
    assert r != "hello world"
def test_function_hello_world1():
    r = main.hello_world()
    assert r == "Hello World"

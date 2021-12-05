# def add(x,y):
#     return x+y

# assert add(4,5) == 6,"sum value is 9"
# assert add(2,8) == 10,"sum value is 10"


def add(x,y):
    return x+y

def test_int_sum():
    assert add(4,5) == 9,"sum value is 9"

def test_float_sum():
    assert add(4.2,8.5) == 1,"sum value is 12.7"

if __name__ == "__main__":
    test_int_sum()
    test_float_sum()
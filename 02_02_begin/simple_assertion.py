can_access = False

try:
    assert can_access
except AssertionError:
    print("No access!")

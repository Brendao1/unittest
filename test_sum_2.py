def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
# sum of 1+2+2 = 5, not 6, so the test fails

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")

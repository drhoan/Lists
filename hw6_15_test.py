import hw6_15

def test_hw6_15():
    assert hw6_15.is_anagram("listen", "silent") == True
    assert hw6_15.is_anagram("hello", "python") == False
    assert hw6_15.is_anagram("hoan", "noah") == True
    assert hw6_15.is_anagram("hoan", "noahh") == False

if __name__ == "__main__":
    test_hw6_15()
    print("hw6_15_test.py is done")
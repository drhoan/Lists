import hw6_10

def test_hw6_10():
    assert len(hw6_10.create_rand_list()) == 10
    for i in hw6_10.create_rand_list():
        assert 1 <= i <= 100

if __name__ == "__main__":
    test_hw6_10()
    print("hw6_10_test.py is done")
from my_app.app import calculate_mean

def test_calculate_mean():
    data = [1, 2, 3]
    assert  2 == calculate_mean(data)
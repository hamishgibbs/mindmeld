from mindmeld import object


def test_create_object():

    new_object = object.create_object("Zaifeng, Prince Chun",
                                      cby="test")

    assert new_object["attributes"][0]["key"] == "title"
    assert new_object["attributes"][0]["value"] == "Zaifeng, Prince Chun"
    assert new_object["attributes"][0]["cby"] == "test"

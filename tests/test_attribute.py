import pytest
from mindmeld import attribute


@pytest.fixture()
def new_attribute():

    return attribute.create_attribute(key="title",
                                      value="Zaifeng, Prince Chun",
                                      cby="hamishgibbs",
                                      source="https://www.google.com/")


def test_create_attribute(new_attribute):

    assert new_attribute["key"] == "title"
    assert type(new_attribute["ctime"]) is float
    assert new_attribute["modifications"] == []


def test_modify_attribute_once(new_attribute):

    modified = attribute.modify_attribute(new_attribute,
                                          value="Prince Chun",
                                          citation="WikiWiki",
                                          mby="hamishgibbs")

    assert len(modified["modifications"]) == 1
    assert modified["value"] == "Prince Chun"
    assert modified["citation"] == "WikiWiki"

    modification = modified["modifications"][0]

    assert modification["mby"] == "hamishgibbs"
    assert modification["old_value"] == "Zaifeng, Prince Chun"
    assert modification["old_citation"] == "https://www.google.com/"
    assert type(modification["mtime"]) is float


def test_modify_attribute_twice(new_attribute):

    modified = attribute.modify_attribute(new_attribute,
                                          value="Prince Chun2")

    modified = attribute.modify_attribute(modified,
                                          value="Prince Chun3")

    assert len(modified["modifications"]) == 2

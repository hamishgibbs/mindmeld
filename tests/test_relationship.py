from ..mindmeld import relationship


def test_create_relationship():

    new_relationship = relationship.create_relationship(relationship="lives",
                                                        source="uuid1",
                                                        target="uuid2")

    assert len(new_relationship["attributes"]) == 3

    r_value = [x["value"] for x in new_relationship["attributes"] if x["key"] == "relationship"]
    s_value = [x["value"] for x in new_relationship["attributes"] if x["key"] == "source"]
    t_value = [x["value"] for x in new_relationship["attributes"] if x["key"] == "target"]

    assert "lives" in r_value
    assert "uuid1" in s_value
    assert "uuid2" in t_value

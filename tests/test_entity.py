from ..mindmeld import entity


def test__create_entity():

    new_entity = entity._create_entity(attributes=[])

    assert type(new_entity["uuid"]) is str
    assert new_entity["attributes"] == []

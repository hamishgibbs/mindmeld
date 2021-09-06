import pytest
from ..mindmeld import graph
from ..mindmeld import object
from ..mindmeld import relationship


@pytest.fixture()
def example_nodes():

    return [
        object.create_object("object1"),
        object.create_object("object2"),
        object.create_object("object3")
    ]


@pytest.fixture()
def example_edges():

    obj1 = object.create_object("object1")
    obj2 = object.create_object("object2")
    obj3 = object.create_object("object3")

    return {"nodes": [obj1, obj2, obj3],
            "edges": [relationship.create_relationship("knows", obj1["uuid"], obj2["uuid"]),
                      relationship.create_relationship("knows", obj2["uuid"], obj3["uuid"]),
                      relationship.create_relationship("knows", obj3["uuid"], obj1["uuid"])]}


def test_get_nodes(example_nodes):

    nodes = graph.get_nodes(example_nodes)

    assert len(nodes) == 3

    titles = [x["title"] for x in nodes]

    assert ["object1", "object2", "object3"] == titles


def test_get_edges(example_edges):

    edges = graph.get_edges(example_edges["edges"])

    assert len(edges) == 3

    exp_uuids = [x["uuid"] for x in example_edges["nodes"]]
    sources = [x["source"] for x in edges]

    assert exp_uuids == sources

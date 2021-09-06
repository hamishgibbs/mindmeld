# Integration test of system so far

from ..mindmeld import object, relationship, graph, attribute


def test_mindmeld():

    # Represent the sentence:
    # "Prince Chun lived in the Northern Residence in Beijing until 1928."

    # Define objects ["Prince Chun", "Northern Residence"]
    objects = []
    prince = object.create_object("Prince Chun")
    objects.append(prince)

    residence = object.create_object("Northern Residence")
    objects.append(residence)

    # Define relationship ["Prince Chun" -> "lived" -> "Northern Residence"]
    relationships = []

    lived = relationship.create_relationship("lived", prince["uuid"], residence["uuid"])

    # Update relationship with time ["Prince Chun" -> "lived" (1924-1928) -> "Northern Residence"]
    attr = []
    attr.append(attribute.create_attribute("start", "1924"))
    attr.append(attribute.create_attribute("end", "1928"))

    lived["attributes"] = lived["attributes"] + attr

    relationships.append(lived)

    print(graph.get_nodes(objects))
    print(graph.get_edges(relationships))
    #print(relationships)

    assert True

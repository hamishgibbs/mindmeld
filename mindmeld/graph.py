
def get_nodes(objects):

    nodes = []

    for obj in objects:

        title = [x["value"] for x in obj["attributes"] if x["key"] == "title"]

        nodes.append({"uuid": obj["uuid"], "title": title[0]})

    return nodes


def get_edges(relationships):

    edges = []

    for rel in relationships:

        r_value = [x["value"] for x in rel["attributes"] if x["key"] == "relationship"]
        s_value = [x["value"] for x in rel["attributes"] if x["key"] == "source"]
        t_value = [x["value"] for x in rel["attributes"] if x["key"] == "target"]

        edges.append({"uuid": rel["uuid"],
                      "relationship": r_value[0],
                      "source": s_value[0],
                      "target": t_value[0]})

    return edges

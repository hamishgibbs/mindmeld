from datetime import datetime


def create_attribute(key, value, citation=None, cby="hamishgibbs"):

    return {
        "key": key,
        "value": value,
        "cby": cby,
        "ctime": datetime.timestamp(datetime.now()),
        "citation": citation,
        "modifications": []
    }


def modify_attribute(attribute, value, citation=None, mby="hamishgibbs"):

    old_value = attribute["value"]
    old_citation = attribute["citation"]

    attribute["value"] = value
    attribute["citation"] = citation

    attribute["modifications"].append(
        {
            "mtime": datetime.timestamp(datetime.now()),
            "mby": mby,
            "old_value": old_value,
            "old_citation": old_citation,
        }
    )

    return attribute

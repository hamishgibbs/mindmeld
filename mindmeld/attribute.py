from datetime import datetime


def create_attribute(key, value, source=None, cby="hamishgibbs"):

    return {
        "key": key,
        "value": value,
        "cby": cby,
        "ctime": datetime.timestamp(datetime.now()),
        "source": source,
        "modifications": []
    }


def modify_attribute(attribute, key, value, source=None, mby="hamishgibbs"):

    old_key = attribute["key"]
    old_value = attribute["value"]
    old_source = attribute["source"]

    attribute["key"] = key
    attribute["value"] = value
    attribute["source"] = source

    attribute["modifications"].append(
        {
            "mtime": datetime.timestamp(datetime.now()),
            "mby": mby,
            "old_key": old_key,
            "old_value": old_value,
            "old_source": old_source,
        }
    )

    return attribute

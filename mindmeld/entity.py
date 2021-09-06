import uuid


def _create_entity(attributes: list):

    return {
        "uuid": str(uuid.uuid4()),
        "attributes": attributes
    }

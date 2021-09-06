import uuid
from ..mindmeld import attribute


def create_object(title, **kwargs):

    return _create_object([
        attribute.create_attribute("title", title, **kwargs)
    ])


def _create_object(attributes: list):

    return {
        "uuid": str(uuid.uuid4()),
        "attributes": attributes
    }

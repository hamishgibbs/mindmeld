from ..mindmeld import attribute
from ..mindmeld import entity


def create_object(title, **kwargs):

    return entity._create_entity([
        attribute.create_attribute("title", title, **kwargs)
    ])

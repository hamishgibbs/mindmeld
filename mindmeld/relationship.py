from ..mindmeld import attribute
from ..mindmeld import entity


def create_relationship(relationship, source, target, **kwargs):

    return entity._create_entity([
        attribute.create_attribute("relationship", relationship, **kwargs),
        attribute.create_attribute("source", source, **kwargs),
        attribute.create_attribute("target", target, **kwargs)
    ])

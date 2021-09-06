# mindmeld

A place to collect your thoughts.

#### Basics

A temporal graph database to store and retrieve interconnected, evolving information with a dynamic, flexible ontology.

Hopefully, a brain for the facts you can't remember.

`mindmeld` is a custom knowledge graph (optionally interoperable). Designed to be deeply detailed but instantly usable.

The challenge - to categorise, store and interpret complex, interconnected, evolving data. For example, a description of [Zaifeng, Prince Chun](https://en.wikipedia.org/wiki/Zaifeng,_Prince_Chun):

``` {shell}
Prince Chun lived in the Northern Residence in Beijing until 1928. He spent most of his time in the library reading books on history and newly published magazines. Sometime after 1911, he married another wife, Lady Dengiya, with whom he had several children. His primary consort, Youlan, committed suicide in 1921 by swallowing opium after being publicly scolded by Dowager Consort Duankang (the highest-ranked woman in the imperial court after Empress Dowager Longyu's death in 1913) for the misconduct of her son, Puyi.
```

The approach - a graph database with three elements:

`objects`: the core storage for entities and concepts. (nodes in the graph).
`relationships`: connections between objects. (edges in the graph).
`attributes`: key value pairs describing nodes and edges.

But, there's more.

`Prince Chun lived in the Northern Residence`

When? According to whom?

`objects`, `relationships`, and `attributes` must be versioned and (optionally) sourced on each update.

### Attribute Structure

``` {shell}
{
  "key": "title",
  "value": "Zaifeng, Prince Chun",
  "ctime": 1,
  "cby": "hamishgibbs",
  "source": "https://en.wikipedia.org/wiki/Zaifeng,_Prince_Chun",
  "modifications": [
    # version history is retained for each key-value pair
    {
      "mtime": 2,
      "mby": "hamishgibbs",
      "old_key": "title",
      "old_value": "Prince Chun",
      "old_source": "https://en.wikipedia.org/wiki/Zaifeng,_Prince_Chun"
    },
    {
      ...
    }
  ]
}
```

### Object Structure

Objects MUST have one special attribute: `title`.

``` {shell}
{
    "uuid": "b5ca74a8-5559-4cd1-956d-efd0803745af",
    "attributes": [],
}
```

### Relationship Structure

Relationships MUST have three special attributes: `relationship` (i.e. lived), `source` (a uuid), `target` (a uuid).

``` {shell}
{
    "uuid": "b5ca74a8-5559-4cd1-956d-efd0803745af",
    "attributes": [],
}
```

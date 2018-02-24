# shapely-geojson
Feature and FeatureCollection to work nice with Shapely geometry structures and GeoJson.

## What?
* Feature & FeatureCollection classes as in [GeoJson spec](http://geojson.org/).
* dump & dumps functions as in json, to serialize your shapely geometries.

## Examples
Feature
```python
>>> from shapely.geometry import Point
>>> from shapely_geojson import dumps, Feature
>>> feature = Feature(Point(1, 2), properties={'key': 'value'})
>>> print(dumps(feature, indent=2))
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
      1.0,
      2.0
    ]
  },
  "properties": {
    "key": "value"
  }
}
```
FeatureCollection
```python
>>> feature1 = Feature(Point(1, 2), {'index': 1})
>>> feature2 = Feature(Point(3, 4), {'index': 2})
>>> features = [feature1, feature2]
>>> feature_collection = FeatureCollection(features)
>>> for feature in feature_collection:
...     print(feature.properties['index'])
...
1
2
>>> print(dumps(feature_collection, indent=2))
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          1.0,
          2.0
        ]
      },
      "properties": {
        "index": 1
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          3.0,
          4.0
        ]
      },
      "properties": {
        "index": 2
      }
    }
  ]
}

```

## Why?
I use shapely all the time and recently more frequently I use GeoJSON to show my data on maps. Main thing I was missing is fast way to create features and dump them on a geojson.

## Existing alternatives
You should also consider alternatives:
* [PyGeoIf](https://pypi.python.org/pypi/pygeoif/) provides a GeoJSON-like protocol for geo-spatial (GIS) vector data.
* [geojson](https://pypi.python.org/pypi/geojson) Python bindings and utilities for GeoJSON

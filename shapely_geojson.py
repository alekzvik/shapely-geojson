import json

from shapely.geometry import mapping
from shapely.geometry.base import BaseGeometry


class Feature():
    def __init__(self, geometry, properties=None):
        self.geometry = geometry
        self.properties = properties

    @property
    def geometry(self):
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        if not isinstance(geometry, BaseGeometry):
            raise ValueError('geometry must be a shapely geometry.')
        self._geometry = geometry

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        if properties is None:
            self._properties = {}
        elif isinstance(properties, dict):
            self._properties = properties
        else:
            raise ValueError('properties must be a dict.')

    @property
    def __geo_interface__(self):
        return {
            'type': 'Feature',
            'geometry': self.geometry.__geo_interface__,
            'properties': self.properties,
        }

    def __eq__(self, other):
        return self.__geo_interface__ == other.__geo_interface__


class FeatureCollection():
    def __init__(self, objects):
        self.features = objects

    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, objects):
        all_are_features = all(
            isinstance(feature, Feature)
            for feature in objects
        )
        if all_are_features:
            self._features = objects
        else:
            try:
                self._features = [
                    Feature(geometry)
                    for geometry in objects
                ]
            except ValueError:
                raise ValueError(
                    'features can be either a Feature or shapely geometry.')

    def __iter__(self):
        return iter(self.features)

    def geometries_iterator(self):
        for feature in self.features:
            yield feature.geometry

    @property
    def __geo_interface__(self):
        return {
            'type': 'FeatureCollection',
            'features': [
                feature.__geo_interface__
                for feature in self.features
            ],
        }

    def __eq__(self, other):
        return self.__geo_interface__ == other.__geo_interface__


def dump(obj, fp, *args, **kwargs):
    """Dump shapely geometry object :obj: to a file :fp:."""
    json.dump(mapping(obj), fp, *args, **kwargs)


def dumps(obj, *args, **kwargs):
    """Dump shapely geometry object :obj: to a string."""
    return json.dumps(mapping(obj), *args, **kwargs)

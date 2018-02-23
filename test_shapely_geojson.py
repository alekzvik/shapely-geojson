import io

import pytest

from shapely.geometry import Point

from shapely_geojson import dump, dumps, Feature, FeatureCollection


def test_dump():
    fp = io.StringIO()
    point = Point(1, 1)
    geojson = '{\n "type": "Point",\n "coordinates": [\n  1.0,\n  1.0\n ]\n}'
    with fp:
        dump(point, fp, indent=1)
        assert fp.getvalue() == geojson


def test_dumps():
    point = Point(1, 1)
    geojson = '{\n "type": "Point",\n "coordinates": [\n  1.0,\n  1.0\n ]\n}'
    assert dumps(point, indent=1) == geojson


class TestFeature():
    def test_invalid_properties(self):
        with pytest.raises(ValueError):
            Feature(Point(), properties=[])

    def test_default_properties(self):
        feature = Feature(Point())
        assert feature.properties == {}

    def test_invalid_geometry(self):
        with pytest.raises(ValueError):
            Feature([0, 1])

    def test_geo_interface(self):
        feature = Feature(Point(1, 1), properties={'key': 'value'})
        geo_interface = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': (1.0, 1.0),
            },
            'properties': {
                'key': 'value'
            },
        }
        assert feature.__geo_interface__ == geo_interface

    def test_equality(self):
        one = Feature(Point(1, 1))
        another = Feature(Point(1, 1))
        assert one == another


class TestFeatureCollection():
    def test_is_iterable(self):
        features = [Feature(Point(0, 0)), Feature(Point(0, 1))]
        collection = FeatureCollection(features)
        for collection_item, feature in zip(collection, features):
            assert collection_item == feature

    def test_geometries_iterator(self):
        points = [Point(0, 0), Point(0, 1)]
        features = list(map(Feature, points))
        collection = FeatureCollection(features)
        geometry_point_pairs = zip(collection.geometries_iterator(), points)
        for geometry, point in geometry_point_pairs:
            assert geometry == point

    def test_geometry_conversion(self):
        points = [Point(0, 0), Point(0, 1)]
        features = list(map(Feature, points))
        collection = FeatureCollection(points)
        for collection_item, feature in zip(collection, features):
            assert collection_item == feature

    def test_invalid_features(self):
        with pytest.raises(ValueError):
            FeatureCollection([[1, 2]])

    def test_equality(self):
        features = [Feature(Point(0, 0)), Feature(Point(0, 1))]
        one = FeatureCollection(features)
        another = FeatureCollection(features)
        assert one == another

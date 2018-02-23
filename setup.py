from codecs import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='shapely-geojson',
    version='0.0.1',
    author='Alex Vykaliuk',
    author_email='alekzvik@gmail.com',
    py_modules=['shapely_geojson'],
    url='https://github.com/alekzvik/shapely_geojson/',
    license='LICENSE',
    description='Feature and FeatureCollection for Shapely.',
    long_description=open('README.md').read(),
    install_requires=[
        'Shapely',
    ],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: GIS',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='shapely helpers geojson',
)
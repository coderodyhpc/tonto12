# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.

WRF_EARTH_RADIUS = 6370000
WRF_PROJ4_SPHERE = '+a={radius} +b={radius}'.format(radius=WRF_EARTH_RADIUS)

'''
v1:
Initial version
v2:
Add stand_lon to Lambert projections.
In v1, stand_lon was implicitly required to be identical to domain center longitude.
'''
PROJECT_JSON_VERSION = 1

# gdal forces us to provide names for categories starting from index 0.
# WRF's categories typically start at 1, so we need to add fake entries
# which we later filter out again from the palette when creating a QGIS raster layer.
UNUSED_CATEGORY_LABEL = '__UNUSED__'

# wrf-python/src/wrf/projection.py
class ProjectionTypes(object):
    LAMBERT_CONFORMAL = 1
    POLAR_STEREOGRAPHIC = 2
    MERCATOR = 3
    LAT_LON = 6

WRF_WPS_DIST_VERSION = '4.0'


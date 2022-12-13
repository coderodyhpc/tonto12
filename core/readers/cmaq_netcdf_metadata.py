# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.

from typing import List
import os

import netCDF4 as nc

from Gv3GEWRF.core.util import export

@export
def get_cmaq_nc_time_steps(path: str) -> List[str]:
    ds = nc.Dataset(path)
    try:
        steps = []
        # Each time step is stored as a sequence of 1-byte chars, e.g.:
        # array([b'2', b'0', b'0', b'5', b'-', b'0', b'8', b'-', b'2', b'8', b'_',
        #   b'0', b'0', b':', b'0', b'0', b':', b'0', b'0'],
        #  dtype='|S1')
        # ... which we convert to a plain string '2005-08-28_00:00:00'
        # and replace the underscore with a space: '2005-08-28 00:00:00'.
        for val in ds.variables['Times']:
            time = ''.join([c.decode() for c in val])
            time = time.replace('_', ' ')
            steps.append(time)
    finally:
        ds.close()
    return steps
  

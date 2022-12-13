# Gv3GEWRF 
# Copyright (c) Odycloud.

from typing import List
import os

import f90nml

from Gv3GEWRF.core.util import export
from Gv3GEWRF.core.readers.namelist import read_namelist
from Gv3GEWRF.core.logging import logger

@export
def write_namelist(namelist: dict, path: str) -> None:
    logger.info(f'writing namelist to {path}')
    nml = f90nml.Namelist(namelist)   # nml has the namelist content 
    nml.indent = 0
#    nml.write(path, force=True) #It seems to be failing here
    nml.write('/home/ubuntu/PREPRO/WPS/namelist.wps', force=True) # I manually modified this


def patch_namelist(path: str, patch: dict, delete_vars: List[str]=[]) -> None:
    logger.debug(f'patching {path}')
    nml = read_namelist(path)
    for group_name, group_patch in patch.items():
        if group_name not in nml:
            logger.debug(f'{path}: group {group_name} not found, inserting from patch')
            nml[group_name] = group_patch
            continue
        for var_name, val in group_patch.items():
            logger.debug(f'{path}: patching {group_name}/{var_name} = {val}')
            nml[group_name][var_name] = val
        for var_name in delete_vars:
            try:
                del nml[group_name][var_name]
                logger.debug(f'{path}: removing {group_name}/{var_name}')
            except KeyError:
                pass
    nml.indent = 2
    nml.write('/home/ubuntu/PREPRO/WPS/namelist.wps', force=True)

def patch_namelist2(path: str, patch: dict, delete_vars: List[str]=[]) -> None:
    logger.debug(f'patching {path}')
    nml = read_namelist(path)
    for group_name, group_patch in patch.items():
        if group_name not in nml:
            logger.debug(f'{path}: group {group_name} not found, inserting from patch')
            nml[group_name] = group_patch
            continue
        for var_name, val in group_patch.items():
            logger.debug(f'{path}: patching {group_name}/{var_name} = {val}')
            nml[group_name][var_name] = val
        for var_name in delete_vars:
            try:
                del nml[group_name][var_name]
                logger.debug(f'{path}: removing {group_name}/{var_name}')
            except KeyError:
                pass
    nml.indent = 2
    nml.write('/home/ubuntu/WRF-4.4/test/em_real/namelist.input', force=True)

# The following alternative patch_namelist implemention uses the f90nml.patch function
# which preserves formatting and comments of the input namelist.
# Due to a bug we can't use it currently, see https://github.com/marshallward/f90nml/issues/80
#def _patch_namelist(path: str, patch: dict, delete_vars: List[str]=None) -> None:
#    ''' Patch an existing namelist file, retaining any formatting and comments. '''
#    # f90nml does not create a patch file if the patch is empty

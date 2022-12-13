# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.

from collections import OrderedDict

from Gv3GEWRF.core.util import export
from Gv3GEWRF.core.project import Project

@export
def convert_project_to_wps_namelist(project: Project, puella) -> dict:
#    self.puella = puella
#    print ("convert_project_to_wps_namelist ", project, puella, puella.satus_dies, puella.satus_hora)

    wps = OrderedDict() # type: dict

    domains = project.data['domains']
    num_domains = len(domains)
    assert num_domains > 0
    innermost_domain = domains[0]
    outermost_domain = domains[-1]

    map_proj = innermost_domain['map_proj']

    def to_wrf_date(date):
        return date.strftime('%Y-%m-%d_%H:%M:%S')

    def conv_wps(diesWPS, horaWPS):
        nomen = diesWPS.strftime('%Y-%m-%d')+"_"+str(horaWPS).zfill(2)+":00:00"
#        print ("CONV-WPS ", date, diesWPS, num_domains)
        return nomen
    
    def tempus_to_output(servus):
        dateA = servus.satus_dies
        return dateA

    bellatorI = conv_wps(puella.satus_dies, puella.satus_hora)
    bellatorII = conv_wps(puella.finis_dies, puella.finis_hora)
    
    wps['share'] = OrderedDict(
        wrf_core = 'ARW',
        nocolons = True,
        max_dom = num_domains,
#        start_date = [puella.satus_dies] * num_domains,
#        end_date = [puella.finis_dies] * num_domains,
#        bellatorI = conv_wps(puella.satus_dies, puella.satus_hora) 
#        start_date = str(puella.satus_dies) * num_domains,
        start_date = [bellatorI] * num_domains,
        end_date = [bellatorII] * num_domains,
        interval_seconds = [puella.interval],
        io_form_geogrid = 2,
    )
#    try:
#        met_spec = project.met_dataset_spec
#    except KeyError:
#        pass
#    else:
#        wps['share'].update(
#            start_date = [puella.satus_dies] * num_domains,
#            end_date = [puella.finis_dies] * num_domains,
#            interval_seconds = met_spec['interval_seconds']
#         )

#            start_date = inicio * num_domains,
#            end_date = alfinal * num_domains,
#            interval_seconds = intervalo
#            start_date = [to_wrf_date(met_spec['time_range'][0])] * num_domains,
#            end_date = [to_wrf_date(met_spec['time_range'][1])] * num_domains,
#            interval_seconds = met_spec['interval_seconds']

    wps['geogrid'] = OrderedDict(
        parent_id = [1] + list(range(1, num_domains)),
        parent_grid_ratio = [1] + [domain['parent_cell_size_ratio'] for domain in domains[:0:-1]],
        i_parent_start = [domain['parent_start'][0] for domain in domains[::-1]],
        j_parent_start = [domain['parent_start'][1] for domain in domains[::-1]],
        # e_we and e_sn represent the number of velocity points (i.e., u-staggered or v-staggered points)
        # which is one more than the number of cells in each dimension.
        e_we = [domain['domain_size'][0] + domain['padding_left'] + domain['padding_right'] + 1 for domain in domains[::-1]],
        e_sn = [domain['domain_size'][1] + domain['padding_bottom'] + domain['padding_top'] + 1 for domain in domains[::-1]],
        map_proj = map_proj,
        dx = outermost_domain['cell_size'][0],
        dy = outermost_domain['cell_size'][1],
        ref_lon = outermost_domain['center_lonlat'][0],
        ref_lat = outermost_domain['center_lonlat'][1],
#        geog_data_res = project.geo_dataset_specs[::-1],
#        geog_data_path = geog_data_path
        geog_data_res = 'default',
        geog_data_path = '/home/ubuntu/WRF-4.4/WPS_GEOG' #! I'm changing this to a fixed location 
    )

    if map_proj in ['lambert', 'mercator', 'polar']:
        wps['geogrid']['truelat1'] = innermost_domain['truelat1']

    if map_proj == 'lambert':
        wps['geogrid']['truelat2'] = innermost_domain['truelat2']

    if map_proj in ['lambert', 'polar']:
        wps['geogrid']['stand_lon'] = innermost_domain['stand_lon']

    if map_proj == 'lat-lon':
        wps['geogrid']['stand_lon'] = innermost_domain['stand_lon'] # rotation
    #    wps['geogrid']['pole_lat'] = innermost_domain['pole_lat']
    #    wps['geogrid']['pole_lon'] = innermost_domain['pole_lon']

    wps['metgrid'] = OrderedDict(
        fg_name = ['FILE']
    )

    return wps

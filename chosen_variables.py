def chosen_variables(Variables_available):
    """Gives a string of the variables chosen by the user"""

    #Dictionary of variables
    Variable={'mean_sea_level_pressure': 151.128,
    'total_cloud_cover':164.128,
    'U_wind_10m':165.128,
    'V_wind_10m':166.128,
    '2m_temperature':167.128,
    '2m_dewpoint_temperature':168.128,
    'total_precipitation':228.128,
    'sea_surface_temperature':34.128}
    #Check what variables were chosen by the user and returns a string with
    #such variables
    temporal=[]
    for index in range(len(Variables_available)):
        temporal=[Variable[Variables_available[index]]] + temporal
    Chosen_var="/".join(map(str,list(temporal)))
    return Chosen_var




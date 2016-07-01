def chosen_area(location):
    """Gives a string with the geographic coordenates of the chosen area"""

    #Dictionary of stations with their respective associated coordenates
    all_locations={"urias":"23.25/253.5/23.125/253.625",
    "terminos":"18.75/268.125/18.5/268.625",
    "pto.morelos":"21/273.125/20.875/273.25",
    "sta.ma.oro":"21.375/255.375/21.25/255.5"
    }

    return str(all_locations[location])
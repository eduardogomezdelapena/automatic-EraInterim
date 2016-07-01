def retrieve_netcdf(Variables_available,monthlystr,namestr,location):
    """Retrieve NetCDF file"""
    from chosen_variables import chosen_variables
    from location import chosen_area
    from ecmwfapi import ECMWFDataServer
    server = ECMWFDataServer()
    server.retrieve({
        "class": "ei",
        "dataset": "interim",
        "date": monthlystr,
        "expver": "1",
        "grid": "0.125/0.125",
        "area": chosen_area(location),
        "levtype": "sfc",
        "param": chosen_variables(Variables_available),
        "step": "0",
        "stream": "oper",
        "target": namestr,
        "time": "00/06/12/18",
        "type": "an",
        'format'    : "netcdf"
        })
    server.retrieve({
        "class": "ei",
        "dataset": "interim",
        "date": monthlystr,
        "expver": "1",
        "grid": "0.125/0.125",
        "area": chosen_area(location),
        "levtype": "sfc",
        "param": chosen_variables(Variables_available),
        "step": "3/6/9/12",
        "stream": "oper",
        "target": namestr,
        "time": "00/12",
        "type": "fc",
        'format'    : "netcdf"
        })


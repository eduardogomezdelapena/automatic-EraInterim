# -*- coding: utf-8 -*-
def retrieve_monthly_netcdfs(location,output_folder,Variables_available,start,end):
    """Retrieves netcdf files month by month for all years involved"""
    months=("-01","-02","-03","-04","-05","-06","-07","-08","-09","-10","-11","-12")
    month_31={"January":"-01",
    "March":"-03","May":"-05","July":"-07","August":"-08",
    "October":"-10","December":"-12"}
    month_30={"April":"-04","June":"-06","September":"-09","November":"-11"}
    month_special={"February":"-02"}
    years=range(int(start),int(end)+1)

    from retrieve_netcdf import retrieve_netcdf
    import os
    os.chdir(output_folder)
    for year in years:
    #Cycle for months in a year
        for month in months:
            str1="-01/to/"
            #Conditions for determining month´s ending
            if month in month_31.values():
                str2="-31"
            elif month in month_30.values():
                    str2="-30"
            elif month in month_special.values():
                #int_year=int(year)
                if year%4==0:
                    str2="-29"
                else:
                    str2="-28"
            monthlystr= str(year)+month+str1+str(year)+month+str2
            namestr=location+".erainterim."+monthlystr[:4]+monthlystr[5:7]+".nc"
            retrieve_netcdf(Variables_available,monthlystr,namestr,location)
            del monthlystr
            del namestr

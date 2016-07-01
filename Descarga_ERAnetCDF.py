#Este programa descarga archivos netCDF mensuales del
#reanalisis ERA-Interim de la estacion especificada

#Especificar carpeta donde se descargaran los archivos
output_folder = '/media/sf_PRUEBA_share/Sta.Maria'
#Bases_datos/'
#Elegir la estacion
location = "sta.ma.oro"  # "urias" #"terminos"

#Comentar las variables que NO se quieran descargar
Variables_available = ("mean_sea_level_pressure",
                            "total_cloud_cover",
                            "U_wind_10m",
                            "V_wind_10m",
                            "2m_temperature",
                            "2m_dewpoint_temperature",
                            "total_precipitation",
                            "sea_surface_temperature")
start = "2005"  # Anio inicial
end = "2015"   # Anio final

from retrieve_monthly_netcdfs import retrieve_monthly_netcdfs
retrieve_monthly_netcdfs(location,
output_folder,Variables_available, start, end)
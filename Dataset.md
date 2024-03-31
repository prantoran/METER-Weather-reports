# Dataset

'''
This module provides functionality to download weather data from specified networks and stations
and save it in Google Cloud Storage in Parquet format.

The downloaded data is saved in the data directory, with a subdirectory 
for each network and station containing a Parquet file with the name of the station:

/data/<network_name>/<station_name>/<station_name>.parquet
'''

```python

# https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=EPKK&data=all&year1=2023&month1=1&day1=1&year2=2023&month2=3&day2=26&tz=Etc%2FUTC&format=onlycomma&latlon=no&elev=no&missing=null&trace=T&direct=no&report_type=3&report_type=4
# France Hungary Poland Germany Spain Greece Italy  Austria United Kingdom

```

ICAO codes for Canada: https://en.wikipedia.org/wiki/List_of_airports_by_ICAO_code:_C


Abbreviations:
- http://www.moratech.com/aviation/metaf-abbrev.html

IEM network:
- https://mesonet.agron.iastate.edu/request/download.phtml
- https://mesonet.agron.iastate.edu/sites/networks.php?network=GH__ASOS


Sample output from `https://mesonet.agron.iastate.edu/sites/networks.php?network=CA_ASOS&format=csv&nohtml=on`:

```bash
                              0                   1

stid                        AAT                 ACV   
station_name  ALTURAS (WAS O00)  ARCATA/EUREKA ARPT   
lat                    41.49139            40.97811   
lon                  -120.56444          -124.10861   
elev                     1333.0                66.0   
begints        1983-11-03 00:00    1949-12-01 00:00   
endts                       NaN                 NaN   
iem_network             CA_ASOS             CA_ASOS   
```
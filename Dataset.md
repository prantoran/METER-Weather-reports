# Dataset

We will make API calls and save data to GCS buckets using parquey format with the following file path: `<network_name>/<station_name>/<station_name>.parquet`.

Here is a sample API call:
```python
https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=EPKK&data=all&year1=2023&month1=1&day1=1&year2=2023&month2=3&day2=26&tz=Etc%2FUTC&format=onlycomma&latlon=no&elev=no&missing=null&trace=T&direct=no&report_type=3&report_type=4
```

ICAO codes for Canada: https://en.wikipedia.org/wiki/List_of_airports_by_ICAO_code:_C

Abbreviations:
- http://www.moratech.com/aviation/metaf-abbrev.html

IEM network:
- https://mesonet.agron.iastate.edu/request/download.phtml
- https://mesonet.agron.iastate.edu/sites/networks.php?network=GH__ASOS


Sample output from `https://mesonet.agron.iastate.edu/sites/networks.php?network=CA_BC_ASOS&format=csv&nohtml=on`:

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
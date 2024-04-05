# Dataset
An ordinary METAR report is issued hourly unless significant weather changes have occurred. For terminology, METAR refers to the type of report issued hourly and a SPECI refers to the type issued during special circumstances.

[ICAO codes for Canada](https://en.wikipedia.org/wiki/List_of_airports_by_ICAO_code:_C).

The raw records from the API calls contain [abbreviations](http://www.moratech.com/aviation/metaf-abbrev.html) related to METER and TAF weather reports. 
 

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

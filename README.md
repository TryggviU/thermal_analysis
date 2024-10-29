# Thermal analysis with MODIS spectral radiance data

To run the code, open the Anaconda Prompt terminal and execute the following lines:

```
> conda activate earthdata
```


```
> python download_modis.py -n VOLCANO_NAME -b LON_MIN LAT_MIN LON_MAX LAT_MAX  -t START_DATE END_DATE -d DOWNLOAD_DIRECTORY
```

| Variable | Input example |
|----------|---------------|
| `VOLCANO_NAME`| Redoubt |
| `LON_MIN` `LAT_MIN`... | -152.2 64.2 ... |
| `START_DATE` `END_DATE` | "2024-06-17" "2024-06-18" |
| `DOWNLOAD_DIRECTORY` | "C:\\Users\\USER\\Downloads\Redoubt" |

Note that if you only want a single date then `START_DATE` and  `END_DATE` must be the same.

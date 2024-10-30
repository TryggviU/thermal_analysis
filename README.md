# Thermal analysis with MODIS spectral radiance data

## Important information

The code in this repository is presented "as is" without warranty of any kind.

## Running the code

For the first time you plan to use the code, open the Anaconda Prompt terminal and execute these lines:
```
> conda create --name earthdata
> conda activate earthdata
> conda install -c conda-forge earthaccess
```
Download the [download_modis.py](../src/download_modis.py) script. It does not really matter where you store the script on your computer.

To run the code after the first time, you will only need to activate the environment:
```
> conda activate earthdata
```

 and locate it in the terminal window. Downloading the MODIS data is then fairly straight forward:

```
> python download_modis.py -n VOLCANO_NAME -b LON_MIN LAT_MIN LON_MAX LAT_MAX  -t START_DATE END_DATE -d DOWNLOAD_DIRECTORY
```

| Variable | Input example |
|----------|---------------|
| `VOLCANO_NAME`| `Spurr` |
| `LON_MIN` `LAT_MIN` `LON_MAX` `LAT_MAX` | `-152.2` `61.2` `-152.1` `61.4` |
| `START_DATE` `END_DATE` | `2024-06-17` `2024-06-18` |
| `DOWNLOAD_DIRECTORY` | `"C:\Users\USER\Downloads\Spurr"` |

Note that if you only want a single date then `START_DATE` and  `END_DATE` must be the same.

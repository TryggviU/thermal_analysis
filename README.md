# Thermal analysis of volcanoes with MODIS spectral radiance data

## Important information

The code in this repository is presented "as is" without warranty of any kind. See the [LICENCE](/LICENSE) file for further information.

Users must first acquire [NASA EarthData](https://www.earthdata.nasa.gov/) login credentials before using the code.

The code relies on the [earthaccess](https://github.com/nsidc/earthaccess) Python package to search for and download [MODIS](https://modis.gsfc.nasa.gov/) data to use for the volcano thermal analysis presented in [Girona et al. (2021)](https://doi.org/10.1038/s41561-021-00705-4). The code is further designed to adhere to the storage structure system of [Girona et al. (2021)](https://doi.org/10.1038/s41561-021-00705-4), so it may require some changing for other applications.

___
### !!! WARNING !!!

* Downloading satellite data to a personal hard drive can be storage intensive and it is not recommended for larger data suites.
* The code here does not check for erroneous inputs or storage requirements - ALWAYS DOUBLE-CHECK BEFORE EXECUTING DOWNLOADS!
* Test the code for short timespans first before committing to large scale downloads.
___

## Running the code

For the first time you plan to use the code, open the Anaconda Prompt terminal and execute these lines to create a virtual environment (named `earthdata` here) that will store the necessary python packages:
```
> conda create --name earthdata
> conda activate earthdata
> conda install -c conda-forge earthaccess
```
Download the [download_modis.py](src/download_modis.py) script. It does not really matter where you store the script on your computer.

To run the code for subsequent times, you will only need to activate the virtual environment:
```
> conda activate earthdata
```

Downloading the MODIS data is then fairly straight forward:

```
> python download_modis.py -n VOLCANO_NAME -b LON_MIN LAT_MIN LON_MAX LAT_MAX  -t START_DATE END_DATE -d DOWNLOAD_DIRECTORY
```
> It may occur that some files will not download for various reasons.

1. If multiple files failed to download - rerun the above script.
2. If only several files (<100) failed to download - continue on to below instructions.

To retry downloading the missing files execute the following script:
```
> python download_missing_modis.py -n VOLCANO_NAME -b LON_MIN LAT_MIN LON_MAX LAT_MAX  -t START_DATE END_DATE -d DOWNLOAD_DIRECTORY
```

| Variable | Input example |
|----------|---------------|
| `VOLCANO_NAME`| `Spurr` |
| `LON_MIN` `LAT_MIN` `LON_MAX` `LAT_MAX` | `-152.2` `61.2` `-152.1` `61.4` |
| `START_DATE` `END_DATE`[^1] | `2024-06-17` `2024-06-18` |
| `DOWNLOAD_DIRECTORY` | `"C:\Users\USER\Downloads\Spurr"`[^2] |

[^1]: Note that if you only want a single date then `START_DATE` and  `END_DATE` must be the same.
[^2]: I recommend using quotation marks around the path to the desired download directory, especially if the path contains whitespaces.

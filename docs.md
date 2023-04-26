## Convertir un jeu de données netCDF en format Zarr et l'afficher avec MapLibre

### 1. Installer les packages Python nécessaires

Il est nécessaire de d'installer les librairies `xarray`, `zarr` et `netCDF4` pour la conversion.

``` bash
pip install xarray zarr netCDF4
```

### 2. Convertir netCDF en Zarr

Appeler `convert_nc_to_zarr.py` dans `/utils/` et appelez également l'argument CLI (`input`). Exemple:
``` bash
python3 convert_nc_to_zarr.py -i EM3
```

Cela va chercher le fichier NetCDF `/data/input/EM3.nc` et va l'enregistrer en zarr sous `/data/output/`.

### 3. Suite...

[GeoTiff JS](https://geotiffjs.github.io/geotiff.js/)
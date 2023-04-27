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

### 3. Tiling, où j'en suis...

``` bash
python3 tiling.py -i 3D
```
```
>>> Zarr dataset opened
    <xarray.Dataset>
    Dimensions:  (YC: 196, XC: 560, time: 121, Z: 50, XG: 560, YG: 196, Zl: 50,
                Zp1: 51, Zu: 50)
    Coordinates: (12/14)
        Depth    (YC, XC) float32 ...
    * XC       (XC) float32 56.5 169.5 282.5 395.5 ... 6.3e+04 6.311e+04 6.322e+04
    * XG       (XG) float32 0.0 113.0 226.0 ... 6.294e+04 6.305e+04 6.317e+04
    * YC       (YC) float32 56.5 169.5 282.5 ... 2.187e+04 2.198e+04 2.209e+04
    * YG       (YG) float32 0.0 113.0 226.0 ... 2.181e+04 2.192e+04 2.204e+04
    * Z        (Z) float32 -0.15 -0.57 -1.23 -2.13 ... -267.9 -279.3 -291.0 -303.0
        ...       ...
    * Zu       (Zu) float32 -0.3 -0.84 -1.62 -2.64 ... -273.5 -285.1 -296.9 -309.0
        hFacC    (Z, YC, XC) float32 ...
        hFacS    (Z, YG, XC) float32 ...
        hFacW    (Z, YC, XG) float32 ...
        iter     (time) int64 ...
    * time     (time) timedelta64[ns] 17544 days 00:00:00 ... 17559 days 00:00:00
    Data variables:
        THETA    (time, Z, YC, XC) float32 ...
        UVEL     (time, Z, YC, XG) float32 ...
        VVEL     (time, Z, YG, XC) float32 ...
        WVEL     (time, Zl, YC, XC) float32 ...
    Attributes:
        MITgcm_version:  checkpoint67g
        Zl     YC     XC     Depth    iter       time      WVEL                     geometry
    0 -0.3   56.5   56.5  6.730265  864000 17544 days -0.000050    POINT (56.50000 56.50000)
    1 -0.3   56.5  169.5  7.536000  864000 17544 days -0.000032   POINT (169.50000 56.50000)
    2 -0.3   56.5  282.5  7.989007  864000 17544 days -0.000027   POINT (282.50000 56.50000)
    3 -0.3  169.5   56.5  7.710030  864000 17544 days -0.000026   POINT (56.50000 169.50000)
    4 -0.3  169.5  169.5  8.000000  864000 17544 days -0.000006  POINT (169.50000 169.50000)
````

### 4. Suite....

Passer par `martin` n'est pas une bonne idée car il faut suivre les étapes suivantes:
1. Install `PostgreSQL` with `PostGIS` extension.
2. Create a new database and enable the `PostGIS` extension.
Convert your `Zarr` dataset to a `GeoDataFrame` (similar to
what we did earlier).
1. Import the `GeoDataFrame` into the `PostGIS` database.
2. Install and configure `Martin` to serve vector tiles from the `PostGIS` database.

Et il est dommage de devoir reconvertir Zarr vers un dataframe... Au lieu, il faut se pencher sérieusement sur [@carbon/map](https://github.com/carbonplan/maps).
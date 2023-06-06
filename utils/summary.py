import rasterio
from rasterio.transform import from_origin
import xarray as xr
import os

crs = 'EPSG:4326'
file = "3D"
# file = "ME3"

ds = xr.open_dataset(f'../data/input/{file}.nc')


# Define the georeferencing transform.
# This will depend on the resolution of your data.
transform = from_origin(ds.XC.min(), ds.YC.max(), 1, 1)

# Loop over all the variables in the dataset.
for var_name, variable in ds.data_vars.items():

    os.makedirs(f"../data/other/{var_name}", exist_ok=True)

    for i in range(len(ds['time'])):

        if var_name == "THETA":
            for j in range(len(ds['Zl'])):  # use 'Z' instead of 'depth'
                # use 'Z' instead of 'depth'
                slice = variable.isel(time=i, Zl=j)
                # consider correct resolution
                transform = from_origin(ds['XC'].min(), ds['YC'].max(), 1, 1)
                output_file = f"../data/data/{var_name}/{i}_{j}.tif"
                with rasterio.open(output_file, 'w', driver='GTiff', height=slice.shape[0],
                                   width=slice.shape[1], count=1, dtype='float32',
                                   crs=crs, transform=transform) as dst:
                    dst.write(slice.data, 1)

        else:
            for j in range(len(ds['Zl'])):  # use 'Z' instead of 'depth'
                # use 'Z' instead of 'depth'
                slice = variable.isel(time=i, Zl=j)
                # consider correct resolution
                transform = from_origin(ds['XC'].min(), ds['YC'].max(), 1, 1)
                output_file = f"../data/data/{var_name}/{i}_{j}.tif"
                with rasterio.open(output_file, 'w', driver='GTiff', height=slice.shape[0],
                                   width=slice.shape[1], count=1, dtype='float32',
                                   crs=crs, transform=transform) as dst:
                    dst.write(slice.data, 1)

    print(f"{var_name}\t{i} - {j}\tdone")

    # for time in ds['time']:
    #     for z in ds['Z']:  # use 'Z' instead of 'depth'
    #         print(f"{var_name}\n\n{time.values}\n\n{z.values}")

# Import dependencies
import xarray as xr
import geopandas as gpd
from shapely.geometry import Point
from absl import app, flags
import os
import pandas as pd

# Define the flags and mark them as required
flags.DEFINE_string('input', None, 'Input (string)', short_name='i')
flags.DEFINE_integer('chunk', 1000, 'Chunk Size (integer)', short_name='c')

flags.mark_flag_as_required('input')
# flags.mark_flag_as_required('chunk')

FLAGS = flags.FLAGS


def tile(input_name: str = "ME3", chunk_size: int = 1000):
    inpt_path = f"../data/zarr/{input_name}.zarr"
    geodf_out = f"../data/geodataframe/{input_name}."
    dataf_out = f"../data/dataframe/{input_name}."

    # We'd like the read data in Januray 2019
    time_period = pd.date_range('2018-01-01', '2018-01-31')
    # Open Zarr
    ds = xr.open_zarr(inpt_path)
    print("Zarr dataset opened")
    print(ds)

    subset = ds['WVEL'].sel(time='17544 days', Zl=slice(-0.15, -2.13),
                            YC=slice(56.5, 282.5), XC=slice(56.5, 282.5))

    # Display the subset
    # Convert the subset to a Pandas DataFrame
    subset_df = subset.to_dataframe().reset_index()

    # Create a 'geometry' column using the coordinates from the DataFrame
    subset_df['geometry'] = subset_df.apply(
        lambda row: Point(row['XC'], row['YC']), axis=1)

    # Convert the DataFrame to a GeoDataFrame
    subset_gdf = gpd.GeoDataFrame(
        subset_df, geometry='geometry', crs="EPSG:4326")

    # Display the GeoDataFrame
    print(subset_gdf.head())
    # # Convert the Zarr data to a pandas DataFrame
    # try:
    #     df = z.to_dataframe().reset_index()

    # except ValueError:
    #     print("/!\ Iterator is too large, conversion to DF will be chunked.")

    #     # Determine which index columns has the largest dimension
    #     key_val = [(dim, len(z.coords[dim])) for dim in list(z.dims.keys())]
    #     max_len = max(key_val, key=lambda x: x[1])[1]
    #     for i in range(0, max_len, chunk_size):
    #         print(i)
    #     df = ds.isel(index=slice(i, i + chunk_size))
    #     print(i)
    # df = df.to_dataframe().reset_index()
    # print(df.head())
    # df_chunk['geometry'] = df_chunk.apply(create_point, axis=1)
    # gdf_chunk = gpd.GeoDataFrame(
    #     df_chunk, geometry='geometry', crs='EPSG:4326')

    # # Save the GeoJSON file
    # if i == 0:
    #     gdf_chunk.to_file(geodf_out, driver='GeoJSON')
    # else:
    #     gdf_chunk.to_file(geodf_out, driver='GeoJSON', mode='a')

    # print("Dataset converted to DataFrame")
    # print(df.head())
    # print(df.columns)
    # print(df.dtypes)

    # # Define a function to create a Point geometry from latitude and longitude

    # def create_point(row):
    #     return Point(row['longitude'], row['latitude'])

    # # Apply the function to create a new column in the DataFrame with Point geometries
    # df['geometry'] = df.apply(create_point, axis=1)

    # # Convert the pandas DataFrame to a GeoDataFrame
    # gdf = gpd.GeoDataFrame(df, geometry='geometry', crs='EPSG:4326')

    # # Save the GeoDataFrame as a GeoJSON file
    # gdf.to_file(out, driver='GeoJSON')

    # print("Successfully converted .zarr to GeoJSON")


def main(argv):
    input_name = FLAGS.input
    chunk_size = FLAGS.chunk
    tile(input_name, chunk_size)


if __name__ == '__main__':
    app.run(main)

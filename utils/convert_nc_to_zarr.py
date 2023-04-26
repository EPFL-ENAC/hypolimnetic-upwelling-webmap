# Import dependencies
import xarray as xr
from absl import app, flags

# Define the flags and mark them as required
flags.DEFINE_string('input', None, 'Input (string)', short_name='i')
flags.mark_flag_as_required('input')

FLAGS = flags.FLAGS


def convert_nc_to_zarr(input_nc, output_zarr):
    ds = xr.open_dataset(input_nc)
    ds.to_zarr(output_zarr, mode='w')
    print(f"Converted {input_nc} to {output_zarr}")


def main(argv):
    name = FLAGS.input
    input_nc = f'../data/input/{name}.nc'
    output_zarr = f'../data/output/{name}.zarr'
    convert_nc_to_zarr(input_nc, output_zarr)


if __name__ == '__main__':
    app.run(main)

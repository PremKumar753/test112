import rasterio

file_path = "classified_inundation.tif"

with rasterio.open(file_path) as src:
    crs = src.crs
    if crs:
        print("EPSG Code:", crs.to_epsg())
    else:
        print("No CRS information found0000.")

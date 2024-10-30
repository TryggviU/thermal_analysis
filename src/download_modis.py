import os
import argparse
import earthaccess

# Initiate the argument parser.
parser = argparse.ArgumentParser()
# Add arguments.
parser.add_argument("-n", "--name", action="store", type=str, required=True,
                    help="The volcano name.")
parser.add_argument("-b", "--bbox", action="store", nargs=4, type=float, required=True,
                    help="The bounding box coordinates lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat.")
parser.add_argument("-t", "--temp", action="store", nargs=2, type=str, required=True,
                    help="The start and end times as YYYY-MM-DD.")
parser.add_argument("-d", "--dir", action="store", type=str, required=True,
                    help="The download destination directory.")
# Read arguments from the command line
args = parser.parse_args()
args.bbox = tuple(args.bbox)
args.temp = tuple(args.temp)

products = {
	"MOD021KM": f"MODIS_Level_1B_{args.name}_Terra",
	"MYD021KM": f"MODIS_Level_1B_{args.name}_Aqua",
	"MOD03": f"MODIS_Geolocation_{args.name}_Terra",
	"MYD03": f"MODIS_Geolocation_{args.name}_Aqua",
	"MOD35_L2": f"MODIS_Cloud_mask_{args.name}_Terra",
	"MYD35_L2": f"MODIS_Cloud_mask_{args.name}_Aqua",
}

# Provide the user's credentials.
earthaccess.login()


def download_product(product, dir_download, bounding_box=args.bbox, temporal=args.temp, count=-1):
    if not os.path.exists(dir_download):
        os.mkdir(dir_download)
    
    results = earthaccess.search_data(
        short_name=product,
        bounding_box=bounding_box,
        temporal=temporal,
        count=count
    )
    
    earthaccess.download(
        granules=results,
        local_path=dir_download
    )
    

def main():
    for product in products:
        print(product)
        
        download_product(
            product=product,
            dir_download=os.path.join(args.dir, products[product])
        )
        

if __name__ == "__main__":
    main()

import os
import argparse
import earthaccess

# Initiate the argument parser.
parser = argparse.ArgumentParser()
# Add arguments.
parser.add_argument("-n", "--name", action="store", type=str, required=True,
                    help="The volcano name.")
parser.add_argument("-b", "--bbox", action="store", nargs=4, type=float, required=True,
                    help="The bounding box coordinates low_left_lon, low_left_lat, up_right_lon, up_right_lat.")
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


def find_missing_products(product, dir_download, bounding_box=args.bbox, temporal=args.temp, count=-1):
    if not os.path.exists(dir_download):
        os.mkdir(dir_download)

    # Find all MODIS products within the timeframe.
    results = earthaccess.search_data(
        short_name=product,
        bounding_box=bounding_box,
        temporal=temporal,
        count=count
    )

    # List of all currently downloaded products.
    file_list = os.listdir(dir_download)

    i = 0
    while i < len(results):
        if os.path.basename(results[i].data_links()[0]) in file_list:
            results.pop(i)  # Remove products from list that are already downloaded.
        else:
            print(" - ", os.path.basename(results[i].data_links()[0]))
            i += 1

    return results


def main():
    results = {key: [] for key in products.keys()}

    s = 0
    for product in products:
        print(product)

        results[product] = find_missing_products(
            product=product,
            dir_download=os.path.join(args.dir, products[product])
        )

        if not results[product]:
            results.pop(product)
        else:
            s += len(results[product])

    print()
    if s == 0:
        print("No missing scenes found.")
        return

    # Download the products with user's approval.
    if input(f"Submit {s} downloads (yes/no):").lower() == "yes":

        # Provide the user's credentials.
        earthaccess.login()

        for product in results:
            earthaccess.download(
                granules=results[product],
                local_path=os.path.join(args.dir, products[product])
            )
    else:
        print("Download halted by user.")


if __name__ == "__main__":
    main()

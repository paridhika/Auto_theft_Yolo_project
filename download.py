from bing_image_downloader import downloader

# Set the search query
query = "car theft detection"

# Set the number of images to download
limit = 100

# Set the output directory
output_dir = "Car Theft Project"

# Download the images
downloader.download(query, limit=limit, output_dir=output_dir, adult_filter_off=True)

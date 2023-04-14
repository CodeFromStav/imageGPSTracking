from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Open the image
img_path = "/home/stavros/Documents/vsCode/gpsTracker/test01.JPG"
with open(img_path, "rb") as f:
    img = Image.open(f)

# Get Exif Data
exif_data = img.getexif()

# Extract GPS coordinates
gps_data = exif_data.get(34853)  # 34853 is the tag ID for GPSInfo

if gps_data is not None:
    gps_info = {}
    for key in gps_data:
        sub_decoded = GPSTAGS.get(key, key)
        gps_info[sub_decoded] = gps_data[key]
        
    lat = gps_info.get('GPSLatitude')
    lat_ref = gps_info.get('GPSLatitudeRef')
    lon = gps_info.get('GPSLongitude')
    lon_ref = gps_info.get('GPSLongitudeRef')
    
    if lat and lat_ref and lon and lon_ref:
        lat_dec = lat[0] + lat[1] / 60 + lat[2] / 3600
        lon_dec = lon[0] + lon[1] / 60 + lon[2] / 3600
        if lat_ref == 'S':
            lat_dec *= -1
        if lon_ref == 'W':
            lon_dec *= -1
        print(f"Latitude: {lat_dec}, Longitude: {lon_dec}")
    else:
        print("No GPS coordinates found in the image metadata.")
else:
    print("No GPS data found in the image metadata.")

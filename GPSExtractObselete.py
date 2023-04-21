from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# GPS Latitude: 33 deg 9' 43.11" N
# GPS Longitude: 117 deg 21' 3.37" W

GPSINFO_TAG = next( tag for tag, name in TAGS.items() if name == "GPSInfo")

img_path = "/home/stavros/Documents/vsCode/gpsTracker/test02.JPG"
with open(img_path, "rb") as f:
    img = Image.open(f)
    img_exif_data = img.getexif()
    # print(img_exif_data)

gps_info = img_exif_data.get_ifd(GPSINFO_TAG)

# print(gps_info)

#Prints EXIF DATA for viewing
# print("EXIF DATA PRINT START\n")
# for key in sorted(img_exif_data):
#     print(str(key) + ": " + str(img_exif_data[key]))
#     # print(img_exif_data[key])
# print("EXIF DATA PRINT END\n")


#define function to convert GPS coords to decimal degrees
#(degrees, minutes, seconds) - Format for each Lat & Long
def convert_to_degrees(value):
    degrees = value[0] + value[1]/60 + value[2]/3600
    return degrees 

#adjust the decimal coordinates to (-) vaues if South or West
def adjust_coordinates(coord, ref):
    decimal = convert_to_degrees(coord)
    if ref in ['S','W']:
        decimal = -decimal
    return decimal
    
#main function
def extract_gps_data(exif_data):

    # gps_data = exif_data.get('GPSInfo', None)
    # gps_data = exif_data.get('GPSInfo', None)
    # print("gps_data: ", gps_data)
    print(exif_data)

    if not gps_data:
        print("No gps_data")
        return None
    
    #Converts integercodes to human readable tag names.
    gps_info = {GPSTAGS.get(tag, tag): value for tag, value in gps_data.items()} #***** I DONT KNOW IF THIS IS NECESSARY
    print("gps_info: ", gps_info)
    
    #convers lat and long to degrees format
    lat = convert_to_degrees(gps_info['GPSLatitude'])
    lon = convert_to_degrees(gps_info['GPSLongitude'])
    lat_ref = gps_info['GPSLatitudeRef']
    lon_ref = gps_info['GPSLongitudeRef']
    print(lat_ref)
    print("test")
    
    return adjust_coordinates(lat,lat_ref), adjust_coordinates(lon,lon_ref)

#calling main function to execute
gps_data = extract_gps_data(gps_info)
if gps_data:
    lat,lon = gps_data
    print("Latitude: ", lat)
    print("Longitude: ", lon)
    
else:
    print("No GPS data found.")
    
    

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


#Open the image
img = Image.open("C:/Users/stavt/Documents/VSCode/GPSPoint/img.jpg")
# Get Exif Data
exif_data = img.getexif()

for key in sorted(exif_data):
    print(str(key) + ": " + str(exif_data[key]))

#define function to convert GPS coords to decimal degrees
def convert_to_degrees(value):
    degrees = value[0] + value[1]/60 + value[2]/3600
    return degrees 

#adjust the decimal coordinates to (-) vaues if South or West
def adjust_coordinates(coord, ref):
    decimal = convert_to_degrees(coord)
    if ref in ['S','W']:
        decimal = -decimal
    return decimal
    
#
def extract_gps_data(exif_data):
    gps_data = exif_data.get('GPSInfo', None)
    # print(gps_data)
    if not gps_data:
        print("No gps_data")
        return None
    
    #Converts integercodes to human readable tag names.
    gps_info = {GPSTAGS.get(tag, tag): value for tag, value in gps_data.items()}
    
    lat = convert_to_degrees(gps_info['GPSLatitude'])
    lon = convert_to_degrees(gps_info['GPSLongitude'])
    lat_ref = gps_info['GPSLatitudeRef']
    lon_ref = gps_info['GPSLongitudeRef']
    print(lat_ref)
    print("test")
    
    return adjust_coordinates(lat,lat_ref), adjust_coordinates(lon,lon_ref)

gps_data = extract_gps_data(exif_data)
if gps_data:
    lat,lon = gps_data
    print("Latitude: ", lat)
    print("Longitude: ", lon)
    
else:
    print("No GPS data found.")
    
    

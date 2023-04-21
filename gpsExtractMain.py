from exif import Image
# import PIL

image_path = '/home/stavros/Documents/vsCode/gpsTracker/test01.JPG'

#Helper Function
def convert_to_degrees( value, ref ):
    degrees = value[0] + value[1]/60 + value[2]/3600
    if ref == "W" or ref == "S":
        degrees = -degrees
    return degrees 

#Main Function
def extract_gps_data( img_path ):
    with open( image_path, 'rb') as src:
        image = Image( src )
    if image.has_exif:
        try:
            #'try' to access gps_longitude of image. If DNE, move to 'except' block
            image.gps_longitude

            #calls function to convert tuple to descimal and cardinal direction to +/- 
            coords = (
                      convert_to_degrees(image.gps_latitude, image.gps_latitude_ref),
                      convert_to_degrees(image.gps_longitude, image.gps_longitude_ref)
                     )

        except AttributeError:
            print( "No Coordinates" )
    else:
        print( "The Image has no EXIF info" )
    
    print( f"Image {src.name}, OS Version:{image.get('software', 'Not Known')} ------" )
    print( f"Was taken: {image.datetime_original}, and has coordinates:{coords}" )

extract_gps_data(image_path)
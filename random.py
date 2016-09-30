import Image
import PIL
import matplotlib

def main( ):

    filename = "hinata.jpg";

    image_one = Image.open( filename )
    size = width, height = image_one.size;
    # image_one.thumbnail((100, 100));
    #print list(image_one.getcolors());
    #print list(image_one.getdata());
    # image_one.save("modified_" + filename_one)
    del image_one;


if ( __name__ == "__main__" ):

    main();

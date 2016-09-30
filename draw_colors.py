import Image
import ImageDraw

#purpose of function is to take an image, count up pixels and then draw
#rectangles of high count colors
#numColors is how many colors to draw
#swatchSize is length of rectangles

def draw_colors(input, output, numColors, swatchSize):

    image = Image.open(input);
    result = image.convert("P", palette=Image.ADAPTIVE, colors=numColors);
    result.putalpha(1);
    colors = result.getcolors(); #dict of (count, colors)
    #next goal: find percentage of dominance and use that has width
    #when drawing the rectangles

    #create new image, palette = rgb, size = (width*numColors, width)
    newImage = Image.new("RGB", (swatchSize*numColors, swatchSize));

    draw = ImageDraw.Draw(newImage);

    x = 0
    for count, color in colors:
        draw.rectangle([x, 0, x+swatchSize, swatchSize], fill=color, outline=color);
        x += swatchSize;

    newImage.save(output, "PNG");

if __name__ == '__main__':
    draw_colors("hinata.jpg", "output", 10, 100)

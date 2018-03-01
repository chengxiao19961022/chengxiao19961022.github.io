from PIL import  Image

imageDirectory = ""
imageSize = [16,32]

def createImage(size):
    im = Image.open(imageDirectory+"favicon.png")
    im.resize((size,size), Image.ANTIALIAS).save(imageDirectory+"icon%dx%d.png"%(size,size))

def start():
    for size in imageSize:
       createImage(size)

if __name__ == "__main__":
    start()
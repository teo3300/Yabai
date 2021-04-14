# frame size is 240 * 160 = 34240
# max pixel position is 34240 * 6575 = 22512800
# BAE: describe every line of pixel with its length until first different color pixel
# using 8 bit to represent line
# assuming no color switch on frame change by default (if color changes -> first byte of frame is 0)
# 0         : invert color (sequence of 0 pixels)
# 1 - 247   : number of pixels (single scanline is 240 pixels wide) (240 is a full line)
# 248       : 2 lines
# 249       : 4 lines
# 250       : 8 lines
# 251       : 16 lines
# 252       : 32 lines
# 253       : 64 lines
# 254       : fill until frame end
# 255       : do nothing (dead frame)

# macro for packing
frameSize = 240*160
black = 0
white = 1

def imp(filePath, fileName, ext):
    from PIL import Image
    im              = Image.open(filePath + fileName +"."+ ext) # open image file
    pixels          = list(im.getdata())                        # extract pixel data
    width, height   = im.size                                   # get image size
    return(width, height, pixels)

def printSize(img):
    print("Width:", img[0],", Height:",img[1])

def poster(img, threshold=128):
    width, height, pixels = img
    out = []
    for pixel in pixels:        # values from 0 to 255
        if(pixel < threshold):
            out.append(0)
        else:
            out.append(1)
    return(width, height, out)

def save(data, filePath, fileName, ext):
    with open(filePath + fileName +"."+ ext, "wb") as file:
        file.write(bytearray(data))

def resolution(cnt, frameWidth = 240):      # meh
    if cnt > frameWidth*64:
        return 253
    if cnt > frameWidth*32:
        return 252
    if cnt > frameWidth*16:
        return 251
    if cnt > frameWidth*8:
        return 250
    if cnt > frameWidth*4:
        return 249
    if cnt > frameWidth*2:
        return 248
    else: return 247

def biAlEn(curr, prev, frameWidth = 240):
    pad, pad, datacurr = curr       # padding width and height
    if prev and curr == prev:
        return [255]                # dead frame (useless here if pre computed)
    
    outData = []
    ccl = datacurr[0]
    try:
        pcl = prev[2][-1]
    except:
        pcl = ccl
    if pcl != ccl:              # if color changed                 TODO: fix blinking (FIXED)
        outData.append(0)                                      
    
    start = 0

    while (1):                  # very bad exit condition
        end = start
        cnt = 0
        while end < frameSize and datacurr[start] == datacurr[end]:
            cnt += 1                # continous pixels
            end += 1

        if end == frameSize:        # last pixel of screen
            outData.append(254)
            return outData

        if (cnt < 248):
            outData.append(cnt)
            newStart = start + cnt
        else:
            chunk = resolution(cnt)
            outData.append(chunk)
            if chunk == 247:
                newStart = start + 247  # probably 248
                if cnt != 247:
                    outData.append(0)
            else:
                newStart = start + (2**(chunk-247))*frameWidth
                if cnt != (2**(chunk-247))*frameWidth:
                    outData.append(0)
        start = newStart


def biAlDe():       # used 03.5 to test decoding and render
    pass
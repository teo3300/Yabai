from lib import imp, printSize, poster, save, biAlEn, biAlDe

maxframe = 6575

parent = "../"

inPath = parent + "01_export_resized_video/bad_apple_frames_jpg/"
outPath = "./rawdata/"
name1 = "0001"
name2 = "0002"
ext  = "jpg"


# import and extract test
'''
img1 = imp(inPath, name1, ext)          # funzionante
printSize(img1)                         # funzionante
img1 = poster(img1)                     # funzionante
packed = biAlEn(img1, None)             # 
save(packed, outPath, name1, "braw")    # funzionante

img2 = imp(inPath, name2, ext)
printSize(img2)
img2 = poster(img2)
packed = biAlEn(img2, img1)
save(packed, outPath, name2, "braw")
'''


# deadcounter test
'''
print("Counting dead")

# counting dead frames
limit = maxframe + 1
i=1
prev = None
deadCounter = 0
dump = open("./dead.txt", "w")
while i < limit:
    curr = imp(inPath, str(i).zfill(4), ext)
    curr = poster(curr)
    packed = biAlEn(curr, prev)
    if packed == [0]:
        deadCounter += 1
        dump.write(str(i) + "\n")
    if not i % 325:
        print("Now at", i, "\t:", deadCounter)
    prev = curr
    i+=1
dump.close()
print("Done:", deadCounter, "dead frames")
'''


# compression test
'''
name = input("Frame:")

img = imp(inPath, name, ext)
img = poster(img)
out = biAlEn(img, None)
save(out, outPath, name, "BAE")
print("Size:", len(out)*8, ",Base:", 214*160, ", Ratio:", "%.2f" % (len(out)/(214*160)*100), "%")
# print(out)
'''
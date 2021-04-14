from lib import imp, poster, biAlEn, save

maxframe = 6575
parent = "../"

inPath = parent + "01.0_export_resized_video/bad_apple_frames_jpg/"
outPath = parent + "03.0_out_BAE/BAE_file/"
ext = "jpg"

limit = maxframe + 1
i=1
totalSize = 0
prev = None
ln = 0

textdata = open("../04.0_BAE_join/joint/bad_apple.c","w")
textdata.write("const unsigned int bad[] = {")          # format .c
while i < limit:
    if(i % 2):
        curr = imp(inPath, str(i).zfill(4), ext)        # import curr image
        curr = poster(curr)                             # lower bitdepth
        out = biAlEn(curr, prev)                        # encoded frame
        if out == [255]:
            print(str(i).zfill(4)+".BAE: deadframe")    # just report dead frame
        if(not i % 225):
            print("running:", i)
        totalSize += len(out)
        textdata.write("\n\t")
        for l in out:
            textdata.write(str(l)+",")                  # text output
        ln += len(out)
        save(out, outPath, str(i).zfill(4), "BAE")      # raw output
        prev = curr
    i += 1
textdata.write("\n};")
textdata.write("#define bad_len " + str(ln))
textdata.close()

print("DONE")
print("\n\n(b) Size: " + str(totalSize) + ", (b) Original: " + str((214*160*maxframe)/8) + ", Ratio:", "%.2f" % (totalSize/((240*160*maxframe)/8)*100), "%")    # overall compression
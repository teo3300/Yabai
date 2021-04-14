# yep joiner gonna join in the joint

path = "../03.0_out_BAE/BAE_file/"
outPath = "./joint_halfed/"

first = 1
last = 6575

len = 0
cap = last + 1
i=first
out = open(outPath+"bad_apple.c", "w") # don't remeber if I used this or the other one
binry = open(outPath+"bad_apple.BAD", "wb")
out.write("const unsigned char bad[] = {\n")
while i < cap:
    if(i%2):
        print("copying file:",i)
        out.write("\n\t")
        with open(path+str(i).zfill(4)+".BAE","rb") as file:
            data = file.read(1)
            len += 1
            while data:
                out.write(str(int.from_bytes(data, "big")))
                binry.write(data)
                out.write(", ")
                len += 1
                data = file.read(1)
    i+=1
out.write("\n};")
out.write("\n\n#define bad_len " + str(len))
out.close()
binry.close()
print("Done")

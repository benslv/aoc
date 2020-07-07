import hashlib

inp = "yzbqklnj"

i = 0
mined = False
while not mined:
    ans = hashlib.md5((inp+str(i)).encode()).hexdigest()
    if ans[:6] == "000000":
        mined = True
        break
    i += 1

print(i)

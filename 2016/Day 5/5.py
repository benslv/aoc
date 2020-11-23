from hashlib import md5


def generate_md5(string):
    return md5(string.encode("utf-8")).hexdigest()


# Part 1
password = ""
i = 0
inp = "uqwqemis"

print("Decrypting password... ________", end="\r")
while len(password) < 8:
    test = inp+str(i)
    if (hashed := generate_md5(test))[:5] == "00000":
        password += hashed[5]
        print("Decrypting password... "+password +
              ("_"*(8-len(password))), end="\r")
    i += 1

print("\nPart 1 decrypted!")


# Part 2
password = ["_" for _ in range(8)]
i = 0
inp = "uqwqemis"

print("Decrypting password... ________", end="\r")
while "_" in password:
    test = inp+str(i)
    if (hashed := generate_md5(test))[:5] == "00000" and (position := int(hashed[5], 16)) in range(8):
        if password[position] == "_":
            password[position] = hashed[6]

        print("Decrypting password... " + "".join(password), end="\r")
    i += 1

print("\nPassword decrypted!")

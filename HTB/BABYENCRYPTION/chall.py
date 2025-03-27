import string
# MSG = bytes("skibidi", encoding='utf-8')

# print(MSG)
# print(bytes(MSG))

# from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

# ct = encryption(MSG)
# f = open('./msg.enc','w')
# f.write(ct.hex())
# f.close()

f = open('./msg.enc','r')
enc_msg = f.readline()
enc_msg = enc_msg.strip()

byte_msg = bytes.fromhex(enc_msg)
# byte_text = byte_msg.decode("utf-8")

def decrypt(msg):
    result = []
    for char in msg:
        result.append(((char-18)*179)%256)

    return result

final = str(decrypt(byte_msg)).replace("[", "")
final = final.replace("]", "")
final = final.replace(",", "")
print(final)


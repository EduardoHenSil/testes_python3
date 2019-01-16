import struct

fmt = '<3s3sHH'

with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))

print(struct.unpack(fmt, header))
del header
del img

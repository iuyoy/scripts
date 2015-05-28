# A small script to calculate the checksum of IP or Tcp checksum by hex_encode data package

#coding=utf-8

# import binascii
# import struct

def IP_or_Tcp_checksum(data):
    checksum = 0
    _len = len(data)
    i = 0
    while i<_len:
        temp=int(data[i:i+16],2)
        checksum = checksum+temp
        i = i+16
    checksum = (checksum>>16) + (checksum&0xffff)
    checksum = checksum+(checksum>>16)
    return ~checksum
# Maybe I can use struct.
def hex_to_16bits(tcp):
    ntcp=''
    for j in tcp:
        b=bin(int(j,16))
        ntcp+= '0'*(4-len(b)+2)+b[2:]
    return ntcp
if __name__ == "__main__":
    tcp='0a0f09bb0a0f08e5000600381f1c1e62b475a5163d0103d85018ffdf0000'
    tcp=hex_to_16bits(tcp)
    checksum=IP_or_Tcp_checksum(tcp)
    print ('%x' % (checksum & 0xffff))
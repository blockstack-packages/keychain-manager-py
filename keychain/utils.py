from binascii import unhexlify
from keylib.key_formatting import encode, decode, from_int_to_byte, from_byte_to_int, changebase, bin_dbl_sha256

MAINNET_PRIVATE = b'\x04\x88\xAD\xE4'
MAINNET_PUBLIC = b'\x04\x88\xB2\x1E'
TESTNET_PRIVATE = b'\x04\x35\x83\x94'
TESTNET_PUBLIC = b'\x04\x35\x87\xCF'
PRIVATE = [MAINNET_PRIVATE, TESTNET_PRIVATE]
PUBLIC = [MAINNET_PUBLIC, TESTNET_PUBLIC]

def extract_bin_chain_path(chain_path):
    if len(chain_path) == 64:
        return unhexlify(chain_path)
    elif len(chain_path) == 32:
        return chain_path
    else:
        raise ValueError('Invalid chain path')

def hash_to_int(x):
    if len(x) in [40, 64]:
        # decode as hex string
        return decode(x, 16)

    # decode as byte string
    return decode(x, 256)


def bip32_serialize(rawtuple):
    """
    Derived from code from pybitcointools (https://github.com/vbuterin/pybitcointools)
    by Vitalik Buterin
    """
    vbytes, depth, fingerprint, i, chaincode, key = rawtuple
    i = encode(i, 256, 4)
    chaincode = encode(hash_to_int(chaincode), 256, 32)
    keydata = b'\x00'  +key[:-1] if vbytes in PRIVATE else key
    bindata = vbytes + from_int_to_byte(depth % 256) + fingerprint + i + chaincode + keydata
    return changebase(bindata + bin_dbl_sha256(bindata)[:4], 256, 58)


def bip32_deserialize(data):
    """
    Derived from code from pybitcointools (https://github.com/vbuterin/pybitcointools)
    by Vitalik Buterin
    """
    dbin = changebase(data, 58, 256)
    if bin_dbl_sha256(dbin[:-4])[:4] != dbin[-4:]:
        raise Exception("Invalid checksum")
    vbytes = dbin[0:4]
    depth = from_byte_to_int(dbin[4])
    fingerprint = dbin[5:9]
    i = decode(dbin[9:13], 256)
    chaincode = dbin[13:45]
    key = dbin[46:78]+b'\x01' if vbytes in PRIVATE else dbin[45:78]
    return (vbytes, depth, fingerprint, i, chaincode, key)


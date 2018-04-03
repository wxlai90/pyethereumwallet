#!/usr/bin/python

import ecdsa
import sha3

def cksum(s):
        s = s
        h = sha3.keccak_256(s).hexdigest()
        c = ''
        for i,k in zip(s,h):
                if int(k, 16) <= 7:
                        c += i.lower()
                else:
                        c += i.upper()
        return '0x' + c

def gen_keys():
	priv_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
	pub_key = priv_key.get_verifying_key().to_string()
	
	pub_key_hash = sha3.keccak_256(pub_key).hexdigest()
	address = pub_key_hash[24:]
	address = cksum(address)
	priv_key = priv_key.to_string().encode('hex')
	
	return priv_key, address

def main():
	priv_key, address = gen_keys()
	print "Ethereum Address:", address
	print "Private Key:", priv_key


if __name__ == '__main__':
	main()

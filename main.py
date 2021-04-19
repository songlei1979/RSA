import rsa
(pubkey, privkey) = rsa.newkeys(512)
print(pubkey, privkey)
message = "hello world"
print("before crypto:", message.encode('utf8'))
crypto = rsa.encrypt(message.encode('utf8'), pubkey)
print("after crypto", crypto)
message = rsa.decrypt(crypto, privkey)
print("after decrypt:", message.decode('utf8'))
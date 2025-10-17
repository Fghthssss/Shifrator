import zlib
import base64
import hashlib
import marshal
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as pad
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import DES as _DES, DES3 as _DES3, Blowfish as _Blowfish

def get_salt(a, b, c):
    return hashlib.sha256(str(a * 13.37 + b * 7.77 + c * 3.33).encode()).digest()[:8]

def aes_enc(dat, key, ivv):
    padder = pad.PKCS7(algorithms.AES.block_size).padder()
    padded = padder.update(dat) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(ivv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(padded) + encryptor.finalize()

def aes_dec(dat, key, ivv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(ivv), backend=default_backend())
    decryptor = cipher.decryptor()
    buf = decryptor.update(dat) + decryptor.finalize()
    unpadder = pad.PKCS7(algorithms.AES.block_size).unpadder()
    return unpadder.update(buf) + unpadder.finalize()

def des_enc(dat, key, ivv):
    y = 8 - len(dat) % 8
    padded = dat + bytes([y]) * y
    return _DES.new(key[:8], _DES.MODE_CBC, ivv[:8]).encrypt(padded)

def des_dec(dat, key, ivv):
    res = _DES.new(key[:8], _DES.MODE_CBC, ivv[:8]).decrypt(dat)
    return res[:-res[-1]]

def tdes_enc(dat, key, ivv):
    y = 8 - len(dat) % 8
    padded = dat + bytes([y]) * y
    return _DES3.new(key[:24], _DES3.MODE_CBC, ivv[:8]).encrypt(padded)

def tdes_dec(dat, key, ivv):
    res = _DES3.new(key[:24], _DES3.MODE_CBC, ivv[:8]).decrypt(dat)
    return res[:-res[-1]]

def bfish_enc(dat, key, ivv):
    y = 8 - len(dat) % 8
    padded = dat + bytes([y]) * y
    return _Blowfish.new(key[:16], _Blowfish.MODE_CBC, ivv[:8]).encrypt(padded)

def bfish_dec(dat, key, ivv):
    res = _Blowfish.new(key[:16], _Blowfish.MODE_CBC, ivv[:8]).decrypt(dat)
    return res[:-res[-1]]

def transform(txt, aa, bb, cc, mode):
    salt = get_salt(aa, bb, cc)
    keymat = hashlib.sha512((str(aa) + str(bb) + str(cc)).encode() + salt).digest()
    akey, aiv = keymat[:32], keymat[32:48]
    dkey, div = keymat[:8], keymat[8:16]
    tkey, bkey, biv = keymat[:24], keymat[:16], keymat[16:24]

    if mode == "1":
        try:
            marshaled = marshal.dumps(txt)
            aes_encrypted = aes_enc(marshaled, akey, aiv[:16])
            tdes_encrypted = tdes_enc(aes_encrypted, tkey, div)
            des_encrypted = des_enc(tdes_encrypted, dkey, div)
            res = bfish_enc(des_encrypted, bkey, biv)
            packed = salt + aiv[:16] + res
            compressed = zlib.compress(packed)
            return base64.b64encode(compressed).decode()
        except Exception as e:
            return f"[!] Encryption error: {e}"

    if mode == "2":
        try:
            data = zlib.decompress(base64.b64decode(txt.encode()))
            salt2, ivv, encd = data[:8], data[8:24], data[24:]
            keymat = hashlib.sha512((str(aa) + str(bb) + str(cc)).encode() + salt2).digest()
            akey = keymat[:32]
            dkey = keymat[:8]
            div = keymat[8:16]
            tkey = keymat[:24]
            bkey = keymat[:16]
            biv = keymat[16:24]
            for L, func, rname in (
                (8, bfish_dec, 'Blowfish'),
                (8, des_dec, 'DES'),
                (8, tdes_dec, '3DES'),
                (16, aes_dec, 'AES')
            ):
                if len(encd) % L:
                    return f"[!] Decryption error ({rname}: data not multiple of block size)"
                try:
                    if rname == 'Blowfish':
                        encd = func(encd, bkey, biv)
                    elif rname == 'DES':
                        encd = func(encd, dkey, div)
                    elif rname == '3DES':
                        encd = func(encd, tkey, div)
                    elif rname == 'AES':
                        encd = func(encd, akey, ivv)
                except Exception as err:
                    return f"[!] Decryption error ({rname}) {err}"
            try:
                return marshal.loads(encd)
            except Exception as e:
                return "[!] Decryption error (unmarshal)"
        except Exception as err:
            return f"[!] Decryption error {err}"

    return "[!] Unknown method"

def main():
    while True:
        print("[*] 1 - Translate\n[*] 2 - Untranslate")
        mode = input("[>] Method: ")
        txt = input("[>] Text: ")
        try:
            aa = int(input("\n[>] Weight: "))
            bb = int(input("[>] Level: "))
            cc = int(input("[>] Key: "))
        except Exception:
            print("[!] Invalid weight, level or key input.")
            continue
        print(f"\n{transform(txt, aa, bb, cc, mode)}\n")

if __name__ == "__main__":
    main()

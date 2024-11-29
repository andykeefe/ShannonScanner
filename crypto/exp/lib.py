
LIB_REGEX = {
    'OpenSSL': r'<openssl\/|evp.h|[Oo]penssl|OPENSSL|[Oo]penSSL',
    'GnuTLS': r'gnutls',
    'PyCryptodome': r'from Crypto.',
    'py-cryptography': r'from (cryptography.fernet|cryptography.hazmat)',
    'WolfSSL/WolfCrypt': r'wolfssl|WOLFSSL|WolfSSL|Wolfssl|wc_Init',
    'Go Crypto': r'crypto\/(aes|cipher|des|dsa|ecdsa|ed25519|elliptic|md5|rc4|rsa|sha)',
    'Libsodium': r'[Ll]ibsodium|sodium.h|LIBSODIUM',
    'NaCl': r'#include "crypto_(box|scalarmult|sign|secretbox|stream|auth|onetimeauth)\.h"',
    'Botan': r'botan\/|BOTAN_',
    'Bouncy Castle': r'[Bb]ouncycastle|BOUNCYCASTLE', ## to be improved
    'MatrixSSL': r'matrixssl|[Mm]atrixSSL|MATRIXSSL', ## to be completed
    'Libgcrypt': r'\b[Ll]ibgcrypt|\bGCRY_', ## to improved
    'LibreSSL': r'LIBRESSL|[Ll]ibressl|[Ll]ibreSSL', ## to be completed
    'Crypto++': r'[Cc]ryptopp|[Cc]rypto\+\+|CRYPTOPP|CRYPTO\+\+', ## to be reviewed
    'Nettle': r'[Nn]ettle|NETTLE',
    'LibTomCrypt': r'LIBTOMCRYPT|[Ll]ib[Tt]om[Cc]rypt', ## to be completed
    'Relic': r'(RELIC|[Rr]elic)_(CORE|[Cc]ore|util|ep|eb|bn)', ## to be completed
    'Sodium Oxide': r'sodiumoxide::', ## to be completed
    'Rustls': r'rustls|aws_lc_rs', ## to be completed
    'ring': r'ring::',
    'CryptLib': r'\bcrypt(lib|Create|Encrypt|Decrypt)', ## to be improved
    'Orion': r'orion::', ## to be completed
    'Mbed TLS': r'[Mm]bedtls|[Mm]bedTLS|MBEDTLS'
    }

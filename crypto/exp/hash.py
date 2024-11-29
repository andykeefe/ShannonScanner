HASH_REGEX = {
    'SHA1': r'\bSHA[-_\.]?1\b|sha[-_\.]?1\b|Sha[-_\.]?1',
    'SHA2': r'SHA[-_\.]?2|sha[-_\.]?2|Sha[-_\.]?2|SHA384|[Ss]ha384|SHA_384|[Ss]ha_384|SHA-384|[Ss]ha-384|SHA512|[Ss]ha512|SHA_512|[Ss]ha_512',
    'SHA3': r'SHA[-_\.]?3[-_\.]$|[Ss]ha[-_\.]?3[-_\.]$',
    'MD2': r'MD2|md2|Md2',
    'MD4': r'MD4|md4|Md4',
    'MD5': r'MD5|md5|Md5',
    'MD6': r'MD6|md6|Md5',
    'Threefish': r'Threefish|threefish|ThreeFish|THREEFISH',
    'BLAKE2': r'BLAKE2|[Bb]lake2',
    'BLAKE3': r'BLAKE3|[Bb]lake3',
    'SipHash': r'SIPHASH|Sip[Hh]ash',
    'RIPEMD': r'RIPEMD|[Rr]ipe[Mm]d', 
    'SM3': r'[Ss]m3|SM3',
    'WHIRLPOOL': r'WHIRLPOOL|whirlpool',
    'Keccak': r'KECCAK|[Kk]eccak'
    }
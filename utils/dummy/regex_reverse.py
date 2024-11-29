import exrex


# Symmetric cipher regex
AES_REGEX = r'[A][E][S](?:([._-])?(?:128|192|256))|[a][e][s](?:([._-])?(?:128|192|256))|aes|AES'
DES_REGEX = r'[D][E][S](?:([._-])?(?:56|64))|[d][e][s](?:([._-])?(?:56|64))|DES\.|des\.|DES-|des-|DES_|des_|DES:|des:'

# Hash function regex
SHA1_REGEX = r'\bSHA[-_\.]?1\b|sha[-_\.]?1\b|Sha[-_\.]?1'
SHA2_REGEX = r'SHA[-_\.]?2|sha[-_\.]?2|Sha[-_\.]?2|SHA384|[Ss]ha384|SHA_384|[Ss]ha_384|SHA-384|[Ss]ha-384|SHA512|[Ss]ha512|SHA_512|[Ss]ha_512'
SHA3_REGEX = r'SHA[-_\.]?3[-_\.]$'

# Modes of operation regex
ECB_REGEX = r'\b(?:[-_\.](?:ECB|ecb|Ecb))'
CBC_REGEX = r'\b(?:[-_\.](?:CBC|cbc|Cbc))'
CCM_REGEX = r'\b(?:[-_\.](?:CCM|ccm|Ccm)|Ccm|CCM))'
OFB_REGEX = r'\b(?:[-_\.](?:OFB|ofb|Ofb)|Ofb|OFB))'
CFB_REGEX = r'\b(?:[-_\.](?:CFB|cfb|Cfb)|Cfb|CFB))'
CTR_REGEX = r'\b(?:[-_\.:](?:CTR|ctr|Ctr))\b'

# Digital signature algorithms
ECDSA_REGEX = r'ECDSA|ecdsa|EcDSA'

# Libraries
CRYPTOPP_REGEX = r'[Cc]ryptopp|[Cc]rypto\+\+|CRYPTOPP|CRYPTO\+\+'
CRYPTLIB_REGEX = r'\bcryptlib|\bcryptCreate|\bcryptEncrypt|\bcryptDecrypt'



def reverse_regex(regex):
    matches = set(list(exrex.generate(regex)))
    possible_matches = {f"Match_{i+1}": match for i, match in enumerate(matches)}
    return possible_matches


if __name__ == '__main__':
    match_regex = reverse_regex(SHA3_REGEX)
    print("Possible matches: ")
    for key, value in match_regex.items():
        print(f"{key}: {value}")


    print("\n\n\n")

SYMMETRIC_REGEX = {
    'AES': r'[A][E][S](?:([._-])?(?:128|192|256))|[a][e][s](?:([._-])?(?:128|192|256))|aes|AES',
    'ARIA': r'[A][R][I][A](?:([._-])?(?:192|256))|[Aa][r][i][a](?:([._-])?(?:192|256))',
    'Blowfish': r'Blowfish|blowfish|BlowFish|BLOWFISH',
    'Twofish': r'Twofish|twofish|TwoFish|TWOFISH',
    'ChaCha20/XChaCha20': r'ChaCha20Poly1305|chacha20poly1305|chacha20|chacha',
    'Camellia': r'Camellia|camellia|CAMELLIA',
    'CAST': r'[C][A][S][T](?:([._-])?(?:|5|6|128|192|256))|[Cc][a][s][t](?:([._-])?(?:5|6|128|192|256))',
    'DES': r'[D][E][S](?:([._-])?(?:56|64))|[d][e][s](?:([._-])?(?:56|64))',
    'TDEA': r'3DES|3[Dd]es|DES3|Des3|3-DES|3-des|des-3|DES-3|TDES|[Tt]des|TDEA|[Tt]dea',  ## to be improved
    'IDEA': r'IDEA[\._-](CBC|ECB|OFB|CTR)|[Ii]dea[\._-]([Cc]bc|[Ee]cb|[Oo]fb|[Cc]tr)',
    'MARS': r'#include "mars\.h"', ## to be completed
    'RC4': r'arc4|ARC4|Arc4|rc4|RC4|Rc4|ARCFOUR|arcfour|ArcFour|RCFOUR|RcFour|rcfour',
    'RC5': r'[Aa]rc5|ARC5|[Rr]c5|RC5|ARCFIVE|arcfive|ArcFive|RCFIVE|RcFive|rcfive',
    'RC6': r'[Aa]rc6|ARC6|[Rr]c6|RC6|ARCSIX|arcsix|ArcSix|RCSIX|RcSix|rcsix',
    'SEED': r'(SEED|[Ss]eed)[-_\.](CBC|[Cc]bc|ECB|[Ee]cb|OFB|[Oo]fb|[Pp]oly1305|CMAC|[Cc]mac|GMAC|[Gg]mac)', 
    
    ##  SEED is a tough algorithm to parse out because the word 'seed' is used in a bunch of different
    ##  source code for all sorts of reasons; RNGs, simulation software, etc. So hopefully this regex is 
    ##  specific enough to cut down on false positives. And hopefully we don't miss too many false negatives!

    'Serpent': r'([Ss]erpent|SERPENT)[-_\.](CBC|[Cc]bc|CFB|[Cc]fb|ECB|[Ee]cb|OFB|[Oo]fb]|TECB|[Pp]oly1305)', ## to be completed
    'SM4': r'[Ss]m4|SM4'
    }

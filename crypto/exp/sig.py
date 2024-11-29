
DIGITAL_SIGNATURE_REGEX = {
    'RSA': r'\b(?<=[-_\.:](RSA|rsa|Rsa))|(RSA|[Rr]sa)[-_\.:]',
    'DSA': r'\b(?<=[-_\.:](DSA|dsa|Dsa|DSS|[Dd]ss))|(DSA|dsa|Dsa|DSS|[Dd]ss)[-_\.:]',
    'ECDSA': r'ECDSA|ecdsa|EcDSA',
    'ED25519': r'ed25519|ED25519|Ed25519',
    'EdDSA': r'EdDSA|eddsa|EDDSA'
    }

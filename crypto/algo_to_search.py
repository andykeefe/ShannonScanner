#                      REGEX COLLECTION                              #
# ------------------------------------------------------------------ # 

from crypto.exp.sym_exp import SYMMETRIC_REGEX
from crypto.exp.mode import MODE_OPERATIONS_REGEX
from crypto.exp.hash import HASH_REGEX
from crypto.exp.sig import DIGITAL_SIGNATURE_REGEX
from crypto.exp.lib import LIB_REGEX

import exrex



#                          REGEX REVERSAL                             #
# ------------------------------------------------------------------- #

def reverse_regex(regex):
    return set(exrex.generate(regex))



#                       ALGORITHM DICTIONARY                          #
# ------------------------------------------------------------------- #

ALGORITHMS = {
    'Symmetric algorithms': {algorithm: reverse_regex(regex) for algorithm, regex in SYMMETRIC_REGEX.items()},

    'Hash functions':{hash: reverse_regex(regex) for hash, regex in HASH_REGEX.items()},

    'Modes of operation': {mode: reverse_regex(regex) for mode, regex in MODE_OPERATIONS_REGEX.items()},

    'Digital signatures': {algorithm: reverse_regex(regex) for algorithm, regex in DIGITAL_SIGNATURE_REGEX.items()},

    'Libraries': {library: reverse_regex(regex) for library, regex in LIB_REGEX.items()}
}




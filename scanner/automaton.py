

#                        AHO-CORASICK SET UP                          #
# ------------------------------------------------------------------- #

import ahocorasick


def ac_setup(ALGORITHMS):
    automaton = ahocorasick.Automaton()
    for category, algorithms in ALGORITHMS.items():
        for algorithm, regex in algorithms.items():
            for pattern in regex:
                automaton.add_word(pattern, (category, algorithm, pattern))
    automaton.make_automaton()
    return automaton



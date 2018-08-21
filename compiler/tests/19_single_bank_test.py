#!/usr/bin/env python3
"""
Run a regression test on various srams
"""

import unittest
from testutils import header,openram_test
import sys,os
sys.path.append(os.path.join(sys.path[0],".."))
import globals
from globals import OPTS
import debug

class single_bank_test(openram_test):

    def runTest(self):
        globals.init_openram("config_20_{0}".format(OPTS.tech_name))
        from bank import bank

        debug.info(1, "No column mux")
        a = bank(word_size=4, num_words=16, words_per_row=1, num_banks=1, name="bank1_single")
        self.local_check(a)

        debug.info(1, "Two way column mux")
        a = bank(word_size=4, num_words=32, words_per_row=2, num_banks=1, name="bank2_single")
        self.local_check(a)

        debug.info(1, "Four way column mux")
        a = bank(word_size=4, num_words=64, words_per_row=4, num_banks=1, name="bank3_single")
        self.local_check(a)

        # Eight way has a short circuit of one column mux select to gnd rail
        debug.info(1, "Eight way column mux")
        a = bank(word_size=2, num_words=128, words_per_row=8, num_banks=1, name="bank4_single")
        self.local_check(a)
        
        globals.end_openram()
        
# instantiate a copy of the class to actually run the test
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main()

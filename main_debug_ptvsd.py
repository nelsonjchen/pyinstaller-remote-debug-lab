from __future__ import print_function
from counterup import CounterPrint

print("DEBUG VERSION")
import ptvsd
ptvsd.enable_attach()
ptvsd.wait_for_attach()

if __name__ == "__main__":
    CounterPrint()
from __future__ import print_function
from counterup import CounterPrint

print("DEBUG VERSION")
import ptvsd
ptvsd.enable_attach("my_secret", address=("0.0.0.0", 3000))
print("Waiting for Attach")
ptvsd.wait_for_attach()

if __name__ == "__main__":
    CounterPrint()
from __future__ import print_function
from counterup import CounterPrint

print("DEBUG VERSION")
import pydevd
pydevd.settrace('localhost', port=3434, stdoutToServer=True, stderrToServer=True)

if __name__ == "__main__":
    CounterPrint()
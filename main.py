import os
import sys
import subprocess
import pkg_resources

import foo
from foo.lib import X, SCRIPT_PATH

if __name__ == "__main__":
    print(f"foo from {foo.__path__}")
    print(X)
    print(sys.argv)
    print(os.getcwd())
    print(f"SCRIPT_PATH = {SCRIPT_PATH}")
    subprocess.check_call([SCRIPT_PATH])

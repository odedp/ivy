import os
import platform
import z3

def main():
    if platform.system() == 'Darwin':
        path = ':'.join(os.path.join(os.path.dirname(os.path.abspath(x)),'lib') for x in [z3.__file__,__file__])
        pvar = 'DYLD_LIBRARY_PATH'
        if os.environ.get(pvar):
            path += ':' + os.environ[pvar]
        cmd = 'export {}={}'.format(pvar,path)
        print(cmd)

#! /usr/bin/env python3

def module_sys():
    import sys
    sys_version = sys.version_info
    sys_cr = sys.copyright
    print("version: {}, copyright: {}".format(sys_version,sys_cr))

def module_os():
    import os
    print(os.name)
    print(os.getcwd)
    print(os.getenv("PATH"))
    print(os.environ["PATH"])
    


def main():
    # module_sys()
    module_os()

if __name__ == "__main__": main()
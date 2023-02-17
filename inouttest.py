#!/usr/bin/env python3
#
import sys
def print_ho(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# sys.stderr.write('no Error')
if __name__ == '__main__':
    print_ho(__name__)
else:
    while True:
    # try:
        instr = input()
        print("Прилетело: {}".format(instr))
    # except:
    # EOFError:
    # sys.stderr.write('EOF Error')
    # print('EOFError', file=sys.stderr)
        pass

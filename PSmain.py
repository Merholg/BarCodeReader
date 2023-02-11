#!/usr/bin/env python3
#
import subprocess

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    # print_hi('PyCharm')
    with subprocess.Popen('python3 inouttest.py', executable='/bin/bash', shell=True, stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE) as inouttest:
        with open('error.log', 'a') as log_file:
            stdout, stderr = inouttest.communicate(input='data_to_write'.encode())
            print("STDOUT is: {}".format(stdout.decode()))
            # print("STDERR is: {}".format(stderr.decode()))
            log_file.write(stderr.decode())

    # input('Stop?')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

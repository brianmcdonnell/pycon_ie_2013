#!/bin/bash

source ./env/bin/activate
# `exec` replaces the bash process with the command being exec'd
#     NB: Any subsequent bash commands will not be executed.
# Alternatively, we could have used a pidproxy program to relay signals
# to the command being executed.
#     e.g. https://github.com/Supervisor/supervisor/blob/master/supervisor/pidproxy.py
exec ./hello.py --unix_socket /tmp/tornado_hello.sock

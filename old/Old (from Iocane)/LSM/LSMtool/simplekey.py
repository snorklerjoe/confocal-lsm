#!/usr/bin/python
import keyboard
import sys
sys.stdout.flush()
print keyboard.is_pressed(sys.argv[1])

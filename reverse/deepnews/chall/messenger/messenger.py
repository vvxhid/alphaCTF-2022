#!/usr/bin/python3

import subprocess


print('So did you find anything?\nyou can send me the link here',flush=True)

link = input('link: ')

print('ok, i will click on it',flush=True)

subprocess.call(
    ["adb", "shell", f"am start -a android.intent.action.VIEW -d '{link}' com.alphactf.deepnews"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)

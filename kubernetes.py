#!/usr/bin/python3

import subprocess
import cgi

print("content-type: text/html")
print()

form=cgi.FieldStorage()
cmd=form.getvalue("x")
ouput=subprocess.getoutput("sudo "+ cmd)
print(output)

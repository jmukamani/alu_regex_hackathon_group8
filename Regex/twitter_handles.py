#!/bin/bash env ruby

import re
handle = input('enter your twitter username ')

pattern = re.compile("@(\w+)")
if re.match(pattern,handle):
    print("Twitter username found")
else:
    print("Error")

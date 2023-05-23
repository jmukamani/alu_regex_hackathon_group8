#!/bin/bash env.ruby 

import re

Isbn = input('please input an ISBN of your choice ')
pattern = re.compile(^ISBN \d{3}-\d-\d{3}-\d{5}-\d$)

if re.search(pattern,Isbn):
    print("Isbn found")
else
    print("Error")


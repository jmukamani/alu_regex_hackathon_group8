# The jokes should match the pattern "Why did the ... ? Because...", where the first part of the pattern can be any string of characters, 
# and the second part can be any string of characters.
import re
jokes = re.compile(r'Why\sdid\sthe\w+\?\sBecause\w+')

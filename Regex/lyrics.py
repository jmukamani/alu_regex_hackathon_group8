import re

song = r"\[Verse \d+] .+"

# Test string
lyrics = "[Verse i] I'm walking on sunshine"  # Write your own lyrics
match = re.search(song, lyrics)

if match:
    print(match.group(0))
else:
    print("No match found!")

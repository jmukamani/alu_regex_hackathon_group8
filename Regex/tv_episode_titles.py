# The episode titles should match the pattern "Show Name SXXEXX: Episode Title", where "Show Name" is any string of characters, 
# SXX is a two-digit season number and EXX is a two-digit episode number, and "Episode Title" is any string of characters.

import re

sample_string = 'Today we want to watch Merlin S09E07: Last Digit and Thor S08E03: Unfailing Love at the cinema'

tV_episode_titles = re.compile('([A-Z]\w+\s?)+S\d{2}E\d{2}:\s([A-Z]\w+\s?)+')

show_names = tV_episode_titles.finditer(sample_string)

print()
for name in show_names:
  print(name.group(0))


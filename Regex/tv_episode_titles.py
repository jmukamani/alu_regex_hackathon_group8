# The episode titles should match the pattern "Show Name SXXEXX: Episode Title", where "Show Name" is any string of characters, 
# SXX is a two-digit season number and EXX is a two-digit episode number, and "Episode Title" is any string of characters.

import re

sample_string = 'Merlin Th S04E07'

# tV_episode_titles = re.match('([A-Z]w+\s)+S\d{2}E\d{2}', sample_string)

tV_episode_titles = re.match('^/D*', sample_string)

# show_names = tV_episode_titles.match()

print('Show', tV_episode_titles)

# for name in show_names:
#     print(name)
# import re

# sample_string = 'Today we want to watch Merlin S09E07: Last Digit and Thor S08E03: Unfailing Love at the cinema'
# sample_joke = 'Why did the girl faint yesterday? Because she is fainthearted.\
#     Why did the color of the sky change? Because God is omnipotent'

# # jokes = re.findall(r'Why\sdid\sthe\w+\?\sBecause\w+', sample_joke)
# jokes_reg = r'Why\sdid\sthe[\s\w]+[?]\sBecause[\s\w]+.?'
# jokes = re.findall(jokes_reg, sample_joke)
# movie_reg = r'[A-Z]\w+\sS\d{,2}E\d{,2}:[\s\w]{,2}'
# movie_titles = re.findall(movie_reg, sample_string)

# print()
# print('movie_titles:', movie_titles)
# print('jokes:', jokes)

import re

movie_title = "Sanctuary (221) LENGENDARY(304)"  # Replace with your actual movie title

Name = r'^[^\(\)]+\s\(\d{,4}\)$'
movie_match = re.match(Name, movie_title)

if movie_match:
    print(movie_match.group(0))
else:
    print("The movie title does not match the pattern.")
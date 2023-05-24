
import re

movie_title = "Today we want to watch Sanctuary (221), Legendary(1234), and Merlin(23)"  # Replace with your actual movie title


def match_movie_titles(input_string, obj):

    regex_pattern = r"\w+\s*\(\d+\)"
    movie_match = re.findall(regex_pattern, input_string)
    all_matches = ''

    for title in movie_match:
       all_matches += f'{title}, '
       print(all_matches)

    if len(all_matches) == 0:
        obj['Movie Title'] = 'No match found!'
        print(obj)
        return

    obj['Movie Title'] = all_matches
    print(obj)
    return


if __name__ == '__main__':
    match_dict = {}
    match_movie_titles('movie_title', match_dict)
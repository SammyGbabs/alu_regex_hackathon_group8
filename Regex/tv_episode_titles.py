# The episode titles should match the pattern "Show Name SXXEXX: Episode Title", where "Show Name" is any string of characters,
# SXX is a two-digit season number and EXX is a two-digit episode number, and "Episode Title" is any string of characters.

import re

sample_string = 'Today we want to watch Merlin S09E07: Last Digit and Thor S08E03: Unfailing Love at the cinema'


def add_tv_episode_title(input_string, obj):
    tV_episode_titles = re.compile(
        '([A-Z]\w+\s?)+S\d{2}E\d{2}:\s([A-Z]\w+\s?)+')

    show_names = tV_episode_titles.finditer(input_string)

    all_matches = ''

    for name in show_names:
        all_matches += f'{name.group(0)}, '
        print(all_matches)

    if len(all_matches) == 0:
        obj['TV_EPISODE_TITLES'] = 'No match found!'
        print(obj)
        return

    obj['TV_EPISODE_TITLES'] = all_matches
    print(obj)
    return



if __name__ == '__main__':
    match_dict = {}
    add_tv_episode_title(sample_string, match_dict)
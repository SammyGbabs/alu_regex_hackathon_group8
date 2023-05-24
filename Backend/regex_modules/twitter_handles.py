import re

sample_string = 'Today @ssam_dev we want @olubode14 to watch @akd_123 Merlin S09E07: Last Digit and Thor S08E03: Unfailing Love at the cinema'


def match_twitter_username(input_string, obj):
    regex_pattern = re.compile("@(\w+)")
    username_matches = regex_pattern.finditer(input_string)

    all_matches = ''

    for username in username_matches:
        all_matches += f'{username.group(0)}, '

    if len(all_matches) == 0:
        obj['Twitter Username'] = 'No match found!'
        return

    obj['Twitter Username'] = all_matches
    return

if __name__ == '__main__':
    match_dict = {}
    match_twitter_username('sample_string', match_dict)
# The jokes should match the pattern "Why did the ... ? Because...", where the first part of the pattern can be any string of characters, 
# and the second part can be any string of characters.
import re

sample_string = 'Why did the king laugh at the clown? Because the clown looked really funny'

def match_jokes(input_string, obj):
    pattern = re.compile(r'Why\sdid\sthe.*?\? Because.*?')
    jokes = pattern.finditer(input_string)

    all_matches = ''

    for joke in jokes:
        all_matches += f'{joke.group(0)}, '

    if len(all_matches) == 0:
        obj['Jokes'] = 'No match found!'
        return

    obj['Jokes'] = all_matches
    return


if __name__ == '__main__':
    match_dict = {}
    match_jokes('sample_string', match_dict)

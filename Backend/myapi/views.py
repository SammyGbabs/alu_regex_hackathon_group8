from rest_framework.response import Response
from rest_framework.decorators import api_view

from regex_modules.add_tv_episode_title import add_tv_episode_title
from regex_modules.match_movie_titles import match_movie_titles
from regex_modules.twitter_handles import match_twitter_username

matchers = [add_tv_episode_title, match_movie_titles, match_twitter_username]
movie_title = "Today we want to watch Sanctuary (221), Legendary(1234), and Merlin(23)"  # Replace with your actual movie title
result = {}

# Create your views here.
@api_view(['POST'])
def regex(request):
    user_input = request.body.decode('utf-8')

    for matcher in matchers:
        matcher(user_input, result)
    
    return Response({'message': 'success', 'data': result})
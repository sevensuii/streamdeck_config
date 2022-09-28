import sys
import requests as req
import os
# import argparse

# TODO delete when upload repo
# TODO implement autoupdate script
# bearer_token = 'BQCpqWdt9i9HKvvwhHpKQsHSe0KayXoLfFcTAKbEO7ef8uDbX-tkJhp6YBeXF0lGXZRGP4Ys40P2besqofF_0U_myrWzQWN2jl_SVxWYRGmj7CitZMabtTEr7cyjXrrgYXQHAn1FnpdRZVC1Jc2z_lLu9bjwhXP1Yln88lUNoNVHdC1l-3uzzVg3pGHsfMjTC62KY-xCtxSN'
spoty_api_url = 'https://api.spotify.com/v1/me/player'
# AUTH_URL = 'https://accounts.spotify.com/api/token'
AUTH_URL = 'https://accounts.spotify.com/authorize'
# asdasd = 


# auth_response = req.post(AUTH_URL, data={
#     'grant_type': 'client_credentials',
#     'client_id': '9180a8561d3f4c77965285a822d08b70',
#     'client_secret': '5b09c5a9b30e4654aca1639ac18af082'
# })


# auth_response = req.get(AUTH_URL, data={
#     'client_id': '9180a8561d3f4c77965285a822d08b70',
#     'response_type': 'token',
#     'redirect_uri': 'https://localhost:8888/callback',
#     'scope': 'user-modify-playback-state user-read-playback-state',
#     'client_secret': '5b09c5a9b30e4654aca1639ac18af082'
# })

auth_response = req.get(AUTH_URL+'?client_id=9180a8561d3f4c77965285a822d08b70&response_type=code&redirect_uri=http://localhost:8888/callback&scope=user-modify-playback-state%20user-read-playback-state&show_dialog=true')

# auth_response_data = auth_response.json()
# bearer_token = auth_response_data['access_token']
print(auth_response.text)






# os.getenv('SPOTIFY_TOKEN')



# if ( 'next' == sys.argv[1] ):
#     next_url = spoty_api_url + '/pause'
#     response = req.put(spoty_api_url, headers={'Authorization': 'Bearer ' + bearer_token})
#     print(response)
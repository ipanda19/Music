import pylast

API_KEY = "43a50efab57e43b554f57bd94593a27b"
API_SECRET =   "3313a702044f9c51a9fd836ce2031fef"
# In order to perform a write operation you need to authenticate yourself
username = "LPanda1"
password_hash = pylast.md5("A9162218347a!")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)
import pylast

# Now you can use that object everywhere
#artist = network.get_artist("System of a Down")
track = network.get_track("Iron Maiden", "The Nomad")
track.love()
track.add_tags(("awesome", "favorite"))

user_name="Edguy90"
period = 7
limit = 50
 pylast.user.get_top_tracks(user_name, period, limit)

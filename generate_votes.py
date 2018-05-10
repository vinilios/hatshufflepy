import hatshufflepy
import datetime
import sys


start = datetime.datetime.now()
crs_file = "crs.json"
votes_file = "votes.json"

hatshufflepy.hat_shuffle_generate_encoded_votes(crs_file, votes_file)

end = datetime.datetime.now() - start
print(end)

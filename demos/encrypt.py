import hatshufflepy
import datetime
import sys


start = datetime.datetime.now()
crs_file = "crs.json"
votes_file = "votes.json"
ciphertexts_file = "ciphertexts.json"

hatshufflepy.hat_shuffle_encrypt(crs_file, votes_file, ciphertexts_file)

end = datetime.datetime.now() - start
print(end)

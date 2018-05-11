import hatshufflepy
import datetime
import sys


start = datetime.datetime.now()
secret_file = "sk"
crs_file = "crs.json"
votes_file = "votes.json"
proofs_file = "proofs.json"
decrypted_votes_file = "decrypted_votes.json"

hatshufflepy.hat_shuffle_decrypt(crs_file, votes_file, proofs_file,
                                 decrypted_votes_file, secret_file)

end = datetime.datetime.now() - start
print(end)

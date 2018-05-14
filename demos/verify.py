import hatshufflepy
import datetime
import sys


start = datetime.datetime.now()
crs_file = "crs.json"
ciphertexts_file = "ciphertexts.json"
proofs_file = "proofs.json"

print(hatshufflepy.hat_shuffle_verify(crs_file, ciphertexts_file, proofs_file))

end = datetime.datetime.now() - start
print(end)

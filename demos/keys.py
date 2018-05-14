import hatshufflepy
import datetime
import sys


if sys.argv[0]:
    votes_number = int(sys.argv[1])
else:
    votes_number = 100

start = datetime.datetime.now()
secret_file = "sk"
public_file = "pk"

hatshufflepy.hat_shuffle_key_gen(votes_number, public_file, secret_file)

end = datetime.datetime.now() - start
print(end)

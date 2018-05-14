import hatshufflepy
import datetime
import sys


if sys.argv[0]:
    votes_number = int(sys.argv[1])
else:
    votes_number = 100

start = datetime.datetime.now()
crs_file = "crs.json"
public_file = "pk"

hatshufflepy.hat_shuffle_create_crs(votes_number, crs_file, public_file)

end = datetime.datetime.now() - start
print(end)

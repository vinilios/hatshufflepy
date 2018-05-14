import hatshufflepy
import datetime
import sys


if sys.argv[1]:
    votes_number = int(sys.argv[1])
else:
    votes_number = 100

start = datetime.datetime.now()
hatshufflepy.hat_shuffle_test_mixnet(votes_number)

end = datetime.datetime.now() - start
print(end)

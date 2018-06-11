import hatshufflepy
import datetime
import sys


start = datetime.datetime.now()
pk_file = "pk"
votes_file = "votes.json"
votes = 100
ballots = 10

hatshufflepy.hat_shuffle_demo_voting(votes, ballots, pk_file, votes_file)

end = datetime.datetime.now() - start
print(end)

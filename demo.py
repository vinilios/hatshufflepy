import hatshufflepy
import datetime

start = datetime.datetime.now()
votes_number = 1000
crs_file = "crs.json"
votes_file = "votes.json"
ciphertexts_file = "ciphertexts.json"
proofs_file = "proofs.json"
decrypted_votes_file = "decrypted_votes.json"

hatshufflepy.hat_shuffle_create_crs(votes_number, crs_file)
hatshufflepy.hat_shuffle_generate_encoded_votes(crs_file, votes_file)
hatshufflepy.hat_shuffle_encrypt(crs_file, votes_file, ciphertexts_file)
hatshufflepy.hat_shuffle_prove(crs_file, ciphertexts_file, proofs_file)
hatshufflepy.hat_shuffle_verify(crs_file, ciphertexts_file, proofs_file)
hatshufflepy.hat_shuffle_decrypt(crs_file, votes_file, proofs_file,
                                 decrypted_votes_file)

end = datetime.datetime.now() - start
print(end)

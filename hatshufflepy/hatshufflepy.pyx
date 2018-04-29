cimport hatshufflepy


def hat_shuffle_create_crs(votes_number, crs_file):
	hatshufflepy.create_crs(votes_number, crs_file)


def hat_shuffle_generate_encoded_votes(crs_file, votes_file):
	hatshufflepy.generate_encoded_votes(crs_file, votes_file)


def hat_shuffle_encrypt(crs_file, votes_file, ciphertexts_file):
	hatshufflepy.encrypt(crs_file, votes_file, ciphertexts_file)


def hat_shuffle_prove(crs_file, ciphertexts_file, proofs_file):
	hatshufflepy.prove(crs_file, ciphertexts_file, proofs_file)


def hat_shuffle_verify(crs_file, ciphertexts_file, proofs_file):
	hatshufflepy.verify(crs_file, ciphertexts_file, proofs_file)


def hat_shuffle_decrypt(crs_file, votes_file, proofs_file,
                        decrypted_votes_file):
	hatshufflepy.decrypt(crs_file, votes_file, proofs_file,
                      decrypted_votes_file)

from libcpp cimport bool
from libcpp.string cimport string

cdef extern from "mixnet.h":
	bool create_crs(int votes_number, string crs_file)

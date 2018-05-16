# Install libhatshuffle
cd hatshufflepy/libhatshuffle/
git fetch
git submodule update --init --recursive
git checkout lib
cp ../libhatshuffle_changes/CMakeLists.txt CMakeLists.txt
cp libff_changes/depends/libff/libff/CMakeLists.txt depends/libff/libff/CMakeLists.txt
cp libff_changes/depends/libff/depends/CMakeLists.txt depends/libff/depends/CMakeLists.txt
cp libff_changes/depends/libff/libff/algebra/curves/bn128/bn128_pairing.cpp depends/libff/libff/algebra/curves/bn128/bn128_pairing.cpp
cp libff_changes/depends/libff/libff/algebra/curves/bn128/bn128_pp.cpp depends/libff/libff/algebra/curves/bn128/bn128_pp.cpp
# Build and install
mkdir build && cd build && cmake  .. -DCMAKE_INSTALL_PREFIX=../
# Use multiple cores
# mkdir build && cd build && cmake -DMULTICORE=ON .. -DCMAKE_INSTALL_PREFIX=../
make && make install
cd ../../../

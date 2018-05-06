cd hatshufflepy/libhatshuffle/
git fetch && git checkout lib
git submodule update --init --recursive
cp ..//libhatshuffle_changes/CMakeLists.txt CMakeLists.txt
cp libff_changes/depends/libff/libff/CMakeLists.txt depends/libff/libff/CMakeLists.txt
cp libff_changes/depends/libff/depends/CMakeLists.txt depends/libff/depends/CMakeLists.txt
cp libff_changes/depends/libff/libff/algebra/curves/bn128/bn128_pairing.cpp depends/libff/libff/algebra/curves/bn128/bn128_pairing.cpp
cp libff_changes/depends/libff/libff/algebra/curves/bn128/bn128_pp.cpp depends/libff/libff/algebra/curves/bn128/bn128_pp.cpp
mkdir build && cd build && cmake  .. -DCMAKE_INSTALL_PREFIX=../
make && make install
cd ../../../

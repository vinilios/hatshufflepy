# Install libhatshuffle
git submodule init
git submodule update --recursive

if [ -d "hatshufflepy_dist/lib" ]; then
    echo "hatshuffle libs found. skipping libhatshuffle build";
    exit;
fi;
cd libhatshuffle
git fetch
git submodule update --init --recursive
git checkout aabdc03
cp ../libhatshuffle_changes/CMakeLists.txt CMakeLists.txt
cp libff_changes/depends/libff/libff/CMakeLists.txt depends/libff/libff/CMakeLists.txt
cp libff_changes/depends/libff/depends/CMakeLists.txt depends/libff/depends/CMakeLists.txt
cp libff_changes/depends/libff/libff/algebra/curves/bn128/bn128_pairing.cpp depends/libff/libff/algebra/curves/bn128/bn128_pairing.cpp
cp libff_changes/depends/libff/libff/algebra/curves/bn128/bn128_pp.cpp depends/libff/libff/algebra/curves/bn128/bn128_pp.cpp
cd depends/libff/depends/xbyak/ && git pull origin master && cd ../../../../
# Build and install
mkdir build; cd build && cmake .. -DCMAKE_INSTALL_PREFIX=../../hatshufflepy_dist/ -DCMAKE_INSTALL_RPATH="\$ORIGIN" -DDEBUG=ON -DCPPDEBUG=ON
# Use multiple cores
# mkdir build && cd build && cmake -DMULTICORE=ON .. -DCMAKE_INSTALL_PREFIX=../
make && make install
cd ../../../

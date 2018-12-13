git submodule update -f --init;
rm -rf libhatshuffle/build;
rm -rf hatshufflepy_dist/lib;
cd libhatshuffle && git submodule update -f --init; cd ..;
rm -rf build dist hatshufflepy.egg-info;
rm *.json pk sk;
rm demos/*.json demos/pk demos/sk;
rm -rf build dist;

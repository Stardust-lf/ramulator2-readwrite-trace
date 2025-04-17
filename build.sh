#cd py-scripts/
#python random_trace_generator.py
# cd ..
cd build
cmake .. -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
make -j8
cd ..
cp build/ramulator2 .
# ./ramulator2 -f exp_configs/repar_config.yaml

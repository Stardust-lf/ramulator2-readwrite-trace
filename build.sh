#cd py-scripts/
#python random_trace_generator.py
# cd ..
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
make -j8
./ramulator2 -f exp_configs/repar_config.yaml

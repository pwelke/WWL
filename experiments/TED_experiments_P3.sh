dataset=Synth_P3
o=../${dataset}

f=/opt/mlfta/ted_kernel/${dataset}
python3 ../converter/synth.py $f $o
mv ${o}/* ../data/

for f in ../data/syth*; do
  python3 main.py --dataset `basename $f` --h 5 --crossvalidation --gridsearch --repetitions 1
done

mkdir ./results/${dataset}
mv ./results/syth* ./results/${dataset}

python3 TED_experiments_Synth_parse.py ./results/${dataset}
python3 TED_experiments_Synth_parse_avg.py ./results/${dataset}

# cleanup
mv ../data/* ${o}/

mkdir ./output/${dataset}
mv ./output/syth* ./output/${dataset}

for f in COX2 BZR DHFR; do
  python3 main.py --dataset `basename $f` --h 5 --crossvalidation --gridsearch --repetitions 1
done

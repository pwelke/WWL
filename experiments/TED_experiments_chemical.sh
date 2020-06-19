#!/usr/bin/env bash

for f in MUTAG NCI1 IMDB_BINARY REDDIT_BINARY COX2 BZR DHFR; do
  python3 main.py --dataset `basename $f` --h 5 --crossvalidation --gridsearch --repetitions 1
done

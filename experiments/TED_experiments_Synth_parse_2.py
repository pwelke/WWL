import os
import numpy as np
import sys
import re

if __name__ == '__main__':
    results = sys.argv[1]

    f1 = open(os.path.join(results, 'tab_Synth1.csv'), 'w')
    f1.write('Dataset, Accuracy, std\n')

    f2 = open(os.path.join(results, 'tab_Synth2.csv'), 'w')
    f2.write('n, ee, c_min, c_max, p, p_noise, ga, j, Accuracy, std\n')

    regex = re.compile('sythetic_n(.*?)_ee(.*?)_c(.*?)c(.*?)_p(.*?)_pn(.*?)_ga(.*?)_i(.*?).p')

    for db in os.listdir(results):
        match = regex.match(db)
        if match:
            n = match.group(1)
            ee = match.group(2)
            c_min = match.group(3)
            c_max = match.group(4)
            p = match.group(5)
            p_noise = match.group(6)
            ga = match.group(7)
            j = match.group(8)

            input_file = os.path.join(results, db, 'results_' + db + '_crossvalidation_gridsearch_all1repetitions.csv')

            accs = np.loadtxt(input_file)
            f1.write(f'{db}, {np.mean(accs)}, {np.std(accs)}\n')
            f2.write(f'{n}, {ee}, {c_min}, {c_max}, {p}, {p_noise}, {ga}, {j}, {np.mean(accs)}, {np.std(accs)}\n')

    f1.close()
    f2.close()
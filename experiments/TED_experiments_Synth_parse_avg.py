import os
import numpy as np
import re
import sys

if __name__ == '__main__':
    results = sys.argv[1]

    f2 = open(os.path.join(results, 'tab_Synth_avg.csv'), 'w')
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

            # inefficient. We will copmute the same thing five times. but faster for me, right now.
            accs = list()
            for j in [1, 2, 3, 4, 5]:
                db = f'sythetic_n{n}_ee{ee}_c{c_min}c{c_max}_p{p}_pn{p_noise}_ga{ga}_i{j}.p'
                input_file = os.path.join(results, db, 'results_' + db + '_crossvalidation_gridsearch_all1repetitions.csv')

                accs.append(np.loadtxt(input_file))
            allaccs = np.stack(accs)
            allaccs.flatten()
            f2.write(f'{n}, {ee}, {c_min}, {c_max}, {p}, {p_noise}, {ga}, {np.mean(accs)}, {np.std(accs)}\n')

    f2.close()
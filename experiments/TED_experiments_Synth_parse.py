import os
import numpy as np

if __name__ == '__main__':
    results = './results/'

    n = 8
    ee = 1
    p_noise = 0.01
    ga = 200
    cs = [[1, 2], [2, 4], [4, 8], [8, 8]]
    ps = [0.25, 0.5, 0.75, 1.0]

    f1 = open(os.path.join(results, 'tab_Synth1.csv'), 'w')
    f1.write('Dataset, Accuracy, std\n')

    f2 = open(os.path.join(results, 'tab_Synth2.csv'), 'w')
    f2.write('n, ee, c_min, c_max, p, p_noise, ga, j, Accuracy, std\n')

    for j in [1, 2, 3, 4, 5]:
        for c in cs:
            for p in ps:
                [c_min, c_max] = c

                db = f'sythetic_n{n}_ee{ee}_c{c_min}c{c_max}_p{p}_pn{p_noise}_ga{ga}_i{j}.p'
                input_file = os.path.join(results, db, 'results_' + db + '_crossvalidation_gridsearch_all1repetitions.csv')

                accs = np.loadtxt(input_file)
                f1.write(f'{db}, {np.mean(accs)}, {np.std(accs)}\n')
                f2.write(f'{n}, {ee}, {c_min}, {c_max}, {p}, {p_noise}, {ga}, {j}, {np.mean(accs)}, {np.std(accs)}\n')

    f1.close()
    f2.close()
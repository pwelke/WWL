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

    # f1 = open(os.path.join(results, 'tab_Synth1.csv'), 'w')
    # f1.write('Dataset, Accuracy, std\n')

    f2 = open(os.path.join(results, 'tab_Synth3.csv'), 'w')
    f2.write('n, ee, c_min, c_max, p, p_noise, ga, Accuracy, std\n')

    for c in cs:
        for p in ps:
            [c_min, c_max] = c

            accs = list()
            for j in [1, 2, 3, 4, 5]:
                db = f'sythetic_n{n}_ee{ee}_c{c_min}c{c_max}_p{p}_pn{p_noise}_ga{ga}_i{j}.p'
                input_file = os.path.join(results, db, 'results_' + db + '_crossvalidation_gridsearch_all1repetitions.csv')

                accs.append(np.loadtxt(input_file))
            allaccs = np.stack(accs)
            allaccs.flatten()
            # f1.write(f'{db}, {np.mean(allaccs)}, {np.std(allaccs)}\n')
            f2.write(f'{n}, {ee}, {c_min}, {c_max}, {p}, {p_noise}, {ga}, {np.mean(accs)}, {np.std(accs)}\n')

    # f1.close()
    f2.close()
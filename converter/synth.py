
import os
import pickle

import egonetconverter

if __name__ == '__main__':
    source = '/opt/mlfta/ted_kernel/Synth_P1P2/'
    output = '../data/Synth_P1P2_GML/'

    # n = 8
    # ee = 1
    # p_noise = 0.01
    # ga = 200
    # cs = [[1, 2], [2, 4], [4, 8], [8, 8]]
    # ps = [0.25, 0.5, 0.75, 1.0]
    #
    # for j in [1, 2, 3, 4, 5]:
    #     for c in cs:
    #         for p in ps:
    #             [c_min, c_max] = c
    #
    #             db = f'sythetic_n{n}_ee{ee}_c{c_min}c{c_max}_p{p}_pn{p_noise}_ga{ga}_i{j}.p'

    for db in os.listdir(source):
        input_file = os.path.join(source, db)
        with open(input_file, "rb") as f:
            [G, y] = pickle.load(f)
            egonetconverter.write_graph_list(name=db, graph_list=G, data_root=output)
            egonetconverter.write_label_list(name=db, label_list=y, data_root=output)

        # # lazy persons way to create the bash script file
        # print(f'python3 main.py --dataset {db} --h 3 --crossvalidation --gridsearch --repetitions 1')
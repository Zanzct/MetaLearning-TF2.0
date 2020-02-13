import os

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

epochs = np.array(range(500, 5001, 500)) * 3
accs_mean_maml = [0.37649333477020264, 0.4036933481693268, 0.4293866753578186, 0.4558666944503784, 0.4553333818912506, 0.4556933641433716, 0.4692400097846985, 0.45899999141693115, 0.468720018863678, 0.47546666860580444]
accs_stds_maml = [0.07559756934642792, 0.08231999725103378, 0.08122657984495163, 0.08090148121118546, 0.08344738930463791, 0.08378562331199646, 0.08831232786178589, 0.08698032796382904, 0.08776765316724777, 0.09781105816364288]

accs_mean_sp = [0.34838664531707764, 0.3836800456047058,  0.4265066981315613, 0.44043999910354614,  0.45205333828926086, 0.4710133373737335, 0.4840400218963623, 0.46532002091407776, 0.47696003317832947, 0.4960800111293793]
accs_stds_sp = [0.06972244381904602, 0.08529355376958847, 0.08183001726865768, 0.07993543148040771, 0.08389918506145477, 0.08288758248090744, 0.07600139081478119, 0.07664381712675095, 0.07868023961782455,  0.08475173264741898]


def plot(x, means, stds, label):
    bands = np.array(stds) * 1.96 / np.sqrt(1000)
    plt.errorbar(x, means, yerr=bands, label=label, fmt="--o")
    plt.ylim(0.3, 0.5)


if __name__ == '__main__':
    plot(epochs, accs_mean_maml, accs_stds_maml, label='MAML')
    plot(epochs, accs_mean_sp, accs_stds_sp, label='Ours')
    plt.legend(loc='upper left', fontsize=16)
    plt.xlabel('Iterations', fontsize=16)
    plt.ylabel('Accuracy', fontsize=16)
    plt.show()
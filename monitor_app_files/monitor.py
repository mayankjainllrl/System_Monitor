"""Program for visualizing CPU and Memory usage of any Docker container"""

import matplotlib.pyplot as plt
import numpy as np
import os

name = input("Enter name of your container"
             "\nMake sure it is running and please enter correct name: ")

# Checking the validity of name given by user
all_running_processes = os.popen("docker container ls")
validity = False
for process in all_running_processes:
    if str(process).strip().split()[-1] == name:
        validity = True
        break
if validity is False:
    print("\nNo image with such name."
          "\nPlease check the name of your image using docker ps or any other command."
          "\nAnd Enter a valid name.")
    exit()

stats = os.popen(f'docker stats {name} --format "{{{{.Name}}}} {{{{.MemPerc}}}} {{{{.CPUPerc}}}}"')


def get_stats(stats):
    """
    :param stats: os object holding realtime stats of our container.
    :return: current memory and cpu percent our container using.
    """
    for stat in stats:
        return float(stat.strip().split()[1][:-1]), float(stat.strip().split()[2][:-1])


fig, ax = plt.subplots()
ind = np.arange(0, 2)
plt.show(block=False)
pm, pc = plt.bar(ind, get_stats(stats))
pm.set_facecolor('r')
pc.set_facecolor('g')
ax.set_xticks(ind)
ax.set_xticklabels(['Memory', 'CPU'])

# If Your Application is using more memory or CPU than 2%
# In that case you can replace 2 with any other number in range 2-100 according to your requirement
ax.set_ylim([0, 2])

ax.set_ylabel('Percent usage')
ax.set_title('System Monitor')

while True:
    try:
        m, c = get_stats(stats)
        pm.set_height(m)
        pc.set_height(c)
        fig.canvas.draw_idle()
        fig.canvas.flush_events()
    except:
        exit()


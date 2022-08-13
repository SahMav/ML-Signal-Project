import matplotlib.pyplot as pp
import numpy as np
import json
from spectrum import *
import scipy.io

def pie_plot():
    sizes = [1075840 - 282350, 282350]
    explode = [0, 0.1]
    labels = ['normal', 'hypertension']
    fig1, ax1 = pp.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    pp.show()

def histograms():
    ppg_dataset = np.loadtxt('parts1to6_ppg.csv', delimiter=',')
    bp_dataset = np.loadtxt('parts1to6_bp.csv', delimiter=',')
    diastolic = bp_dataset[:, 0]
    systolic = bp_dataset[:, 1]

    print(len(bp_dataset))
    hypertension = np.where(bp_dataset[:,1] > 140)
    print(len(hypertension[0]))

    # frequency, bins = np.histogram(x, bins=10, range=[0, 100])
    pp.hist(systolic, bins=90)
    pp.gca().set(title='Systolic Blood Pressure', ylabel='Frequency')
    pp.show()
    i = [_ for _ in range(len(bp_dataset))]

    pp.scatter(i, bp_dataset[:, 1], marker='o')
    pp.show()

# with open('1.json') as f:
#   data = json.load(f)
#
# pp.plot(data['data_PPG'])
# pp.show()

def test_pmtm():
    part = scipy.io.loadmat('./Data/part_1.mat')
    part_data = part['p'][0]
    record = part_data[0]
    ppg = record[0]
    bp = record[1]
    ppg_signal = ppg[29:91]
    # pp.plot(ppg_signal)
    # pp.show()

    data = data_cosine(N=2048, A=0.1, sampling=1024, freq=200)
    # If you already have the DPSS windows
    [tapers, eigen] = dpss(20, 2.5, 4)
    res = pmtm(ppg_signal,NW=0.5, k = 5, show=False)
    res = pmtm(ppg_signal,NW=0.5, k = 5, show=False)
    res = pmtm(ppg_signal,NW=0.5, k = 5, show=True)

    print(res)
    print(len(res))
    print(len(res[0]))
    print(len(res[1]))
    print(len(res[2]))
    res = pmtm(data, NW=2.5, show=False)
    res = pmtm(data, NW=2.5, k=4, show=True)
import matplotlib.pyplot as pl
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Plot golang benchmark results')
parser.add_argument('filename', metavar='filename', nargs=1,
                    help='filename containing benchmark results')

args = parser.parse_args()

values = pd.read_csv(args.filename[0], index_col = 0, usecols = [0, 1,2,3], sep='\s+', header=None, names=["index", "iterations", "time", "unit"])

values.dropna(inplace = True)

values.index = values.index.str.replace('-\\d', '').str.split('/', expand=True)

values.index.set_levels([values.index.levels[0], values.index.levels[1].astype(int)], inplace = True)

fig, ax = pl.subplots(figsize=(5, 3))

ax.set_xlabel('size')
ax.set_ylabel('time' + '  (' + values['unit'].iloc[0] + ')')

for i in values.index.get_level_values(0).unique():
    ax.plot(values['time'][i].index, values['time'][i], linestyle='-')

ax.legend(values.index.get_level_values(0).unique())

fig.savefig('output.png')

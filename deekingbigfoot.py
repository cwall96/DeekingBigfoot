import twint
import sys

c = twint.Config()

param_1 = sys.argv[1]

c.Search = [param_1]       # topic
c.Store_csv = True       # store tweets in a csv file
c.Output = "deeking.csv"     # path to csv file
c.Since = '2008-04-29'
c.Until = '2020-04-29'

twint.run.Search(c)

import pandas as pd
df = pd.read_csv('deeking.csv')
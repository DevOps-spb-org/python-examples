import pandas as pd
import numpy as np

anime = pd.read_csv('anime.csv')
rating = pd.read_csv('rating.csv')

anime_modified = anime.set_index('name')

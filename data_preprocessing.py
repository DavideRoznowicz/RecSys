import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from math import sqrt
from scipy.sparse import bsr_array


# Data Pre-Processing Script, allowing to have a dataset suitable for the project


# drop some columns such that we have a dataset suitable for this project
def drop_not_necessary_columns(df_artists, df_user_artists):
    df_artists = df_artists.drop(columns=['url', 'pictureURL'])
    df_user_artists = df_user_artists.drop(columns=['weight'])
    return df_artists, df_user_artists


# remap userID starting from 0 and having sequential and contiguous numbers (there are several users
# which do not follow any artist). We repeat a similar process for artistID. This will make it easier
# to build and index the interaction matrix
def remap(a):
    ct = -1
    cur_el = -1
    dict_idx = {}
    for el_idx in range(len(a)):
        el = a[el_idx]
        if cur_el != el:
            ct += 1
        a[el_idx] = ct
        dict_idx[el]=ct
        cur_el = el
    return a, dict_idx


def main_preprocess(df_artists, df_user_artists):
    # drop columns which are not relevant for the project
    df_artists, df_user_artists = drop_not_necessary_columns(df_artists, df_user_artists)

    # fix userID for better indexing when building the matrix afterwards
    remapped_array_user, dict_idx_user=remap(np.array(df_user_artists['userID']))
    df_user_artists['userID'] = remapped_array_user

    # fix artistID for better indexing when building the matrix afterwards
    remapped_array_artist, dict_idx_artist=remap(np.array(df_artists['id']))
    df_artists['id'] = remapped_array_artist
    new_artist_ID=np.array([dict_idx_artist[el] for el in np.array(df_user_artists['artistID'])])
    df_user_artists['artistID']=new_artist_ID

    return df_artists, df_user_artists







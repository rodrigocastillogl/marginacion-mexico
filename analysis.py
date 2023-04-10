import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from pca import pca


def pca_mi( scores, variance_ratio, m = 2):
    """
    Marginalization index based on PCA.
    Input
    -----
        * scores : scores from PCA.
        * variance_ ratio : explained variance ratio from PCA.
        * m : PC to use.
    Output
    ------
        PCA marginalization index.
    """

    return np.sum( variance_ratio[:m] * - scores[:,:m], axis = 1)

if __name__ == '__main__':

    data_path = 'data/IMM_2020.csv'
    df = pd.read_csv(data_path)

    # PCA
    loadings, scores, variance, variance_ratio = pca(df)
    
    # Marginalization index
    data_mi = np.array( df['IM_2020'] )
    new_mi  = pca_mi(scores, variance_ratio, 2)

    # Correlation 
    print( 'R: {:.4f}'.format( np.corrcoef( data_mi, new_mi )[0,1] ) )
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

def compare_mi(mi1, mi2, img_name = ''):
    """
    Linear regression with marginalization indices.
    Input
    -----
        * mi1, mi2 : marginalization indices.
        * img_name : name to save mi1 vs mi2 plot.
    Output
    -----
        * r: correlation coeffcient.
    """

    r = np.corrcoef( mi1, mi2 )[0,1]

    regressor = LinearRegression()
    regressor.fit(mi1.reshape(-1, 1), mi2.reshape(-1, 1))
    b = regressor.intercept_[0]
    m = regressor.coef_[0][0]

    plt.figure(figsize = (6,4) )
    plt.plot( [ np.min(mi1)-5 , np.max(mi1)+5 ],[ m*(np.min(mi1)-5)+b , m*(np.max(mi1)+5)+b ], alpha = 0.5, color = 'k')
    plt.scatter(mi1, mi2, color = 'silver', edgecolors = 'dimgrey', alpha = 0.6, s = 20)
    plt.xlabel('M. index 1')
    plt.ylabel('M. index 2')
    plt.tight_layout()

    if img_name == '':
        plt.show()
    else:
        plt.savefig('imgs/'+ img_name)

    return r

if __name__ == '__main__':

    data_path = 'data/IMM_2020.csv'
    df = pd.read_csv(data_path)

    # PCA
    loadings, scores, variance, variance_ratio = pca(df)
    
    # Marginalization index
    data_mi = np.array( df['IM_2020'] )
    new_mi  = pca_mi(scores, variance_ratio, 2)

    # Correlation
    r = compare_mi(data_mi, new_mi, 'comparison.png')
    print( 'R: {:.4f}'.format( r ) )
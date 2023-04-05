# PCA analysis using skl-learn

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing

def pca(data_frame):
    """
    PCA using sklearn.
    Input
    -----
        * data_frame : pandas data frame.
    Output
    ------
        * loadings : principal components vectors.
        * scores   : transformed data.
        * variance : eigenvalues/variances.
        * variance_ratio : explained variance ratio.
    """
    

    X = np.array( data_frame.loc[:,'ANALF':'PO2SM'] )
    
    # data standardization
    Xc = preprocessing.scale(X, axis = 0)
 
    # PCA
    pca = PCA()
    pca.fit(Xc)
    
    loadings = pca.components_
    scores = pca.transform(Xc)
    variance = pca.explained_variance_
    variance_ratio = pca.explained_variance_ratio_

    return loadings, scores, variance, variance_ratio


def pca_table(variance, variance_ratio):
    """
    Prints results of PCA (Variance, variance ratio).
    Input
    -----
        * variance : eigenvalues / variances.
        * variance ratio : explained variance ratio.
    Output
    ------
        * None
    """
    
    print(); print('PCA  :  Tabla de varianza expliacada')
    print('-' * 70)
    print( ' {}  |   {}   |   {}   |   {}'.format( 'Componente', 'Valor propio'   ,
                                               '% de varianza', '% acumulado' ) )
    print('-' * 70)
    
    c = 0
    for i in range( variance.shape[0] ):
        c += variance_ratio[i] * 100
        print( '{:^10d}   |       {:^.5}      |        {:^.5}      |       {:^.5}'.format(
            i + 1, '{:0.5f}'.format(variance[i]) , '{:0.5f}'.format( variance_ratio[i]*100 ) , '{:0.5f}'.format(c) ) )
    print( '-' * 70 ); print()


def plot_pc(loadings, n, img_name = '' ):
    """
    Plot n-th principal component.
    Input
    -----
        * loadings: principal components vectors (as matrix).
        * n : principl component to plot.
        * img_name: name to save image.
    Output
    ------
        * None
    """
    
    plt.figure( figsize = (6,3) )
    
    plt.plot( [ 0, loadings[n-1].shape[0]+1 ], [ 0, 0 ], color = 'dimgrey')
    for i in range(loadings[n-1].shape[0]):
        plt.plot( [ i+1, i+1 ], [ 0, loadings[n-1][i] ], color = 'silver')
        plt.text( i + 0.7, loadings[n-1][i] + np.sign(loadings[n-1][i]) * 0.05,
                  '{:.3f}'.format(loadings[n-1][i]), size = 7 )
    plt.scatter( [i for i in range(1,10)], loadings[n-1], color = 'silver', marker = 'o')
    
    plt.title( 'Componente principal {:d}'.format(n) )
    plt.xlabel(''); plt.ylabel('')
    plt.ylim( [-0.7, 0.7] )
    plt.xlim( [ 0, loadings[n-1].shape[0]+1 ] )
    plt.xticks( [i for i in range(1,10)] )
    plt.tight_layout()
    
    if img_name != '' :
        plt.savefig('imgs/' + img_name)
    else:
        plt.show()


if __name__ == '__main__':

    data_path = 'data/IMM_2020.csv'
    df = pd.read_csv(data_path)

    loadings, scores, variance, variance_ratio = pca(df)

    # table
    pca_table( variance, variance_ratio )

    # plot 1st and 2nd PC
    plot_pc( loadings, 1, 'pc1.pdf' )
    plot_pc( loadings, 2, 'pc2.pdf' )

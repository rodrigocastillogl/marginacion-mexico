# PCA analysis using skl-learn

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing

data_path = 'data/IMM_2020.csv'
df2020 = pd.read_csv(data_path)

# data matrix
X = np.array( df2020.loc[:,'ANALF':'PO2SM'] )

# data standardization
Xc = preprocessing.scale(X, axis = 0)

# PCA
pca = PCA()
pca.fit(Xc)

# scores
scores = pca.transform(Xc)
# loadings
loadings = pca.components_
# variance
variance = pca.explained_variance_
# explained variance ratio
variance_ratio = pca.explained_variance_ratio_

# ------------------- PCA results table ------------------ #
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
# -------------------------------------------------------- #

# -------------- Plot principal components --------------- #
plt.figure( figsize = (6,3) )
plt.plot( [ 0, loadings[0].shape[0]+1 ], [ 0, 0 ], color = 'dimgrey')
for i in range(loadings[0].shape[0]):
    plt.plot( [ i+1, i+1 ], [ 0, loadings[0][i] ], color = 'silver')
    plt.text( i + 0.7, loadings[0][i] + np.sign(loadings[0][i]) * 0.05,
              '{:.3f}'.format(loadings[0][i]), size = 7 )
plt.scatter( [i for i in range(1,10)], loadings[0], color = 'silver', marker = 'o')

plt.title('Primer componente principal ')
plt.xlabel(''); plt.ylabel('')
plt.ylim( [-0.7, 0.7] )
plt.xlim( [ 0, loadings[0].shape[0]+1 ] )
plt.xticks( [i for i in range(1,10)] )
plt.tight_layout()
plt.show()
# plt.savefig('imgs/componente1.pdf')

# --------------------------------------------------------- #
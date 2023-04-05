# data exploration and visualization

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def box_plot( data_frame, name = '' ):
    """
    Make boxplot with seaborn.
    Input
    -----
        * data_frame : pandas data frame.
        * name : name to save image.
    Output
    ------
        * None
    """
    
    plt.figure( figsize = (12, 8)  )
    bplot = sns.boxplot( data = data_frame, orient = "v",  fliersize = 1, color = 'silver' )
    plt.tight_layout()
    if name == '':
        plt.show()
    else:
        plt.savefig( 'imgs/' + name )


def pairs_plot( data_frame, name = '' ):
    """
    Make pairsplot with seaborn.
    Input
    -----
        * data_frame : pandas data frame.
        * name : name to save image.
    Output
    ------
        * None
    """

    plt.figure( figsize = (10, 10)  )
    pairs = sns.pairplot( data_frame, corner = True, diag_kind="kde", height = 1.4,
                          plot_kws = dict( alpha = 0.3, size = 1, color = 'silver', edgecolor = 'k'),
                          diag_kws = dict( color = 'grey' ) )
    # pairs.fig.suptitle( 'Pairs Plot', fontsize = 'xx-large' )
    plt.tight_layout()
    if name == '':
        plt.show()
    else:
        plt.savefig( 'imgs/' + name )


if __name__ == '__main__':
    
    data_path = 'data/IMM_2020.csv'
    df = pd.read_csv(data_path)

    # resume
    df.loc[:,'ANALF':'PO2SM'].describe().to_csv( 'data/resume.csv' )

    # boxplot
    box_plot( df.loc[:,'ANALF':'PO2SM'], 'boxplot.pdf')

    # boxplot
    pairs_plot( df.loc[:,'ANALF':'PO2SM'], 'pairsplot.pdf')

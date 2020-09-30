####################################################################################################
# linearly oversample a list
####################################################################################################


def linear_oversample_list(alist, factor=2):
    """Linearly oversample a list: Calculate intermediate values between the list entries using the
    given oversampling factor. The default factor of two fills the medians into the list.

    Parameters
    ----------
    alist : list
        Input list that should be oversampled.
    factor : int
        Oversampling factor. Default: 2

    Returns
    -------
    list
        Oversampled list.

    """
    import numpy as np
    
    newlist = []
    for i1,i2 in zip(alist[:-1],alist[1:]):
        newlist.append(i1)
        for n in np.arange(factor-1):
            newlist.append( i1+(n+1)/factor*(i2-i1) )
    newlist.append(alist[-1])
    return newlist


####################################################################################################
#
####################################################################################################

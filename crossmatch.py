####################################################################################################
# crossmatch lists for non-finite values
####################################################################################################

def crossmatch(*args):
    """Crossmatch lists for non-finite values.

    Parameters
    ----------
    x : list
    y : list
    ...

    Returns
    -------
    list, list
        Lists in input order with the non-finite (infinite and NaN) values removed from the list and
        also the corresponding element of the other list.

    """
    import numpy as np
    
    lists = []
    for list in args:
        lists.append( np.array(list) )

    selection = np.isfinite(lists[0])
    for list in lists[1:]:
        selection = selection & np.isfinite(list)

    matched_lists = []
    for list in lists:
        matched_lists.append( list[selection] )

    return matched_lists


####################################################################################################
#
####################################################################################################

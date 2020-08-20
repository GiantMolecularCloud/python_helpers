####################################################################################################
# flatten list of lists
####################################################################################################

def flatten(x):
    """Flatten list of lists.

    Parameters
    ----------
    x : list,tuple
        List of lists of lists of ...
        Can contain a mixture of lists and values.

    Returns
    -------
    list
        Flattened list.

    """
    import collections
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


####################################################################################################
#
####################################################################################################

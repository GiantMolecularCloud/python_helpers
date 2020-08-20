####################################################################################################
# list product
####################################################################################################

def list_product(*args):
    """
    Generate a list containing all combinations of the input lists. Outputs a list rather than an
    annoying generator.

    Parameters
    ----------
    *args : list, tuple

    Returns
    -------
    list
        Combined list.
    """
    import itertools
    return list(itertools.product(*args))


####################################################################################################
#
####################################################################################################

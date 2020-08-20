####################################################################################################
# multi-list ProgressBar
####################################################################################################

def multilist_progressbar(*lists):
    """Progress bar to replace multiple loops over multiple lists.
    Having multiple for loops is not ideal to get a good progressbar, e.g.
    for i in ProgressBar(list1):
        for j in list2:
            # do something
    Instead, it should be looped over the combination of both lists. This is what multilist_progressbar does
    for i,j in multilist_progressbar(list1, list2):
        # do something

    Parameters
    ----------
    *lists : iterable
        Two or more lists/arrays/... to be looped over.

    Returns
    -------
    Two or more elements of the input lists depending on the number of given lists.

    """
    import itertools
    from astropy.utils.console import ProgressBar

    return ProgressBar(list(itertools.product(*lists)))


####################################################################################################
#
####################################################################################################

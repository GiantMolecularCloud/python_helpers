####################################################################################################
# plot line with color gradient
####################################################################################################

def cgradient_line(x,y, ax, z=None, cmap='inferno', lw=1, **kwargs):
    """Plot line with color gradient.

    Parameters
    ----------
    x : list, array
    y : list, array
    ax : mpl axis
        Description of parameter `ax`.
    z : list, array
        Array to color by using the colormap. Optional. If not given colorcode by x.
    cmap : mpl cmap name or object
        Colormap to use. Default: inferno
    lw : int, float
        Single linewidth or list of linewidths for the color segments. Default: 1
    **kwargs
        Kwargs passed to LineCollection.
    """
    from matplotlib.collections import LineCollection
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap=cmap, linewidths=lw, **kwargs)
    if z:
        lc.set_array(z)
    else:
        lc.set_array(np.linspace(0,1,len(x)))
    ax.add_collection(lc)


####################################################################################################
#
####################################################################################################

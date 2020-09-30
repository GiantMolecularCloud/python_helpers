####################################################################################################
#  annotate lines
####################################################################################################

def label_line(ax,line,x,y,label,angle=0.,**text_kwargs):
    """Label a line.

    Parameters
    ----------
    ax : mpl axis
        The parent axis to draw the annotation onto.
    line : Line2D
        The line to annote. Note: plt.plot returns a list of lines even for a single line plotted.
    x : int,float
        x coordinate to place annotation.
    y : int,float
        y coordinate to place annotation.
    label : string
        The label text.
    angle : int,float
        The angle in degrees how much the text should be rotated relative to the line.
        Default: 0 degrees
    **text_kwargs
        kwargs for plt.text()

    Returns
    -------
    mpl.Text
        Mpl text object.
    """
    import numpy as np
    
    if type(line)==list:
        print("Got list of lines. Using first line in the list.")
        line = line[0]
    # get x/y values
    xs = line.get_xdata()
    i1 = np.argmin(np.abs(xs-x))
    i2 = i1+1
    x1,x2 = line.get_xdata()[i1:i2+1]
    y1,y2 = line.get_ydata()[i1:i2+1]
    # two points
    p1 = ax.transData.transform_point((x1, y1))
    p2 = ax.transData.transform_point((x2, y2))
    # differential
    dy = (p2[1] - p1[1])
    dx = (p2[0] - p1[0])
    # rotation
    rotation = np.degrees(np.arctan2(dy, dx))+angle
    # text
    text = ax.text(x, y, label, rotation=rotation, rotation_mode='anchor', **text_kwargs)
    return text


####################################################################################################
#
####################################################################################################

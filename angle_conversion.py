####################################################################################################
# angle conversion
####################################################################################################

def angle_to_parsec(angle, source=None, distance=None):
    """Convert an angle to a linear distance given a source or distance.

    Parameters
    ----------
    angle : astropy.unit
        Angular unit instance.
    source : str
        NGC253 or GC implemented. Either source or distance must be given.
        Default: None
    distance : astropy.unit
        Distance unit instance. Either source or distance must be given.

    Returns
    -------
    astropy.unit
        The linear distance corresponding to the given angle.
    """
    import astropy.units as u
    if (source==None) and (distance==None):
        raise Exception("Need to provide either source name or distance.")

    if ( source == 'NGC253' ):
        distance = 3.5*u.Mpc
    if ( source == 'GC' ):
        distance = 8178*u.pc
    if ( source == 'M82' ):
        distance = 3.6*u.Mpc

    return (distance*np.sin(angle)).to(u.pc)


def parsec_to_angle(parsec, source=None, distance=None):
    """Convert a linear distance to an angle given a source or distance.

    Parameters
    ----------
    parsec : astropy.unit
        Distance unit instance.
    source : str
        NGC253 or GC implemented. Either source or distance must be given.
        Default: None
    distance : astropy.unit
        Distance unit instance. Either source or distance must be given.

    Returns
    -------
    astropy.unit
        The angle corresponding to the given distance.
    """
    import astropy.units as u
    if (source==None) and (distance==None):
        raise Exception("Need to provide either source name or distance.")

    if ( source == 'NGC253' ):
        distance = 3.5*u.Mpc
    if ( source == 'GC' ):
        distance = 8178*u.pc
    if ( source == 'M82' ):
        distance = 3.6*u.Mpc

    return (np.sin((parsec/distance).to(u.dimensionless_unscaled).value)*u.radian).to(u.degree)


####################################################################################################
#
####################################################################################################

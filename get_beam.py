####################################################################################################
# get beam
####################################################################################################

def get_beam(fitsimage):
    """
    Get the beam of a fits image.

    Parameters
    ----------
    fitsimage : string or PrimaryHDU
        File name of a fits image or astropy.fits PrimaryHDU object.

    Returns
    -------
    list
        Major, minor axis and position angle as astropy.units objects.
    """

    import astropy.units as u
    from astropy.io import fits

    if isinstance(fitsimage, str):
        head = fits.getheader(fitsimage)
    elif isinstance(fitsimage, fits.hdu.image.PrimaryHDU):
        head = fitsimage.header
    else:
        raise TypeError("Unknown format for fitsimage. Must be filename or HDUList.")
    return (head['bmaj']*u.degree).to(u.arcsec), (head['bmin']*u.degree).to(u.arcsec), head['bpa']*u.degree


####################################################################################################
#
####################################################################################################

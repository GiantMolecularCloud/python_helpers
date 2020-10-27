####################################################################################################
# reproject one image on the header of another one in a single line of code
####################################################################################################

def reproject_image(image, template, outfile='auto', overwrite=True):
    """Reproject a FITS image onto another FITS image.

    Parameters
    ----------
    image : str
        File name of the FITS image to be reprojected.
    template : str
        File name of the template image to reproject onto.
    outfile : str
        File name of the reprojected image. If 'auto', '.reprojected' will be added to the file name.
        Default: 'auto'
    overwrite : bool
        Overwrite potentially existing files.
        Default: True
    """

    import numpy as np
    from astropy.io import fits
    from reproject import reproject_interp

    print("Reprojecting "+image+" onto "+template)
    print("This can take several minutes for large cubes.")

    # load files
    im_HDU   = fits.open(image)[0]
    temp_HDU = fits.open(template)[0]

    # reproject
    array, footprint = reproject_interp(im_HDU, temp_HDU.header)

    # keep some info of original image
    for n in np.arange(im_HDU['naxis']):
        n = str(n)
        for x in ['cdelt','crval','crpix','cunit']:
            im_HDU.header[x+n] = temp_HDU.header[x+n]

    # save to disk
    if outfile == 'auto':
        outfile = image.replace('.fits','.reprojected.fits')
    fits.writeto(outfile,
             data      = array,
             header    = temp_HDU.header,
             overwrite = overwrite
            )

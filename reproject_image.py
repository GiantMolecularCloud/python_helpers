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

    from astropy.io import fits
    from reproject import reproject_interp

    # load files
    image    = fits.open(image)[0]
    template = fits.open(template)[0]

    # reproject
    print("Reprojecting "+image+" onto "+template)
    print("This can take several minutes for large cubes.")
    array, footprint = reproject_interp(HI, CO.header)

    # save to disk
    if outfile == 'auto':
        outfile = image.replace('.fits','.reprojected.fits')
    fits.writeto(outfile,
             data      = reprojected,
             header    = template.header,
             overwrite = overwrite
            )

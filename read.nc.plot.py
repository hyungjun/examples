#! /usr/bin/python
#--------------------------------------------------------------------
# PROGRAM    : read.plot.nc.py
# CREATED BY : hjkim @IIS.2015-12-22 09:58:42.589355
# MODIFED BY :
#
# USAGE      : $ ./read.plot.nc.py
#
# DESCRIPTION:
#------------------------------------------------------cf0.2@20120401


import  os,sys
from    optparse                import OptionParser

from    netCDF4                 import Dataset
from    pylab                   import *
from    mpl_toolkits.basemap    import Basemap


def main(args,opts):
    print args
    print opts

    srcPath = '/data2/hjkim/GSWP3/in/EXP1/daily/Tair/GSWP3.BC.Tair.1901.nc'
    pngPath = '/home.rainbow/hjkim/public_html/temp/gswp3.tair.1901_0.png'

    nc      = Dataset( srcPath )

    Tair    = nc.variables[ 'Tair' ]

    aSrc    = Tair[0]

    print aSrc.shape, aSrc.min(), aSrc.max()

    Fig     = figure( figsize=(12,4) )
    Ax      = Fig.add_subplot(111)

    Map     = Basemap( resolution='c', llcrnrlat=-90, llcrnrlon=0, urcrnrlat=90, urcrnrlon=360 )
    Map.drawcoastlines()

    im      = Map.imshow( aSrc )

    colorbar()

    Fig.savefig( pngPath )

    return


if __name__=='__main__':
    usage   = 'usage: %prog [options] arg'
    version = '%prog 1.0'

    parser  = OptionParser(usage=usage,version=version)

#    parser.add_option('-r','--rescan',action='store_true',dest='rescan',
#                      help='rescan all directory to find missing file')

    (options,args)  = parser.parse_args()

#    if len(args) == 0:
#        parser.print_help()
#    else:
#        main(args,options)

#    LOG     = LOGGER()
    main(args,options)



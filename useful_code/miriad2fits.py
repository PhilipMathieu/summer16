#! /usr/bin/env python

import argparse
from uvdata.uv import UVData

parser = argparse.ArgumentParser()
parser.add_argument('--mir', help='Path of input Miriad file')
parser.add_argument('--fits', help='Path of output UVFits file',default='none')
args = parser.parse_args()
infile = args.mir
if args.fits == 'none':
    outfile = args.mir+'.fits'
else:
    outfile = args.fits
this_uv = UVData()
this_uv.read_miriad(infile)
this_uv.write_uvfits(outfile,True,True)
del(this_uv)

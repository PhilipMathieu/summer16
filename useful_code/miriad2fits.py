#! /usr/bin/env python

import argparse
import os
from uvdata.uv import UVData

parser = argparse.ArgumentParser()
parser.add_argument('-d',action='store_true')
parser.add_argument('mir', help='Path of input Miriad file')
parser.add_argument('-f','--fits', help='Path of output UVFits file')
args = parser.parse_args()
if args.d:
    mdir = args.mir
    files = os.listdir(mdir)
    for filename in files:
        filename = mdir+filename
else:
    files = [args.mir]
print files
for infile in files:
    if not(args.fits == None) and not args.d:
        outfile = args.fits
    else:
        outfile = infile+'.fits'
    this_uv = UVData()
    this_uv.read_miriad(infile)
    this_uv.write_uvfits(outfile,True,True)
    del(this_uv)

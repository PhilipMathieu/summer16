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
    #Check if trailing slash from autocomplete
    if files[0][-1:] == '/':
        print 'WARNING: Trailing slash, but not in directory mode.  Ignoring...'
        files[0] = files[0][:-1]
for infile in files:
    if not(args.fits == None) and not args.d:
        outfile = args.fits
    else:
        outfile = infile+'.uvfits'
    this_uv = UVData()
    this_uv.read_miriad(infile)
    #This is hacky rn but could be reworked into a more comprehensive system for
    #fixing expected problems with the input file, possibly via an input file or 
    #something that allows you to manually correct UVProperty values and such
    if this_uv.telescope_name == 'PAPER':
        if this_uv.longitude < 0:
            this_uv.telescope_name='PAPER_GB'
        else:
            this_uv.telescope_name='PAPER_SA'
    this_uv.write_uvfits(outfile,True,True)
    del(this_uv)

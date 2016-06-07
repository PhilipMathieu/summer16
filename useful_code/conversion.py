#!/usr/bin/python
#Must run in uvdata folder of pyuvdata repo (until I figure out how 
#imports work)
import sys
sys.path.append('~/src/pyuvdata/uvdata')
from uv import UVData
infile = '/home/user/data/zen.2455016.68855.uvc'
outfile = infile[0:-4]+'.fits'
test = UVData()
test.read_miriad(infile)
test.write_uvfits('./testout.fits',True,True)

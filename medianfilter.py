# python image filtering
import numpy as np
import PIL.Image as Image
import sys
import matplotlib.pyplot as plt
from readimg import ReadImage

from padding import ImagePadding

import time

def MedianFilter( f, KernelSize ):
    m = KernelSize
    n = KernelSize
    a = int(m/2)
    b = int(n/2)
    M = f.shape[0]
    N = f.shape[1]

    #padded = np.zeros( (M + 2*a, N + 2*b) )
    #padded[ a:-a, b:-b ] = f
    start = time.time()
    padded=ImagePadding(f, a, b)
    end = time.time()
    print( "padding consumed: ", end-start, 'secs' )
    #write out
    #PaddedImg=Image.fromarray(padded)
    #PaddedImg.save('padded.bmp')

    start = time.time()
    #g = np.zeros_like( f )
    g = np.empty( (M,N), dtype=f.dtype ) # same as f 
    
    for r in range( M ):
        for c in range( N ):
            v = np.median( padded[r:r+m, c:c+n] )
            g[r,c] = v

    end = time.time()
    print( "filtering consumed: ", end-start, 'secs' )
    return g


def main( fn1, fn2):
    
    f= ReadImage( fn1 )
    print( "shape of f: ", f.shape )

    KernelSize = 5

    g = MedianFilter( f, KernelSize )

    g = Image.fromarray( g )
    
    g.save( fn2 )



if __name__=='__main__':
    #sys.argv.append( "peppers.png")
    #sys.argv.append("fp.png")

    if len( sys.argv ) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print('Usage: ', sys.argv[0], "[image file 1] [image file 2]" )

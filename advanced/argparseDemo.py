import math
import argparse

def Volume(radius, height):
    volume=math.pi*(radius**2)*height
    return volume

parser=argparse.ArgumentParser(description='Calculate volume of a Cylinder')
parser.add_argument('-r', '--radius', type=int, metavar='',default=2, help='Radius of the Cylinder')
parser.add_argument('-H', '--height', type=int, metavar='Height',required='true', help='Height of the Cylinder')
group=parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',dest='qu',action='store_true',help='print quiet')
group.add_argument('-v','--verbose',action='store_true',help='print verbose')
args=parser.parse_args()

if __name__== '__main__':
    vol=Volume(args.radius,args.height)
    if args.qu:
        print(vol)
    elif args.verbose:
        print("Volume of the cylinder with radius {} & height {} is {}".format(args.radius,args.height,vol))
    else:
        print("Volume of Cylinder is %s" %vol)



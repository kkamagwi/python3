import argparse


def abc(a, b):
    if  a == 'Hello':
        print('foo')

    if b == 'World':
        print('bar')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-f','--foo', help='Description for foo argument', required=True)
    parser.add_argument('-b','--bar', help='Description for bar argument', required=True)
    args = vars(parser.parse_args())

abc(args['foo'], args['bar'])

# python3 opt.py -f foo -b World
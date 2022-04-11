from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.ticker as ticker

plt.grid(True)

#render funcs and const
e = 2.718281
pi = 3.14159

def log(x, base):
    return np.log(x)/np.log(base)

def lg(x):
    return np.log(x)/np.log(10)

def ln(x):
    return np.log(x)

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tg(x):
    return np.tan(x)

def ctg(x):
    return 1/np.tan(x)

def arcsin(x):
    return np.arcsin(x)

def arccos(x):
    return np.arccos(x)

def arctg(x):
    return np.arctan(x)

def arcctg(x):
    return np.pi/2 - np.arctan(x)

def setPoint(x,y, arrX, arrY):
    arrX.append(x)
    arrY.append(y)

def createAxis(ax):
    ax.axhline(y=0, color='k')   
    ax.axvline(x=0, color='k')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
print('Choose function of this programm:\n1.Draw 2D graph\n2.Draw 3D graph\n3.Draw graph by points')
variant = input()
if(variant == '1'):
    print('Write func to show:')
    func = input()
    plt.title('y = ' + func)
    func = func.replace('^', '**')

    x = np.arange(-50, 50, 0.01)
    y = eval(func)

    #render window
    plt.axis('equal')
    ax = plt.gca()
    createAxis(ax)
    ax.set_ylim(-75, 75)
    ax.set_xlim(-75, 75)
    plt.plot(x,y, c = 'r')
    ax.set_xlabel('x', horizontalalignment='right', x=1.0)
    ax.set_ylabel('y', verticalalignment='top', y=1.0)
elif(variant == '2'):
    print('Write func to show:')
    func = input()
    plt.title('z = ' + func)
    func = func.replace('^', '**')
    
    xar = np.arange(-20, 20, 0.01)
    yar = np.arange(-20, 20, 0.01)
    x, y = np.meshgrid(xar, yar)

    z = eval(func)

    plt.axis('equal')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap='plasma')
elif(variant == '3'):
    title = 'Title'
    xlabel = 'x'
    ylabel = 'y'
    print('Whold you like to config this graph?(y/n)')
    anwser = input()
    if(anwser == 'y'):
        print('To continue enter "stop"')
        query = ''
        print('To change title: cht "title"\nTo change label Ox: chx "xlabel"\nTo change label Oy: chy "ylabel"\n')
        while(query != 'stop'):
            query = input()
            if(query.startswith('cht')):
                title = query.split(' ')[1].replace('"', '')
            elif(query.startswith('chx')):
                xlabel = query.split(' ')[1].replace('"', '')
            elif(query.startswith('chy')):
                ylabel = query.split(' ')[1].replace('"', '')
            else:
                pass
    else:
        pass
    arrX = []
    arrY = []
    coords = ''
    print('Enter coords of points (Enter "stop" to end this)')
    ax = plt.gca()
    createAxis(ax)
    ax.set_ylim(0, 10)
    ax.set_xlim(0, 10)
    while(coords != 'stop'):
        try:
            coords = input().split(';')
            x = coords[0].replace('(', '')
            y = coords[1].replace(')', '')
            setPoint(float(x),float(y),arrX,arrY)
        except:
            break
    plt.plot(arrX,arrY, c = 'r')
    plt.title(title)
    ax.set_xlabel(xlabel, horizontalalignment='right', x=1.0)
    ax.set_ylabel(ylabel, verticalalignment='top', y=1.0)
plt.show()

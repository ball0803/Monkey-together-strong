import matplotlib.pyplot as plt
from matplotlib import animation, rc
import random
import math

def main():
    import sys
    # check if this code is running in colab
    in_colab = 'google.colab' in sys.modules
    
    random.seed(1111)
    W, H = 120, 100
    # 200 birds on a WxH window
    x,y,dx,dy = gen_data(200, W, H)

    fig = plt.figure(figsize=(4*W/H, 4))
    anim = animation.FuncAnimation(fig, animate, 
                    fargs=(x, y, dx, dy, W, H),
                    frames=(60 if in_colab else None), 
                    repeat=False, interval=50)
    if in_colab:
        rc('animation', html='jshtml')
        return anim
    else:
        plt.show()

def animate(n, x, y, dx, dy, W, H):   
    NOISE = 0.3        # +/- direction noise radians
    R = 0.10*min(W, H) # neighbors within R
    V = 0.02*min(W, H) # velocity -> displacement in each time step  
    move_all(x, y, dx, dy, V, W, H)
    ax = [0.0]*len(x)
    ay = [0.0]*len(x)
    for k in range(len(x)):
        ax[k],ay[k] = neighbor_average_direction(x, y, dx, dy, k, R)
        t = math.atan2(ay[k],ax[k]) + (NOISE - 2*NOISE*random.random())
        ax[k] = math.cos(t)
        ay[k] = math.sin(t)
    dx[:] = ax   # update the orginal dir vector
    dy[:] = ay
    plt.clf()    # clear figure
    plt.quiver(x, y, dx, dy) # plot a 2D field of arrows
    plt.xlim((0, W))
    plt.ylim((0, H))

#-------------------------------------------
# HW5: Vicsek Model
# ID: Name

def gen_data(N, W, H):
    x = [random.random() * W for _ in range(N)]
    y = [random.random() * H for _ in range(N)]
    dx = [math.cos(random.random() * 360)  for _ in range(N)]
    dy = [math.sin(random.random() * 360)  for _ in range(N)]
    return x, y, dx, dy

#-------------------------------------------
def fit_on_screen(limiter: int, val):
    if limiter >= val >= 0:
        return 0
    
    mul = -1 if val > limiter else 1
    return mul * limiter

def move_all(x, y, dx, dy, d, W, H):
    for i, p in enumerate(zip(dx, dy)):
        ndx, ndy = p
        x[i] += d * ndx
        x[i] += fit_on_screen(W, x[i])
        
        y[i] += d * ndy
        y[i] += fit_on_screen(H, y[i])


#-------------------------------------------
def neighbor_average_direction(x, y, dx, dy, k, R):
    in_focus_x = []
    in_focus_y = []
    center_x = x[k]
    center_y = y[k]
    for i, p in enumerate(zip(x, y)):
        s_x, s_y = p
        if center_x + R >= s_x >= center_x - R and \
            center_y + R >= s_y >= center_y - R:
            in_focus_x.append(dx[i])
            in_focus_y.append(dy[i])
    
    return (sum(in_focus_x)/len(in_focus_x)), (sum(in_focus_y)/len(in_focus_x))


#-------------------------------------------
main()


import numpy as np


# 拟合 y = wx + b
def compute_totalerro(b, w, points):
    totalError = 0
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (w*x + b))**2
    return totalError/float(len(points))

def step_gradient(b_cur, w_cur, points, learning_rate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N)*(y - (b_cur + w_cur*x))
        w_gradient += -(2/N)*x*(y - (b_cur + w_cur*x))
    new_b = b_cur - learning_rate*b_gradient
    new_w = w_cur - learning_rate*w_gradient
    return [new_b,new_w]

def gradient_decent_runner(points, starting_b, starting_w, learning_rate, num_iterations):
    b = starting_b
    w = starting_w
    for i in range(num_iterations):
        b,m = step_gradient(b, m, np,array(points), learning_rate)
        return [b, m]

def run():
    points = np.genfromtxt("data.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0
    initial_w = 0
    num_iterations = 1000
    print("start gradient decent at b:{0} w:{1} error:{2}".format(initial_b, initial_w,
        compute_totalerro(initial_b, initial_w, points) )
          )
    print("Running")
    [b, w] = gradient_decent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After {0}gradient decent, b={1}, w={2}, error={3}".
          format(num_iterations, b, w, compute_totalerro(b, w, points))
          )

if __name__ == "__main__":
    run()

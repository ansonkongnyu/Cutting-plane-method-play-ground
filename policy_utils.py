import numpy as np


def minmax_normalize(array, axis = 0):
    return np.nan_to_num((array - np.min(array, axis))/(np.max(array,axis = 0)- np.min(array, axis)))

class Optimizer(object):
    def __init__(self, pi):
        self.dim = pi
        self.t = 1
    def _compute_step(self, globalg):
        raise NotImplementedError


class SGD(Optimizer):
    def __init__(self, pi, stepsize):
        Optimizer.__init__(self, pi)
        self.stepsize = stepsize

    def _compute_step(self, globalg):
        step = -self.stepsize * globalg
        return step


class Adam(Optimizer):
    def __init__(self, pi, stepsize, beta1=0.9, beta2=0.999, epsilon=1e-08):
        
        Optimizer.__init__(self, pi)
        self.stepsize = stepsize
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = np.zeros(self.dim, dtype=np.float32)
        self.v = np.zeros(self.dim, dtype=np.float32)


        
    def compute_step(self, globalg):
        a = self.stepsize * np.sqrt(1 - self.beta2 ** self.t) / (1 - self.beta1 ** self.t)
        self.m = self.beta1 * self.m + (1 - self.beta1) * globalg
        self.v = self.beta2 * self.v + (1 - self.beta2) * (globalg * globalg)
        step = -a * self.m / (np.sqrt(self.v) + self.epsilon)
        return step
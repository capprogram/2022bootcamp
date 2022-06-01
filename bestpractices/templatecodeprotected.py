"""
This template code is intended to provide practice in debugging, speed 
optimization, and spotting bad habits in programming. The code runs but 
is deeply flawed. If you improve the code following all the best practices 
you know, you'll learn something about both programming and the Central 
Limit Theorem.

Author: Sheila Kannappan
Last modified: September 2019
"""

# standard imports and naming conventions; uncomment as needed
import numpy as np              # basic numerical analysis
import matplotlib.pyplot as plt # plotting
import scipy.stats as stats     # statistical functions
#import pdb                      # python debugger
#import time                     # python timekeeper

def gaussfunc(xvals, mean, sigma):
    y = np.exp(-1.*(((xvals-mean)**2) / (2.* sigma**2)))
    norm = 1./np.sqrt(2. * sigma**2 * np.pi)
    y = norm * y
    return y

def main():
    U = 8. # underlying rate of gym users per hour 
    Nct = np.array([6, 36, 216, 1296]) # total number of people counted (powers of 6)
    nhr = Nct/U # time to count this many people
    #labelarr = ["count for %s hr" % ihr for ihr in nhr]
    
    for i in range(0, len(Nct)):
        
        # plot probabilities of count values for range around mean
        mean = Nct[i]
        maxval = 2*mean
        xvals=np.arange(0, maxval)
        def poissonfunc(xvals, mean):
            prob=np.zeros(len(xvals))
            for j in range(0, len(xvals)):
                prob[j] = stats.poisson.pmf(xvals[j], mean)            
            return prob
        prob = poissonfunc(xvals, mean)
        plt.plot(xvals, prob, 'r', lw=3)
        plt.xlabel("count value")
        plt.ylabel("probability")
        plt.xscale("log")
        sel = np.where(np.isclose(prob,max(prob)))
        n = xvals[sel]
        probval = prob[sel]
        label = "count for %s hr" % (nhr[i])
        plt.text(n, probval, label)

    # plot Gaussian distribution with matching mean and sigma
    sigma=np.sqrt(mean)
    y = gaussfunc(xvals, mean, sigma)
    plt.plot(xvals, y, 'b')
    #plt.xlim([,])
    
if __name__ == '__main__':
    main()
    plt.show()

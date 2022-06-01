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
    y = np.exp(-1.*(((xvals-mean)/sigma)**2 / 2.)) # perform square once
    norm = 1./(np.sqrt(2. * np.pi) * sigma) # remove extra square operation
    y = norm * y
    return y

def poissonfunc(xvals, mean):   # move function out of loop to top of code
    prob=stats.poisson.pmf(xvals, mean) # use array math instead of loop
    return prob # note that defining this function proved entirely unnecessary,
                # could just use "stats.poisson.pmf" instead of poissonfunc

def main():
    # rename single-letter variables U, N, n -- note that "n" is a command for pdb!
    Urate = 8. # underlying rate of gym users per hour 
    Nct = np.array([6, 36, 216, 1296]) # total number of people counted (powers of 6)
    nhr = Nct/Urate # time to count this many people
    # uncomment below to do array string operation
    labelarr = ["count for %s hr" % ihr for ihr in nhr]
    
    for i in range(0, len(Nct)):
        
        # plot probabilities of count values for range around mean
        mean = Nct[i]
        maxval = 2*mean
        xvals=np.arange(0, maxval)
        prob = poissonfunc(xvals, mean)
        plt.plot(xvals, prob, 'r', lw=3)
        sel = np.where(np.isclose(prob,max(prob)))
        sel = sel[0]
        nsel = np.mean(xvals[sel]) # if ties in maxprob, take mean xval
        probval = prob[sel[0]] # if ties in maxprob, just need one
        plt.text(nsel, probval, labelarr[i]) # use labelarr instead of looping over string operation
        # the lines below needed to be in the loop
        # plot Gaussian distribution with matching mean and sigma
        sigma=np.sqrt(mean)
        y = gaussfunc(xvals, mean, sigma)
        plt.plot(xvals, y, 'b')
    
    # these labels didn't need to be in the loop
    plt.xlabel("count value")
    plt.ylabel("probability")
    plt.xscale("log")
    plt.xlim([10,100])

if __name__ == '__main__':
    main()
    plt.show()

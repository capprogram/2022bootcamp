'''
Frequentist and Bayesian Model Selection Tutorial
by Sheila Kannappan, adapted from course materials June 2017 - updated June 2021
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# you are given a file of input data xx and yy; the uncertainties are unknown
# but believed to be mostly in the y direction

# load the data and plot it
input = np.load('xydata.npz')
xx = input['xx']
yy = input['yy']
#plt.figure(1)
#plt.clf()
#plt.plot...

# suppose we wish to determine whether a 2nd order model (quadratic) 
# would be superior to a 1st order model (line) for this data set 

# perform 1st and 2nd order fits using np.polyfit
# please use the variable name convention below and set cov=True so you
# can estimate the errors later on in the tutorial

#pfit1, covp1 = ?? 
#pfit2, covp2 = ??

# compute the rms, chi^2, and reduced chi^2 for each of the fits
# (here you'll have to assume a value for the errors -- you can't estimate 
# them from the rms around one of the fits as you'd get a different answer 
# for the 1st and 2nd order fits, biasing the comparison of reduced chi^2)
errs = 2. # try 2 for starters

#print("rms1 %0.2f" % ???
#print("rms2 %0.2f" % ???
#chisq1 = ???
#chisq2 = ???
#redchisq1 = ???
#redchisq2 = ???

# uncomment line below once you have the variables redchisq1 & redchisq2
#print("reduced chi^2 for 1st order fit = %0.2f and for 2nd order fit = %0.2f" % (redchisq1,redchisq2))

# what is wrong with the reduced chi^2 values? 
# adjust your error bar assumption to fix the problem and re-run

# plot the two fits over the data

xtoplot = np.linspace(2,16,10)
#plt.plot(xtoplot,???
#plt.plot(xtoplot,???

# which fit order is preferred based on this analysis? 

# use stats.chi2.ppf to find the expected 1 & 2 sigma variation of the reduced
# chi^2 value around 1.0 based on the variation of data around the correct 
# model for that data
# here is the calculation for 1 sigma for a 1st order model to get you started
# (notice that ppf returns chi^2, not reduced chi^2)
#print(stats.chi2.ppf(0.68, len(xx)-2) / (len(xx)-2))



# how confident are you in your choice of fit order?


# Google the "Akaike Information Criterion" (AIC) on the use of chi^2 to
# compare models -- notice that since the smallest AIC = Chi^2 +2k "wins", the
# smallest chi-squared may or may not win, depending on how much the number
# of model parameters k changes. There is a penalty for adding parameters.
#print("AIC for order 1: %0.2f" % (chisq1 + ???))
#print("AIC for order 2: %0.2f" % (chisq2 + ???))
# in our example, which fit order wins according to the AIC?


'''
side note: if we had wanted to assume a mix of error in xx and error in yy,
we could have used scipy.odr (orthogonal distance regression) which supports
polynomial fitting and user-supplied functions -- for details see
http://docs.scipy.org/doc/scipy/reference/odr.html and
http://blog.rtwilson.com/orthogonal-distance-regression-in-python/
'''

# Now let's consider Bayesian model comparison.
# The basic method is summarized in the short Introduction at the top of
# https://revbayes.github.io/tutorials/model_selection_bayes_factors/bf_intro.html
# Essentially, we wish to compute the "odds ratio" or "Bayes Factor"
# favoring a first-order model (M1) over a second-order model by marginalizing
# over all possible model parameter values (and multiplying by any prior 
# belief about their relative likelihood of being correct; here we'll assume
# equal prior likelihood for 1st and 2nd order models).
# Below is a code block you can study, then uncomment with two Bayesian
# likelihood grid calculations for 1st and 2nd order model parameters,
# assuming flat priors within a grid of parameter values from -4*err to +4*err
# around the MLE best fit parameter values from the frequentist analysis.

'''
ndata=len(xx)
nalpha=100
nbeta=100
alphaposs = np.linspace(pfit1[0]-4.*np.sqrt(covp1[0,0]),pfit1[0]+4.*np.sqrt(covp1[0,0]),nalpha)
betaposs = np.linspace(pfit1[1]-4.*np.sqrt(covp1[1,1]),pfit1[1]+4.*np.sqrt(covp1[1,1]),nbeta)
range_alpha = (8.*np.sqrt(covp1[0,0]))
range_beta = (8.*np.sqrt(covp1[1,1]))
prior_alpha = 1./range_alpha # set priors so that total integrated prob = 1 
prior_beta = 1./range_beta
prior_1storder = prior_alpha*prior_beta
modelgridterm1 = alphaposs.reshape(1,nalpha) * xx.reshape(ndata,1) 
modelgrid = modelgridterm1.reshape(ndata,nalpha,1) + betaposs.reshape(nbeta,1,1).T
residgrid = yy.reshape(ndata,1,1) - modelgrid
chisqgrid = np.sum(residgrid**2/errs**2,axis=0)        
lnpostprob1 = (-1./2.)*chisqgrid + np.log(prior_1storder) 

ndata=len(xx)
np0=100
np1=100
np2=100
p0poss = np.linspace(pfit2[0]-4.*np.sqrt(covp2[0,0]),pfit2[0]+4.*np.sqrt(covp2[0,0]),np0)
p1poss = np.linspace(pfit2[1]-4.*np.sqrt(covp2[1,1]),pfit2[1]+4.*np.sqrt(covp2[1,1]),np1)
p2poss = np.linspace(pfit2[2]-4.*np.sqrt(covp2[2,2]),pfit2[2]+4.*np.sqrt(covp2[2,2]),np2)
range_p0 = (8.*np.sqrt(covp2[0,0]))
range_p1 = (8.*np.sqrt(covp2[1,1]))
range_p2 = (8.*np.sqrt(covp2[2,2]))
prior_p0 = 1./range_p0 # set priors so that total integrated prob = 1 
prior_p1 = 1./range_p1
prior_p2 = 1./range_p2
prior_2ndorder = prior_p0*prior_p1*prior_p2
modelgridterm1 = p0poss.reshape(1,np0) * xx.reshape(ndata,1)**2
modelgridterm2 = modelgridterm1.reshape(ndata,np0,1) + (p1poss.reshape(np1,1,1).T * xx.reshape(ndata,1,1))
modelgrid = modelgridterm2.reshape(ndata,np0,np1,1) + p2poss.reshape(np2,1,1,1).T
residgrid = yy.reshape(ndata,1,1,1) - modelgrid
chisqgrid = np.sum(residgrid**2/errs**2,axis=0)        
lnpostprob2 = (-1./2.)*chisqgrid + np.log(prior_2ndorder) 
'''

# marginalize over all parameters in the two posterior distributions to
# decide whether the Bayesian odds favors a 1st or 2nd order model --
# note that the "implicit" prior set by the allowed parameter ranges
# matters now and so do the "dparams" in the integral (i.e. the widths 
# "dx" of the parameter increments in the integral)
#postprob1=np.exp(lnpostprob1)
#dalpha = range_alpha/nalpha
#dbeta = range_beta/nbeta
#integral1 = np.sum(postprob1*dalpha*dbeta)
#postprob2= ???
#dp0 = ???
#dp1 = ???
#dp2 = ???
#integral2 = ???
#odds = integral1 / integral2


# uncomment below once you have defined "odds"
#print("Bayesian odds favoring a 1st order over a 2nd order model: %0.2f" % odds)

# consult https://www.statisticshowto.com/bayes-factor-definition/
# to interpret the odds ratio (Bayes Factor) you found for the two models --
# does your result agree with your earlier result based on chi^2 analysis? 
# discuss the confidence levels in each analysis


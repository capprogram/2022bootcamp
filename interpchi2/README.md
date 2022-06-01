# Interpreting &chi;<sup>2</sup>

This tutorial should be completed with reference to [these companion slides](https://github.com/capprogram/2021bootcamp/blob/master/BasicStatsIII.pdf) and is an optional prequel to the tutorial on [ _parameter estimation by maximum likelihood model fitting_](https://github.com/capprogram/2021bootcamp/blob/master/fitting-basic/README.md) discussed in the same slides.<br>

Author: Sheila Kannappan (with prior major contributions from Kathleen Eckert, Rohan Isaac, and Amy Oldenberg)<br>
Last Modified: June 2021<br>

To complete this tutorial, download the code [here](https://github.com/capprogram/2021bootcamp//blob/master/interpchi2/interpretingchi2.py) and modify/run it (ideally in the Spyder app for Anaconda Python 3) with reference to the instructions below.

Computing the &chi;<sup>2</sup> value is useful for determining whether a model is consistent with a data set within its errors. Most (astro)physicists define &chi;<sup>2</sup> as &Sigma;<sub>i</sub>(O<sub>i</sub> - E<sub>i</sub>)<sup>2</sup>/&sigma;<sub>i</sub><sup>2</sup> where O<sub>i</sub>, E<sub>i</sub>, and &sigma;<sub>i</sub> are the Observed and Expected values and the errors. In other words, the numerator represents the actual residuals between the data and the model, and the denominator represents the expected residuals assuming Gaussian-distributed errors. (Note however that in online discussions, &chi;<sup>2</sup> is generally defined with an E<sub>i</sub> in the denominator, which represents the special case of Poisson-distributed data.) 

To see how the &chi;<sup>2</sup> value can serve as a test, consider that if the model is correct and the errors have been correctly estimated, &chi;<sup>2</sup> ≈ df, where df is the number of degrees of freedom (number of data points N minus number of parameters in the model k). Therefore scientists often speak loosely and say that if the “reduced” Chi-squared defined as &chi;<sup>2</sup>/df is approximately equal to 1, then the fit is good. But let’s take a closer look. Open and work through the code you downloaded, uncommenting/modifying/adding code as needed and actually answering the questions embedded in the code as comments.

(a) Using Monte Carlo methods, create 1000 fake data sets following the underlying functional form y=1/x for x = 1, 2, 3…30 with Gaussian random errors on y of amplitude 0.1. Each data set defines one value of &chi;<sup>2</sup> by its residuals from the function y=1/x, and the 1000 values of &chi;<sup>2</sup> from all of the data sets can be divided by df and binned into a histogram to show you the reduced &chi;<sup>2</sup> distribution, which is a well-defined function analogous to a Gaussian or any other function. Note that y=1/x has no free parameters, so df is just the # of data points N=30.

(b) Now create 1000 fake data sets each with 300 values of x = 1.1, 1.2, 1.3… 30.9, using the same function y=1/x with the same errors of 0.1 on y. Overplot the new histogram of reduced &chi;<sup>2</sup> values for N=300. Is a reduced &chi;<sup>2</sup> of 1.3 equally good for both data sets? Google the functional form of the &chi;<sup>2</sup> distribution on the web to understand why in mathematical terms.

(c) This exercise shows that just knowing that the reduced &chi;<sup>2</sup> ≈ 1 does not tell you how good your model is. You must know the number of degrees of freedom (N-k). If you do, you can compute confidence levels by integrating the probability under the normalized &chi;<sup>2</sup> distribution up to your measured &chi;<sup>2</sup>. Use np.argsort to do this approximately with the &chi;<sup>2</sup> distributions from your Monte Carlo.

If you get really stuck, consult [these solutions](https://github.com/capprogram/2021bootcamp//blob/master/interpchi2/interpretingchi2.py.solns), but not 'til your puzzler is sore.

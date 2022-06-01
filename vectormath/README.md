Created by D. Carr - June 2021

# Vector Math and Broadcasting

Please read [this link](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/Broadcasting.html) up until the end of the section titled "The Final Answer, At Last!". This page will go over how mathematical operations on arrays of different shapes will turn out. It is fairly thorough with examples so I would recommend following along with the code in python/spyder yourself to test out some of the broadcasting. You do not have to do the blue rectangles labeled "Reading Comprehension" but I would consider at least reading over them and thinking critically about them. Below are some additional tips that may be nice to know as you follow along with this document:

In another tab on this same website, they formally define "Vectorized Operations". Read over this definition:
________________________________________________________
_Recall that NumPy’s ND-arrays are homogeneous: an array can only contain data of a single type. For instance, an array can contain 8-bit integers or 32-bit floating point numbers, but not a mix of the two. This is in stark contrast to Python’s lists and tuples, which are entirely unrestricted in the variety of contents they can possess; a given list could simultaneously contain strings, integers, and other objects. This restriction on an array’s contents comes at a great benefit; in “knowing” that an array’s contents are homogeneous in data type, NumPy is able to delegate the task of performing mathematical operations on the array’s contents to optimized, compiled C code (C is another coding language). This is a process that is referred to as vectorization. The outcome of this can be a tremendous speedup relative to the analogous computation performed in Python, which must painstakingly check the data type of every one of the items as it iterates over the arrays, since Python typically works with lists with unrestricted contents._

In other words, vectorizing your code speeds it up by not using indexing, looping, etc. Often times, vectorizing your code can make it run more than 50x as fast as if you did the same thing without vectorization. For simple problems, it may not make much of a difference, but it will definitely be noticeable if you are using large datasets.
_______________________________________________________________________________________

Some tips for two sections in the Broadcasting link itself

**Rules of Broadcasting**: While this section is pretty straight-forward, just be sure to get into the habit of checking the results after you do some vector math to make sure the output is as you expected. Since vector math with numpy arrays is "smart" in that it figures out how to handle the mathematical operations, that means it may not return an error when it is doing something you don't expect. Checking the input and output while broadcasting would be your best bet to avoid any mistakes. 


**Optimized Pairwise Distances**: Do not feel the need to do the part that says "It is left to the reader to show that computing this sum...". You may just take that as an accepted identity and continue along with the guide. 




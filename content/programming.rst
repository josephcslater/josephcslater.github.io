Why Matlab Users Should be Moving to Python
############################################

:date: 2015-Jun-08 23:21 EDT
:tags: Python, Scipy, Numpy, Octave, Matlab
:category: Programming
:slug: moving-to-python
:author: Joseph C. Slater
:summary: Why I'm moving to Python after 25 years of Matlab_
:Status: published

Back in 1989, when I first entered graduate school as an engineering student, I knew a handful of
languages to some modest degree. For the sake of computations, I knew Basic and
Fortran 77 (the horror!). During that first year I was assigned a project that required
substantial programming (for my skill set at the time). This project was almost
complete with about an hour to go before the deadline. Unfortunately, this was
the days of floppy drives (it was not a personally owned PC). I accidentally
stepped on the switch on a power strip and damaged the files beyond my
capability to recover them.

With about an hour to go a fellow graduate student, Jeff
Umland- now of JPL, suggested that perhaps I should heed his advice and use
Matlab_. [#]_ *The project would be simple* in Matlab_ according to him. There was
certainly no way I could complete the project in Fortran 77 in the remaining time. So, with him
responding to my shouted out questions (learning under fire - ''How do you write a loop?'') I started  using
Matlab_ and finished with time to spare. That was the last time I started a
project using Fortran. Fortran has its place (although it seems to be slowly fading away), but it has been clear to me ever
since that for most problems facing me, and most engineers, time of development far exceeds time of
program execution. When it doesn't, your prototype in a scriptable language is still not a bad first start. So, the speed cost of using an interpreted language was well worth
the savings in development time.

Unfortunately, this can build some bad habits that I am still working
through. Nevertheless, I continued to learn Matlab_ and later wrote the
`Engineering Vibration Toolbox`_ in Matlab_. I immediately noticed that
in Matlab_ each function is the name of a file, an once that file is in
the path, you can have a clash of names (namespaces_ are a major improvement with Python_). Over the years many of my
programs have been broken because of the shared name space, which
continues to grow. Names such as *addpath*, *spectrum*, *plot3*,
etc. have been replace by Mathworks m-files. Further, when I
distribute a code, I have to be concerned about their
clashes. Fortunately I was savvy enough to effectively create my own
name space for the `Engineering Vibration Toolbox`_ to name each and
every file **vtb#_#.m**, hoping that my starting them with *vtb* they
would remain safe. That seems to have stood the test of time, but no function has a name that can be reasonably guessed. They just have ugly serial numbers.

So, although the names stood the test of time,  many of
my programs written for personal (not for distribution) use did not. I've become further
disenfranchised by the lack of ability for me to truly own my own
codes. Without a Matlab_ license, until *Octave* came around, your
M-files were of little value if you didn't continue to
pay the MathWorks for a license. I appreciate the effort that they put into writing
Matlab_, but I put time into my code as well and I am not willing to be hostage to them. My code doesn't exist without me paying the MathWorks to use it. That means it's not truly my code.

As some might guess, I later switched to Octave_. Ironically, what I
liked the best about Octave_ initially was that it wasn't a Matlab_
clone, but nominally equivalent for most tasks. As time has progressed the author, John Eaton, has acquiesced to
public pleading and moved further and further towards Matlab_
compatibility. [#]_ While I respect why he made the move, for my
interests it downgraded Octave_, although
I'm likely a minority, but it is likely the right decision for the Octave_ ecosystem.

I still love Octave_ and have great respect for the John (he is
certainly a much more accomplished programmer), but I
noticed Python_ and that it seemed to really be taking scientific programming to
another level after `Travis Oliphant created NumPy`_. The add-on packages for scientific programming are extensive. The language isn't
designed to be purely for computation/data manipulation, but in many
respects, it's better, IMHO. Instead of rehashing arguments, I'll redirect you to
the opinions of `Pyzo
<http://www.pyzo.org/python_vs_matlab.html>`_, `Hoyt Koepke
<https://www.stat.washington.edu/~hoytak/blog/whypython.html>`_, and
`Phillip M. Feldman
<http://phillipmfeldman.org/Python/Advantages_of_Python_Over_Matlab.html>`_. Further, as scientific support for Python_ continues, the speed penalty compared to a compiled language is disappearing_.  I
personally love the readability of the code, and that prevents mistakes. It just looks good. `PEP 8`_ and other standards can seem onerous to new users, but in time they prove their value in generating code that is more easily readable and debuggable. Installing scientific tools is easy with modern distributions documented at NumFOCUS_, and other packages (including my own) can be easily installed from PyPI_  using PIP_.



I will likely use them (Matlab_/Octave_) again in the future. However, Python_ has empowered
me to generate more capable code than I ever could in Matlab_ due to
Matlab_'s limitations and focus. Python_'s malleability for such a wide variety of tasks has made it the `best single language`_ to learn, IMHO. It will often not be the best language for a single task. However, it is good enough often enough that if you are going to learn a single language, Python_ is your best bet for your multi-tool. If you have time to learn multiple languages, and have specific needs, by all means grow your language skills as necessary. However, if you spend little time programming, Python_ is likely the most power you can get for the time you have available.

Incidentally, and I made this blog in Python_, using Pelican_, writing
the source files in ReST_.

.. [#] I have always been a bit stubborn in my opinion. I think I'd made some positive strides as I've grown older.

.. [#] Ironically, early on he observed clear reluctance on my part
       to convert to the Octave_ standards of
       Octave_'s help system compared to Matlab_. I think he missed the moment when I came to agree with him about that and other things! I'm sorry!


.. _disappearing: https://www.ibm.com/developerworks/community/blogs/jfp/entry/A_Comparison_Of_C_Julia_Python_Numba_Cython_Scipy_and_BLAS_on_LU_Factorization?lang=en
.. _Octave : http://www.octave.org
.. _Matlab : http://www.mathworks.com
.. _Engineering Vibration Toolbox : http://www.vtoolbox.com
.. _Python : https://www.scipy.org/install.html
.. _Pelican: http://getpelican.com/
.. _ReST : http://docutils.sourceforge.net/rst.html
.. _`PEP 8`: https://www.python.org/dev/peps/pep-0008/
.. _PyPI: https://pypi.python.org/pypi
.. _pip: https://pip.pypa.io/en/stable/
.. _`best single language`: http://www.bestprogramminglanguagefor.me/why-learn-python
.. _NumFOCUS:  https://www.numfocus.org
.. _namespaces: http://www.python-course.eu/namespaces.php
.. _`Travis Oliphant created NumPy`: https://en.wikipedia.org/wiki/NumPy

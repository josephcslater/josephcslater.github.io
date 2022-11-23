Why I Moved to Python From Proprietary Solutions and Will Not Go Back
#####################################################################

:date: 2018-Mar-15 23:21 EDT
:tags: Python, development, open source
:category: Programming
:slug: staying-with-python
:author: Joseph C. Slater
:summary: Why open source computing is the future of engineering computing
:Status: published

Three years ago I wrote my first ever blog entry:
`Why Matlab Users Should be Moving to Python`_. It opened with:

    Back in 1989, when I first entered graduate school as an engineering
    student, I knew a handful of languages to some modest degree. For the sake
    of computations, I knew Basic and Fortran 77 (the horror!).

My knowledge of programming was elementary by the standards of the day, but I
did fancy myself as relatively capable. Of course, I made that judgement based on the company I kept, and Matlab_ was plenty powerful to perform the tasks we
needed (still is- even more so). Amongst engineers in my field I was close to the top in "getting stuff
done" computationally and still am. However, that came at the price of not developing the next level of high-power computing skills and I lived for 25 years in the golden cage of a single commercial software solution. If they didn't have it, I didn't know about it. It continues to grow and thrive, but there is far more growing and thriving that that singular environment.

As a result **I'm doubling down** on open source, with Python_ as my primary tool. Why?

- I'm an engineer. My time will always be focused on engineering and the time to create great C or Fortran that is parallelized for a particular problem won't happen unless it's necessary. It's a lot of work- a task in itself. If I need to, I'll do it, but it's not a great starting point because the time spent programming exceeds time spent executing code far too often. Code should be written as minimally as possible to get the job done. `The best code is no code at all`_. C and Fortran are not concise and require details that interpreted languages do not. There is a benefit to those details, but most of the time they bear little real fruit.
- `The best code is no code at all`_. `Code is our enemy`_. That means libraries, libraries, libraries, or in Python_ languages `packages <https://pypi.python.org/pypi>`_ (soon to be `here <https://pypi.org/>`_). Python had 135,356 projects at the moment I wrote this, and growing. The open source nature, amongst other benefits, has made Python the place to share your package. As a user, that means we get to leverage all of this instead of writing the code all over again. Matthew Rocklin's blog opens with an outstanding observation: `Programming often limits research more than fundamental domain challenges.`_. The Python_ ecosystem continues to grow and be put together to minimize how much coding users have to do themselves.
- Open source means people gladly help you do your work. When you make your project open source and post it, as I do on GitHub_, and then announce it, you might think "oh, I'm just going to embarrass myself." **False!** I will posit that humility is an effective way to grow. Setting that aside, what you will find is others who are interested in your work. They won't usually take over and do it for you, but sometimes they will as Raphael Timbó did with the `Vibration Toolbox for Python`_. [#]_ Short of that, they will provide fixes, highlight deficiencies, provide documentation, etc. Many will test your code for you, many will provide programing advice to improve your programing skills.

**Getting things done takes priority over writing great code.** Unfortunately,
this results in a lot of code, often poorly documented, with limited
reusability (especially by others). Further, this habit creates a culture of
isolation, where I and hundreds of others, perhaps thousands, have rewritten
the same code for nearly the same purpose, without thousands if not tens of
thousands of hours wasted and who knows how many incorrect results impacting
designs. The argument for using commercial code is usually something like: *
well, let experts write code for you. They validate it, and you can trust it as
the best that can be.* Well, that's simply wrong.

- First, consider the warrantee you agree to when you purchase and use commercial code. They don't take any responsibility for the code being fit for your purpose. **That's on you!**

- Second, major corporations validate commercial code then validate it more. Then, they revalidate it. They take the attitude *trust but verify*, which means they don't trust it, but find it more cost effective than writing their own code.

How do I know this? My job is to know and talk to people in industry regarding research, technology, and our graduates and their preparation. More o, they are writing their own code as the cost savings isn't as grea

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

.. [#] I have always been a bit stubborn in my opinion. I think I'd made some
       positive strides as I've grown older.

.. [#] Ironically, early on he observed clear reluctance on my part
       to convert to the Octave_ standards of
       Octave_'s help system compared to Matlab_. I think he missed the moment when I came to agree with him about that and other things! I'm sorry!

.. [#] In fact, he drove me crazy pushing the project forward so fast that I
       spent extra time working on formulating project objectives and
       priorities. In a few months we had a working release, and the project
       has had thousands of downloads since.


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
.. _`Why Matlab Users Should be Moving to Python`: http://josephcslater.github.io/moving-to-python.html
.. _`The best code is no code at all`: https://blog.codinghorror.com/the-best-code-is-no-code-at-all/
.. _GitHub: https://github.com/
.. _`Vibration Toolbox for Python`: https://github.com/vibrationtoolbox/vibration_toolbox
.. _`Code is our enemy`: http://www.skrenta.com/2007/05/code_is_our_enemy.html
.. _`Programming often limits research more than fundamental domain challenges.`: https://matthewrocklin.com/

Installing Python for Scientists and Engineers (and maybe Mathematicians too)
#####################################################################################
:date: 2017-01-13 11AM EDT
:tags: Python, Jupyter, Programming, Spyder, Mathematics, Engineering, Science
:category: Programming
:slug: installing-python
:author: Joseph C. Slater
:summary: Installing Python for Scientists and Engineers (and maybe Mathematicians too)
:Status: published


.. Installing Python for Scientists
.. ==========================================


The title of this article implies that you have similar interests to me: computational usage. I'm going to try to address 99% of the computational community so there are parts of this page you won't need. I apologize. However, I find it valuable to have a single destination to point people to when I have a question like "how do I start using Python?".


`Python`_ is quickly growing acceptance in the scientific and engineering community as a
computational language due to its open source nature, meaning it can be installed
anywhere for free, and its quickly expanding toolkit. With the scientific packages
being developed at a rapid pace it is quickly approaching parity with
established commercial tools such as `Matlab <mathworks.com>`_, or it's free
(and extremely well developed and supported) surrogate `Octave <octave.org>`_,
and even exceeding it in some domains. `My reasons
<{filename}/programming.rst>`_ for moving to `Python`_ have previously been
discussed in `My Journey to Python
<{filename}/programming.rst>`_ and continue to grow as I discover greater power in using it for my
primary language. My other `getting started
<{filename}/scipy-numpy-matplotlib-pylab.rst>`_ entry may also appeal to help
individuals  although the `Plotting with matplotlib
<http://nbviewer.jupyter.org/github/ipython/ipython/blob/1.x/examples/notebooks/Part%203%20-%20Plotting%20with%20Matplotlib.ipynb>`_
is likely the best way to start from zero knowledge.

The question I often hear, though, is how do I try it? How does someone install `Python`_? The answer is simple, once your needs are known. It's simple because many smart people have worked together to make it simple. Doing this as an individual would be prohibitively time consuming and fail to leverage tens of thousands of hours spent solving problems already. So: you don't want to do that. Not now at least.  Probably not in the future either. It's not something to do unless you have a lot of spare time.

What is everything, and why you don't want to manually install it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is no reason to read this subsection if you trust me and are raring to go. I'm the kind of person who would read this section, so that's why it's here. You might want to look at it later.

Just to give a flavor of why you wouldn't want to do this, note that the installation I recommend installs `445 <https://docs.continuum.io/anaconda/pkg-docs>`_ unique sub-packages and ensures that they all work properly, without operating system hangups, missing sub parts, failed compiles of executables, etcetera. These sub-packages include high performance optimally compiled libraries that you would need to install yourself after installing compilers and making sure you have all of the necessary dependencies. If this sounds like a lot of fun, you are reading the wrong page, and I can't even direct you to a right page.


Any platform (Mac/Windows/Linux)
------------------------------------

At this point in time, I believe that it is *very* clear that the hands-down winner for installing `Python`_ as a novice is the `Anaconda`_ distribution by `Continuum Analytics`_. Their website has plenty of information that you can peruse for getting an installation of everything you will need. The CEO, `Travis Oliphant <https://www.continuum.io/leadership>`_, is widely credited for molding `Python`_ into a computational language through his development of `Numpy`_, which became the basis for so much more. While arguments are sometimes made that using a `Continuum Analytics`_ is insufficiently "pure" for the open source community, I strongly disagree. [1]_

Other available distributions, that I don't personally have experience with, are

1. `Active State Python <http://www.activestate.com/activepython/downloads>`_
is a Commercial distribution with a "community edition". Active State is a solid supporter of the broader community by being a sponsor of the `Python Software Foundation <https://www.python.org/psf/sponsorship/sponsors/>`_.

2. `Enthought Canopy Python <https://www.enthought.com/products/epd/>`_.
Reviews for this version of Python seem not to be as good as those for the Anaconda version. Enthought was slow to move to Python 3, and it may still not be here (I say here, because we are here!). I don't see the point of a new user starting on a language being phased out (although it seems `old languages never die <https://jxself.org/cobol.shtml>`_).

3. `Python(x,y) <http://python-xy.github.io>`_
I'm not a fan of this as it is still not using Python 3. Due to inertia and some of the revolutionary improvements to Python 3, many with codebases have been slower to adopt Python 3 (now at 3.6!). For those doing scientific computing, the new features now clearly motivate one to start with Python 3. Overcoming legacy inertia can be a substantial challenge, though, so I don't judge anyone stuck on 2.7.


Windows
---------

One the neatest distributions fits wholly on a thumb drive. The `WinPython <https://winpython.github.io>`_ is completely portable an can *can be moved to any location (local, network, USB drive)*. This means you can take it with you, give it to a group of people pre-configured, distribute it over a network, etc. It can be completely "non-invasive", meaning you don't need to even uninstall it. It's not even on your hard drive. This is a great tool for anyone who has to work at different computers on a regular basis.

Mac
------

I personally have had luck using `MacPort <macports.org>`_, but just to get `Python`_ running, it's a bit much. Other package managers for free software exist, including `Fink <http://www.finkproject.org>`_, `Homebrew <http://brew.sh>`_. These all do more than you are likely interested in, and choosing one is far from a simple task (I've use each at one time or another, and they all seem to work fine.)

That said: If you want to install `Python`_ and run `Python`_ today, use the `Anaconda`_ distribution.

Linux
--------

There are really two types of Linux users:
  1. I want a cheap operating system, or one that will still run fast on old hardware
  2. I'm hard core. I would program in assembly language but I don't have enough time.


If you are type 1, install the `Anaconda`_. If you are type 2, God bless you, and good luck. You may have luck using the `linux package managers <http://www.tecmint.com/linux-package-managers/>`_ (specific to your distribution), but I will simply wish you well. You're not my target audience.


Government labs
-----------------

I've a bit of experience here, but not with `Python`_ explicitly, and not in any way that would make me worth kidnapping.

Working with anything in a SCIF can be daunting. If you work in one, you know that. If you don't, you only are reading this to get a bit of help convincing your tech people that you should be able to get this installed.

The big argument about open source software is that "anybody" can embed code in the software, risking the security of your systems.

Yup. That's true. However, it's also irrelevant. Here's why. Every single unix system contains open source software on it. Yes, that includes the Mac, which comes with an old underwhelming version of `Python`_. `Windows is gradually becoming more open source <http://www.forbes.com/sites/gordonkelly/2015/04/05/open-source-microsoft-windows/#66c7ed963628>`_ as well. Why? Because over time we've begun to realize that `closed source software is more vulnerable than open source software <http://www.forbes.com/sites/gordonkelly/2014/04/28/microsoft-races-to-fix-massive-internet-explorer-hack-no-fix-for-windows-xp-leaves-1-in-4-pcs-exposed/#1189788831a2>`_ because vulnerabilities are found faster, and there are more good guys looking than bad guys. The beauty in open source software is that you, the user, can look for vulnerabilities yourself. You may not be qualified, but surely your IT person is (unlikely, but they often act that way by espousing security mantras that have been refuted.).

*What about the risk of foreign nationals embedding code in the software?* Well, couldn't that be happening to Windows/MacOS/Linux right now? Do you think they don't have programmers oversees working on their operating systems? Call tech support and find out. Commercial packages that are core also have foreign nationals working on them, certainly many on H1B visas. This is also a red herring. The problem with security is it's never as easy as the security people try to tell you it is with platitudes of rules and more rules. Most real vulnerabilities are of the human type, `phishing <https://hbr.org/2016/09/the-biggest-cybersecurity-threats-are-inside-your-company>`_ for example. It's getting the door ajar that is the real threat.

So, I'm not an expert in Cyber security, but security people shouldn't make it easy for me to prove them wrong. However, this document won't convince them. So, instead, point out that there is a process already in place to get open source software in a secure environment: `get commercial support <http://www.activestate.com/government>`_. Further, you can have them contact other SCIFs and ask them how they are using open source. It's inconceivable that `Lawrence Livermore is writing open source software <https://wci.llnl.gov/simulation/computer-codes/ale3d>`_ and not using it where it needs to be used. What may actually convince some of them is that `open source software is actually safer than commercial software`_. This is illustrated by the `Coverity Scan report`_ which shows that *Open source software had a defect density of 0.61, compared to commercial software’s 0.76*. [2]_

That said, there are `valid reasons <http://softwareengineering.stackexchange.com/questions/206558/why-does-the-us-government-disallow-dynamic-languages-for-secure-projects>`_ not to use a dynamic language for code that must be secure. However, one has to ask: is this what's really going on? Are you using Python for analysis, or for delivering code? Those are two different issues that very well may lead to two different security responses.

To specifically address at least one instance: `Enthought Canopy`_ at the United States Air Force Research Lab is already approved and ready to be installed on almost any network including RDT&E, enclave networks, and AFNet, but don't trust me. Look it up yourself!





Questions?
------------

These tips only get better with your feedback, so please provide it below.



.. [1] The `Anaconda`_ distribution you install is completely open source. They constantly feed their software into the open source community, for free, and are unbelievably good citizens in the free software community. Keep in mind: the people doing this work need to eat. They've somehow managed to find a way to give away the product, even provide support for it, and get paid for yet a higher level of service. From my experience, they must flying in to your city, stopping by your MD's waiting room, and helping you code while you wait. I don't know what they do, but they do it, so I don't but this argument. A more eloquent argument is provided by `Jake VanderPlas <https://jakevdp.github.io>`_.

.. [2] `Tackling Open Source's Security Problem.`_

.. _Python: http://python.org
.. _Numpy: http://numpy.org
.. _Jupyter: http://jupyter.org
.. _Linux:  http://linux.org
.. _Atom: http://atom.io
.. _Spyder: https://pypi.python.org/pypi/spyder
.. _Anaconda: https://www.continuum.io/downloads
.. _Windows: https://www.microsoft.com/en-us/windows
.. _MacOS X: http://www.apple.com/macos/
.. _Continuum Analytics: https://www.continuum.io
.. _Enthought Canopy: https://www.enthought.com/products/canopy/
.. _open source software is actually safer than commercial software: https://sector.ca/tackling-open-sources-security-problem/
.. _Coverity Scan report: https://na-sjf.marketo.com/rs/157-LQW-289/images/2014-Coverity-Scan-Report.pdf
.. _`Tackling Open Source's Security Problem.`: https://sector.ca/tackling-open-sources-security-problem/

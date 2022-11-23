Installing the AIAA LaTeX Package 
####################################

:date: 2015-Nov-12 11:00 EDT
:tags: LaTeX, AIAA
:category: LaTeX
:slug: installing_AIAA_LaTeX_package
:author: Joseph C. Slater
:summary: Installing the AIAA LaTeX Package 
:Status: published

Every once in a while, I am asked how to install this package. I'm not
the author... the package lists the authors. However, they've done a
wonderful job, and enough work, so I'm going to pick up a bit of slack
on their behalf with what amounts to 10 minutes of effort, and a few
corrections as you send them to me.

On all platforms
----------------

I presume you've already downloaded the package and unzipped it. 

The first thing you need to do is *process*  ``aiaa.ins`` by getting to the command line on your machine and typing

.. code-block:: bash

   latex aiaa.ins

or by loading the ``aiaa.ins`` file into your favorite LaTeX editor
and compile with the ``LaTeX`` button or menu item (there are a ton of
options depending on your particular installation. ).  Either will
work, so if you don't know where your command line prompt is, you
don't have to use it. 

Installation on a Mac
-----------------------
	 
Then, make sure the pieces and parts are in the right places. 

On a Mac, the ``aiaa.bst`` file has to be put in

.. code-block:: bash

   ~/Library/texmf/bibtex/bst

The ``~/`` means your home directory. To get there, if you don't know
how to use ``Terminal``:

- Go to the ``Finder``
- Select ``Go to Folder`` from the ``Go`` menu.
- Enter ``~/Library``

  
You can now navigate to the folder you need to get to. If it does not
exist, you will need to create all of these folders in this nest so
that your ``aiaa.bst`` file resides inside the ``bst`` folder nested
as shown above. 

The remaining entire folder (currently ``aiaa-3.6.1`` as of this
writing) that is created by unzipping ``aiaa.zip`` (or what ever
archive is the package) must be put into
``~/Library/texmf/tex/latex``.

You might want to make a *Shortcut Link*  by holding the ``command``
and ``option`` keys and dragging the ``aiaa-3.6.1`` folder to the
desktop. If you see an arched arrow before you unclick, you will have
a Shortcut link. If not, don't let go. You are moving it and that's
making things worse. 

On MikTeX (most common on Windows)
------------------------------------

See *On All Platforms* above and perform those steps. 

- `Create a local texmf tree`_ in MiKTeX per the MiKTeX website. I   don't think I can write this up any better. 
- Make the new package known to MiKTeX: refresh the MiKTeX filename database. To do this, click "Start/ Programs/ MiKTeX
  2.x/Maintenance/ Settings" (or similar) to get to the MiKTeX
  options, click the button "Refresh FNDB". The installation is complete.
   

Linux
--------

If you have Linux, and have installed LaTeX, I am going to presume you
are sufficiently capable of figuring this out via an internet
search. Sorry. That's how I would have to figure it out!


To test (all platforms)
--------------------------
Make a copy  of the ``aiaa-3.6.1`` folder in your ``Documents``
folder. Remove the files with extensions ``.cls`` and ``.bst``.  Load
the file ``aiaa.tex`` into your favorite LaTeX compiler. Try to
compile it using LaTeX. If it works, great. If not, you will get a
warning that LaTeX couldn't find something. Please read the logs and
follow the instructions again. 

.. _`Create a local texmf tree` : http://docs.miktex.org/manual/localadditions.html

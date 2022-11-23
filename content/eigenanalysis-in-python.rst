Performing eigenvalue analysis/reconstruction in Python
#######################################################
:date: 2016-02-1 12:28 EDT
:tags: Linear Algebra, Eigenanalysis, Eigenvalues, Eigenvectors, Programming
:category: Programming
:slug: eigenanalysis-in-python
:author: Joseph C. Slater
:summary: Using SciPy to perform eigenanalysis (help for Matlab users)
:Status: published



If you are new to Python, this jumps in a bit quickly. I'd suggest
looking at `Numpy for Matlab
Users <http://scipy.github.io/old-wiki/pages/NumPy_for_Matlab_Users.html>`__
before reading this. The following is simply a brief demonstration of
using Python 3.5 (or greater) for eigenanalysis. The original notebook is
available at `my github examples repository <https://github.com/josephcslater/iPythonExamples>`__. A few things to note:

1. If you use
   an earlier version of Python (than 3.5), the ``@`` operator isn't
   defined "yet". To perform matrix multiplication, you need to type use
   ``numpy.dot(A,B)`` in place of ``A@B``. That will require you to
   start with ``import numpy`` before doing any of this.

2. I demonstrate for a
   non-symmetric matrix. For a symmetric matrix, you should use
   ``eigh``. The *h* in ``eigh`` means *Hermetian*, and is a more
   general definition than symmetric. If you don't deal with complex
   valued matrices, it's irrelevant to you. Using ``eigh`` leverages
   the properties of Hermetian matrices in the solution process
   resulting in potentially faster *and* more accurate results than
   the more general ``eig`` code. For a small matrix, this is
   irrelevant, but it becomes important for more substantial calculations.

3. I
   show a couple of tips later that matter for larger matrices (avoiding the
   inverse). Be aware of them. Why may or may not matter to you, but when
   you get to big or sensitive problems, they do.

The first thing I need to do is import a couple of tools (Scipy, and its
linear algebra package).

.. code:: python

    import scipy as sp
    import scipy.linalg as la


We are going to attempt to solve for

.. math:: A r = r v

where :math:`A` is the matrix, and :math:`r` represents the right eigenvectors,
while :math:`v` represents the eigenvalues. We are also going to obtain
the left eigenvalues as well for later use.

.. code:: python

    A = sp.array([[1,2,3],[4,5,6],[7,8,9]])  # Defining the array (I'm avoiding using the matrix class)
    # It's a personal preference, and I'm still not locked into it myself.
    (v, l, r) = la.eig(A, left = True) # You can read the help, buy the left eigenvectors don't get created without this.
    v = sp.diag(v)  # by default, eig puts the eigenvalues in a 1-D array. We will need a diagonal matrix in a moment.
    print(l)
    print(v)
    print(r)


.. parsed-literal::

    [[-0.46454727 -0.88290596  0.40824829]
     [-0.57079553 -0.23952042 -0.81649658]
     [-0.67704379  0.40386512  0.40824829]]
    [[  1.61168440e+01+0.j   0.00000000e+00+0.j   0.00000000e+00+0.j]
     [  0.00000000e+00+0.j  -1.11684397e+00+0.j   0.00000000e+00+0.j]
     [  0.00000000e+00+0.j   0.00000000e+00+0.j  -9.75918483e-16+0.j]]
    [[-0.23197069 -0.78583024  0.40824829]
     [-0.52532209 -0.08675134 -0.81649658]
     [-0.8186735   0.61232756  0.40824829]]


These should be identical based on the eigen-equation. They are to the
default precision.

.. code:: python

    print(v)
    print(la.inv(r)@A@r)


.. parsed-literal::

    [[  1.61168440e+01+0.j   0.00000000e+00+0.j   0.00000000e+00+0.j]
     [  0.00000000e+00+0.j  -1.11684397e+00+0.j   0.00000000e+00+0.j]
     [  0.00000000e+00+0.j   0.00000000e+00+0.j  -9.75918483e-16+0.j]]
    [[  1.61168440e+01   3.55271368e-15   1.77635684e-15]
     [ -2.49800181e-15  -1.11684397e+00  -2.77555756e-17]
     [  2.79947848e-15   4.62304004e-16   9.86076132e-32]]


In reality, one should never ever use the inverse function unless the
actual answer you want is the inverse itself (which I've never seen for
a real problem). What you typically want is the inverse of a matrix
times another matrix or vector- which is the solution to a linear
algebra problem. We can use the ``solve`` function to obtain this. This
is arguably no better, but it is illustrative. For a larger problem, the
benefit is easier to demonstrate.

.. code:: python

    la.solve(r,A)@r




.. parsed-literal::

    array([[  1.61168440e+01,   3.05037570e-15,  -4.48960353e-17],
           [ -2.74605686e-15,  -1.11684397e+00,   3.95339943e-16],
           [  3.86524889e-15,  -7.16944125e-16,  -3.70074342e-17]])



This is "rebuilding" the original matrix from the eigensolution. Looks
pretty good.

.. code:: python

    r@v@la.inv(r)




.. parsed-literal::

    array([[ 1.+0.j,  2.+0.j,  3.+0.j],
           [ 4.+0.j,  5.+0.j,  6.+0.j],
           [ 7.+0.j,  8.+0.j,  9.+0.j]])



Avoiding the inverse is a bit uncomfortable in this case, but a bit of
doodling yields that

.. math:: A B^{-1}  = \left(\left(A B^{-1}\right)^T\right)^T = \left(\left(B^{-1}\right)^T A^T  \right)^T

Noting that

.. math:: \left(B^{-1}\right)^T  = \left(B^{T}\right)^{-1}

we can use

.. code:: python

    r@la.solve(r.T,v.T).T




.. parsed-literal::

    array([[ 1.+0.j,  2.+0.j,  3.+0.j],
           [ 4.+0.j,  5.+0.j,  6.+0.j],
           [ 7.+0.j,  8.+0.j,  9.+0.j]])



For the left eigenvectors, they are actually simply the right
eigenvectors of the transpose of the matrix, so

.. math:: A^T l = l  v

Below I lazily obtain the eigenvalues using the left eigenvectors, with
an inverse.

.. code:: python

    la.inv(l)@A.T@l




.. parsed-literal::

    array([[  1.61168440e+01,   1.77635684e-15,   8.88178420e-16],
           [  1.94289029e-15,  -1.11684397e+00,  -4.99600361e-16],
           [  1.66684734e-15,   1.64791705e-16,   9.06493304e-17]])

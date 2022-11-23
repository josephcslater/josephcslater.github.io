



Using Laplace Transforms to Solve a Linear Differential Equation in SymPy
=========================================================================

:date: 2017-05-06 11:21 EDT
:tags: SymPy, Laplace, Differential Equations, Python
:category: Programming
:slug: solve-ode
:author: Joseph C. Slater
:summary: Using Python to solve differential equations
:Status: published


Consider solving

.. math:: 3\ddot{x}+30\dot{x}+63x=4\dot{g}(t)+6g(t)

in Jupyter where

.. math:: g(t)=u_s(t)

is the unit step function (Heaviside Function) and :math:`x(0) = 4` and
:math:`\dot{x}(0)=7`.

.. code:: python

   %matplotlib inline
    from sympy.integrals.transforms import laplace_transform
    from sympy.integrals.transforms import inverse_laplace_transform
    from sympy import *
    import sympy as sympy
    from sympy.abc import a, t, x, s, X, g, G
    init_printing(use_unicode=True)

.. code:: python

    x, g, X = symbols('x g X', cls = Function)

.. code:: python

   x0 = 4
    v0 = 7

.. code:: python

    g = Heaviside(t) #This is just the step function

.. code:: python

    laplace_transform(Heaviside(t), t, s) # Checking the performance of the Laplace Transform Module




.. parsed-literal::

    (1/s, 0, True)



.. code:: python

    laplace_transform(DiracDelta(t), t, s) # Checking the performance... this is wrong. Should get 1.




.. parsed-literal::

    (1/2, -oo, True)



.. code:: python

    laplace_transform(DiracDelta(t - 2), t, s) # right result




.. parsed-literal::

    (exp(-2*s), -oo, True)



.. code:: python

    laplace_transform(DiracDelta(t - a), t, s)[0] # right result (theta(t) is a Heaviside function representation in SymPy)




.. math::

    \left(- \theta\left(a e^{i \pi}\right) + 1\right) e^{- a s}



.. code:: python

    laplace_transform(DiracDelta(t - a), t, s)[0].subs(a,2) # Looks good




.. math::

    e^{- 2 s}



.. code:: python

    laplace_transform(DiracDelta(t - a), t, s)[0].subs(a,1) # Looks good




.. math::

    e^{- s}



.. code:: python

    laplace_transform(DiracDelta(t - a), t, s)[0].subs(a,0.0000001) # Looks to converge




.. math::

    e^{- 1.0 \cdot 10^{-7} s}



.. code:: python

    laplace_transform(DiracDelta(t - a), t, s)[0].subs(a,-0.0000001) #So... here is the illustration.




.. math::

    0



What's happening here is that SymPy currently takes the position that
half the Dirac delta happens before zero, half after, so the result should
only be half as big. I think I'm in a rather large crowd in saying that
this isn't proper. It makes some theoretical sense, and is a wonderful
math debate. However, given convention says that :math:`\delta(t)` is
fully captured by a Laplace transform with a result of :math:`1`
(Mathematica, Maple, Matlab, every System Dynamics, Controls, and Signal
Processing book I've ever read), SymPy is practically wrong. I'm hoping
that they will change their minds. I am now a bit skeptical about using
SymPy for my math work as the results of a simple conventional
application don't match expected behavior consistent with other codes.[1]_

So we note that SymPy isn't taking the Laplace Transform properly here,
so we need to avoid using this result. (we should have gotten 1) Valid
as of 0.7.6.1

.. code:: python

    print(sympy.__version__)


.. parsed-literal::

    0.7.6.1


The first line below would work if SymPy performed the Laplace Transform
of the Dirac Delta correctly. Short of that, we manually insert the
Laplace Transform of :math:`g(t)` and :math:`\dot{g}(t)` where
:math:`g(t)=u(t)`.

.. code:: python

   #eom  = Eq(3*(s**2 * X(s)-s*x0-v0)+30 * (s*X(s)-x0)+ 63 * X(s), laplace_transform( 4 * diff(g,t) + 6 * g, t, s, noconds = True))

    eom  = Eq(3*(s**2 * X(s)-s*x0-v0)+30 * (s*X(s)-x0)+ 63 * X(s), 4 * 1 + 6 * 1/s)
    eom




.. math::

    3 s^{2} X{\left (s \right )} + 30 s X{\left (s \right )} - 12 s + 63 X{\left (s \right )} - 141 = 4 + \frac{6}{s}



.. code:: python

    Xofs = solve(eom,X(s))
    Xofs[0]




.. math::

    \frac{12 s^{2} + 145 s + 6}{3 s \left(s^{2} + 10 s + 21\right)}



.. code:: python

    soln = inverse_laplace_transform(Xofs[0],s,t)
    soln




.. math::

    \frac{\theta\left(t\right)}{84} \left(8 e^{7 t} + 749 e^{4 t} - 421\right) e^{- 7 t}



.. code:: python

    soln_simp = expand(soln)
    soln_simp




.. math::

    \frac{2 \theta\left(t\right)}{21} + \frac{107 \theta\left(t\right)}{12} e^{- 3 t} - \frac{421 \theta\left(t\right)}{84} e^{- 7 t}



.. code:: python

    N(soln_simp,5)




.. math::

    0.095238 \theta\left(t\right) + 8.9167 e^{- 3 t} \theta\left(t\right) - 5.0119 e^{- 7 t} \theta\left(t\right)



Note that :math:`\theta(t)` is SymPy's notation for a step function.
This simply means the answer can't be used before :math:`t=0`.

.. [1] This has been fixed in later revisions.

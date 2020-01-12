
Solving multiple linear ordinary differential equations in SymPy
================================================================
:date: 2016-02-29 4:37 EDT
:tags: SymPy, Differential Equations, Python, Jupyter 
:category: Programming
:slug: differential_equation_solution_sympy
:author: Joseph C. Slater
:summary: Solving multiple linear ordinary differential equations in SymPy
:Status: published


I am using `Python 3.5 <www.python.org>`__ in `Jupyter
<www.jupyter.org>`__ (formerly iPython). The original notebook is
available at `my github examples repository <https://github.com/josephcslater/iPythonExamples>`__.
	 
Presume we wish to solve the coupled linear ordinary differential
equations given by

.. raw:: latex

   \begin{align}
   3\dot{x} &= y\\
   \dot{y}&=-3y-15x+4u(t)
   \end{align}

where :math:`u(t)` is the step function and :math:`x(0)=5` and
:math:`y(0) = 10`.

.. code:: python

    %matplotlib inline
    
    # import symbolic capability to Python- namespace is a better idea in a more general code. 
    from sympy import *
    
    # print things all pretty
    from sympy.abc import *
    init_printing()

Need to define variables as symbolic for sympy to use them.

.. code:: python

    t, C1, C2= symbols("t C1 C2")
    x, y =  symbols("x y", cls = Function, Function = True)

First we must define the governing equations as equalities or
expressions. We have the option, I will do one each way for the sake of
illustration, as opposed to simplicity.

.. code:: python

    eq1 = Eq(3 * diff(x(t), t), y(t))
    eq1




.. math::

    3 \frac{d}{d t} x{\left (t \right )} = y{\left (t \right )}



I'd like to use the Heaviside function. It doesn't work, but I'm showing
how I tried anyway.

.. code:: python

    import sympy.functions.special.delta_functions as sfuncs

.. code:: python

    eq2 = Eq(diff(y(t),t), - 3 * y(t) - 15 * x(t) + 4 * sfuncs.Heaviside(t))
    # Note: Heaviside doesn't work for me in the solver, so I've left it here as "proper" but dokn't use it. 
    eq2 = Eq(diff(y(t),t), - 3 * y(t) - 15 * x(t) + 4 * 1)
    eq2




.. math::

    \frac{d}{d t} y{\left (t \right )} = - 15 x{\left (t \right )} - 3 y{\left (t \right )} + 4



Solving the differential equations. The ``ics =``... should apply the
initial conditions. Doesn't work. Perhaps some day.

.. code:: python

    soln = dsolve((eq1, eq2), ics = {x: 5, y: 0})
    soln




.. math::

    \left [ x{\left (t \right )} = \frac{1}{3} \left(C_{1} \sin{\left (\frac{\sqrt{11} t}{2} \right )} + C_{2} \cos{\left (\frac{\sqrt{11} t}{2} \right )}\right) e^{- \frac{3 t}{2}} + \frac{4}{15}, \quad y{\left (t \right )} = \left(\left(- \frac{3 C_{1}}{2} - \frac{\sqrt{11} C_{2}}{2}\right) \sin{\left (\frac{\sqrt{11} t}{2} \right )} + \left(\frac{\sqrt{11} C_{1}}{2} - \frac{3 C_{2}}{2}\right) \cos{\left (\frac{\sqrt{11} t}{2} \right )}\right) e^{- \frac{3 t}{2}}\right ]



Solving for the constants. I'm substituting ``t = 0``, then the initial
values for ``x`` and ``y``. You'll note that the first equation doesn't
need ``y(0)`` substituted, while the second doesn't need ``x(0)``
substituted. I found this out after and did that for brevity.

.. code:: python

    constants = solve((soln[0].subs(t,0).subs(x(0),5), soln[1].subs(t,0).subs(y(0),10)),{C1,C2})
    constants




.. math::

    \left \{ C_{1} : \frac{313 \sqrt{11}}{55}, \quad C_{2} : \frac{71}{5}\right \}



Let's put in our constants and see what we get. I'm using ``.rhs`` to
pull out the right side of the solution. You can look at ``soln[0]`` to
see what I mean, or try ``help(soln[0])`` and read the results.

.. code:: python

    xsoln = expand(soln[0].rhs.subs(constants))
    xsoln




.. math::

    \frac{4}{15} + \frac{313 \sqrt{11}}{165} e^{- \frac{3 t}{2}} \sin{\left (\frac{\sqrt{11} t}{2} \right )} + \frac{71}{15} e^{- \frac{3 t}{2}} \cos{\left (\frac{\sqrt{11} t}{2} \right )}



.. code:: python

    ysoln = soln[1].rhs.subs(constants)
    ysoln




.. math::

    \left(- \frac{172 \sqrt{11}}{11} \sin{\left (\frac{\sqrt{11} t}{2} \right )} + 10 \cos{\left (\frac{\sqrt{11} t}{2} \right )}\right) e^{- \frac{3 t}{2}}



.. code:: python

    eq1.subs(x(t),xsoln).subs(y(t),ysoln)




.. math::

    3 \frac{d}{d t}\left(\frac{4}{15} + \frac{313 \sqrt{11}}{165} e^{- \frac{3 t}{2}} \sin{\left (\frac{\sqrt{11} t}{2} \right )} + \frac{71}{15} e^{- \frac{3 t}{2}} \cos{\left (\frac{\sqrt{11} t}{2} \right )}\right) = \left(- \frac{172 \sqrt{11}}{11} \sin{\left (\frac{\sqrt{11} t}{2} \right )} + 10 \cos{\left (\frac{\sqrt{11} t}{2} \right )}\right) e^{- \frac{3 t}{2}}



Is equation 1 true with this solution set?

.. code:: python

    Eq(simplify(3*diff(xsoln,t)),simplify(ysoln))




.. math::

    \mathrm{True}



Is equation 2 true with this solution set?

.. code:: python

    Eq(simplify(diff(ysoln,t)),simplify(4-3*ysoln-15*xsoln))




.. math::

    \mathrm{True}



So that's it. Out answers are indeed given by

.. code:: python

    Eq(x(t),xsoln)




.. math::

    x{\left (t \right )} = \frac{4}{15} + \frac{313 \sqrt{11}}{165} e^{- \frac{3 t}{2}} \sin{\left (\frac{\sqrt{11} t}{2} \right )} + \frac{71}{15} e^{- \frac{3 t}{2}} \cos{\left (\frac{\sqrt{11} t}{2} \right )}



and

.. code:: python

    Eq(y(t),ysoln)




.. math::

    y{\left (t \right )} = \left(- \frac{172 \sqrt{11}}{11} \sin{\left (\frac{\sqrt{11} t}{2} \right )} + 10 \cos{\left (\frac{\sqrt{11} t}{2} \right )}\right) e^{- \frac{3 t}{2}}




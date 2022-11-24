Using SymPy and Jupyter to reduce 5 linear equations to a single equation in two variables.
##############################################################################################

:date: 2016-02-15 13:00 EDT
:tags: Python, Jupyter, SymPy
:category: Programming
:slug: sympy-solve-equation-set
:author: Joseph C. Slater
:summary: Using SymPy in Jupyter to reduce a set of linear equations
:Status: published

Solving a variant of problem 6.3, Gray, Costanzo, and Plesha (Gray,
G.L., Costanzo, F., and Plesha, M.E., *Engineering Mechanics: Dynamics*,
McGraw Hill, New York, 2010.), where kinetics are added (:math:`I_1`,
:math:`I_2`, :math:`I_3`).

For my students: This is Wright State University, ME 3210, Quiz 2, Spring 2016



The problem statement is: A Moment :math:`M` is applied to the rightmost gear
(gear 3). Find the acceleration of the gear as a resulting moment
presuming inertias :math:`I_1`, :math:`I_2`, :math:`I_3`.	 

Figure awaiting copyright approval. Dummy graphic in place for the
moment.

.. Gears.png

.. figure:: images/image.pdf
   :width: 50%
   :align: center
   :alt: Gears

   Figure 1: Gear figure from Gray, Costanzo, and Plesha.

I am using `Python 3.5 <www.python.org>`__ in `Jupyter
<www.jupyter.org>`__ (formerly iPython). The original notebook is
available at `my Github examples repository <https://github.com/josephcslater/iPythonExamples>`__.

.. code-block:: python
   :linenos:

    # import symbolic capability to Python
    from sympy import *
    # print things all pretty
    from sympy.abc import *
    init_printing()
    # Need to define variables as symbolic for sympy to use them. 
    r_A, r_B, r_C, r_D, F_AB, F_DC, M= symbols("r_A r_B r_C r_D F_AB F_DC M", real = True)
    I_1, I_2, I_3 = symbols("I_1 I_2 I_3", real = True)
    theta_1, theta_2, theta_3 = symbols("theta_1 theta_2 theta_3", real = True)

Defining equations. In SymPy, and equation is an expression that is
equal to zero. All terms must be brought to the same side in defining
it.

.. code-block:: python
   :linenos:

    EA = F_DC *r_D  - I_3 * diff(theta_3(t),t,t)
    EA

.. math::

    F_{DC} r_{D} - I_{3} \frac{d^{2}}{d t^{2}}  \theta_{3}{\left (t \right )}


.. code-block:: python
   :linenos:
      
    EB = r_B* F_AB - r_C* F_DC - I_2 * diff(theta_2(t),t,t)
    EB

.. math::

    F_{AB} r_{B} - F_{DC} r_{C} - I_{2} \frac{d^{2}}{d t^{2}}  \theta_{2}{\left (t \right )}



.. code-block:: python
   :linenos:

    EC = r_A *(-F_AB) + M - I_1 * diff(theta_1(t),t,t)
    EC




.. math::

    - F_{AB} r_{A} - I_{1} \frac{d^{2}}{d t^{2}}  \theta_{1}{\left (t \right )} + M



.. code-block:: python
   :linenos:

    E1 = diff(theta_3(t),t,t)* r_D - diff(theta_2(t),t,t) *r_C
    E1




.. math::

    - r_{C} \frac{d^{2}}{d t^{2}}  \theta_{2}{\left (t \right )} + r_{D} \frac{d^{2}}{d t^{2}}  \theta_{3}{\left (t \right )}



.. code-block:: python
   :linenos:

    E2 = r_B * diff(theta_2(t),t,t) - diff(theta_1(t),t,t) *r_A
    E2




.. math::

    - r_{A} \frac{d^{2}}{d t^{2}}  \theta_{1}{\left (t \right )} + r_{B} \frac{d^{2}}{d t^{2}}  \theta_{2}{\left (t \right )}



.. code-block:: python
   :linenos: 

    solve(EA,diff(theta_3(t),t,t))




.. math::

    \left [ \frac{F_{DC} r_{D}}{I_{3}}\right ]



.. code-block:: python
   :linenos:

    solve(EB,F_AB)[0]




.. math::

    \frac{1}{r_{B}} \left(F_{DC} r_{C} + I_{2} \frac{d^{2}}{d t^{2}}  \theta_{2}{\left (t \right )}\right)



I'm going to do substitutions in stages, eliminating one variable at a
time for clarity.

.. code-block:: python
   :linenos:

    step1 = EC.subs(F_AB, solve(EB,F_AB)[0])
    step1




.. math::

    - I_{1} \frac{d^{2}}{d t^{2}}  \theta_{1}{\left (t \right )} + M - \frac{r_{A}}{r_{B}} \left(F_{DC} r_{C} + I_{2} \frac{d^{2}}{d t^{2}}  \theta_{2}{\left (t \right )}\right)



.. code-block:: python
   :linenos:

    step2 = step1.subs(F_DC,solve(EA,F_DC)[0])
    step2




.. math::

    - I_{1} \frac{d^{2}}{d t^{2}}  \theta_{1}{\left (t \right )} + M - \frac{r_{A}}{r_{B}} \left(I_{2} \frac{d^{2}}{d t^{2}}  \theta_{2}{\left (t \right )} + \frac{I_{3} r_{C}}{r_{D}} \frac{d^{2}}{d t^{2}}  \theta_{3}{\left (t \right )}\right)



.. code-block:: python
   :linenos:

    step3 = step2.subs(diff(theta_1(t),t,t),solve(E2,diff(theta_1(t),t,t))[0])
    step3




.. math::

    - \frac{I_{1} r_{B}}{r_{A}} \frac{d^{2}}{d t^{2}}  \theta_{2}{\left (t \right )} + M - \frac{r_{A}}{r_{B}} \left(I_{2} \frac{d^{2}}{d t^{2}}  \theta_{2}{\left (t \right )} + \frac{I_{3} r_{C}}{r_{D}} \frac{d^{2}}{d t^{2}}  \theta_{3}{\left (t \right )}\right)



.. code-block:: python
   :linenos:

    step4 = step3.subs(diff(theta_2(t),t,t),solve(E1,diff(theta_2(t),t,t))[0])
    step4




.. math::

    - \frac{I_{1} r_{B} r_{D}}{r_{A} r_{C}} \frac{d^{2}}{d t^{2}}  \theta_{3}{\left (t \right )} + M - \frac{r_{A}}{r_{B}} \left(\frac{I_{2} r_{D}}{r_{C}} \frac{d^{2}}{d t^{2}}  \theta_{3}{\left (t \right )} + \frac{I_{3} r_{C}}{r_{D}} \frac{d^{2}}{d t^{2}}  \theta_{3}{\left (t \right )}\right)



Finally, the acceleration of the right most gear as a function of the
input moment

.. code-block:: python
   :linenos:

    solve(step4,diff(theta_3(t),t,t))




.. math::

    \left [ \frac{M r_{A} r_{B} r_{C} r_{D}}{I_{1} r_{B}^{2} r_{D}^{2} + I_{2} r_{A}^{2} r_{D}^{2} + I_{3} r_{A}^{2} r_{C}^{2}}\right ]




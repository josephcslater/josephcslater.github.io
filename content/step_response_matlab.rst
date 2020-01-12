
Step response of a first order system with derivative input contribution Matlab
=================================================================================
:date: 2016-02-18 4:37 EDT
:tags: Transfer Functions, Step Response, Matlab
:category: Programming
:slug: step-response-matlab
:author: Joseph C. Slater
:summary: Step response of a first order system with derivative input contribution Matlab
:Status: published

The response of a system to a sudden excitation is often modeled as a step response. The following is an example of how to obtain the step response of a simple system. It illustrated the difference between a system with and without so-called *numerator dynamics*. Such dynamics represent an interaction due to velocity induced forces, such as those in viscous fluid dynamics or caused by a dashpot (also fluid-driven).



Consider the transfer function of a system given by

.. math::


   4\dot{x}+x=g(t)+\dot{g}(t)

is

.. math::


   T(s)=\frac{s+1}{4s+1}


while for a second system given by

.. math::


   4\dot{x}+x=g(t)

is

.. math::


   T(s)=\frac{1}{4s+1}

Find the response to an input of :math:`5u(t)`.

Given that the amplitude of the step input is 5, it's easiest to simply
multiply the transfer function by five and use a unit step function,
allowing us to use the Matlab ``step`` function.

.. code:: python

    sys1=tf([1 1]*5,[4 1])
    sys2 = tf([1]*5,[4 1])
    step(sys1);
    hold on;
    step(sys2)



.. image:: images/output_2_0.png
   :alt: Gear figure

.. parsed-literal::

    sys1 =

      5 s + 5
      -------
      4 s + 1

    Continuous-time transfer function.


    sys2 =

         5
      -------
      4 s + 1

    Continuous-time transfer function.


Alternatively, using ``lsim``.

.. code:: python

    sys1=tf([1 1]*5,[4 1])
    sys2 = tf([1]*5,[4 1])
    t=0:.01:40;
    u=t*0+1;
    lsim(sys1,u, t);
    hold on;
    lsim(sys2,u,t)




.. image:: images/output_4_0.png
   :alt: My hand drawn free body diagrams and equations.

.. parsed-literal::

    sys1 =

      5 s + 5
      -------
      4 s + 1

    Continuous-time transfer function.


    sys2 =

         5
      -------
      4 s + 1

    Continuous-time transfer function.


In both cases, the blue line represents the *sys1* response, and the
orange line the *sys2* response. This can be demonstrated by plotting
them individually.

The effect of the :math:`\dot{g}(t)` term is to effectively jump start
the response at a higher level, equivalent to 5/4, which are two numbers
you should see in the *sys1* transfer function.

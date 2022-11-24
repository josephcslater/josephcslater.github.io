
``kwargs``, ``args``, ``**kwargs``, and ``*args``
=================================================

:date: 2017-12-03 07:28 EDT
:tags: Python, Programming
:category: Research
:slug: python-args-and-kwargs
:author: Joseph C. Slater
:summary: Using args and kwargs in Python
:Status: published


In my observation, nothing in Python is more confusing than ``kwargs``
and ``args`` and how to use them. There are explanations on the web, but
none ever seem comprehensive enough for me. So, here is my attempt. Like
anything else, they are a feature that seem to have no point until you
are stuck needing them. Then they become invaluable.

(This
`notebook <https://raw.githubusercontent.com/josephcslater/iPythonExamples/master/args_n_kwargs.ipynb>`__
can be downloaded and run within the `Jupyter notebook <jupyter.org/>`__
environment by selecting `the
link <https://raw.githubusercontent.com/josephcslater/iPythonExamples/master/args_n_kwargs.ipynb>`__
and using ``Save Page As`` in your web browser.)

They don’t exist
----------------

What? How can they not exist? Well, the Python only reserves a `limited
number of
keywords <https://docs.python.org/3.6/reference/lexical_analysis.html#keywords>`__.
33 to be exact. ``args`` and ``kwargs`` aren’t on the list. ``kwargs``
and ``args`` are variable names you choose.

If they don’t exist, why do I see them all over the place?
----------------------------------------------------------

They have become conventional variable names for *packed arguments* and
*packed keyword arguments*. You could use any other name you’d like that
is allowable in Python. These are just conventions.

What is packing?
----------------

Packing is collecting a group of values into a single variable name.
``*`` collects values into a
`tuple <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuples>`__
while ``**`` collects named values into a
`dictionary <https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries>`__.
The distinction is somewhat irrelevant for the purpose here, outside of
the apparent bundling of name and value in the dictionary.

``*`` and ``**`` are actually used outside of ``args`` and ``kwargs``.
For instance, some functions return multiple values. They can be packed
by calling them with a single variable, e.g. ``a = f(x)`` in place of
``a, b, c = f(x)``. Alternatively, if you only need the first value, you
can instead call the function with ``a, *_ = f(x)``, which packs the
rest of the returned values into ``_``, which represents nowhere.

How does ``*args`` work in a function?
--------------------------------------

Consider a function into which we want to send a variable number of
arguments.

.. code:: ipython3

    def f(*args):
        print(args)

.. code:: ipython3

    f('This', 'is', 'how', 'the', 'print', 'command', 'works.')


.. parsed-literal::

    ('This', 'is', 'how', 'the', 'print', 'command', 'works.')


Of course, this isn’t quite right. What this shows is that all of the
arguments have been assembled into a tuple. They now are part of a list,
and print as such. This isn’t likely what we meant to do. What we want
to do now is *unpack* the tuple so that the print command perceives the
tuple as a group of individual arguments.

.. code:: ipython3

    def g(*args):    # packed into the tuple
        print(*args) # unpacked into individual arguments

.. code:: ipython3

    g('This', 'is', 'how', 'the', 'print', 'command', 'works.')


.. parsed-literal::

    This is how the print command works.


Now, the Python ``print`` command is much more sophisticated, but this
starts to show the power of packing arguments this way.

What is an example where this could be helpful?
-----------------------------------------------

Say I want to write a function that returns the product of a number to
the 3rd power, such as

.. math:: a b^3

However, I already have a more general function that returns

.. math:: a b^c

.. code:: ipython3

    def power(a, b, c):
        return a*b**c

.. code:: ipython3

    power(5, 2, 3)




.. parsed-literal::

    40



What I can do is create a function that calls ``power``, but packs and
unpacks the arguments appropriately. We know that the last argument must
be the number 3. We could simply explicitly write the other arguments:

.. code:: ipython3

    def power3(a, b):
        return power(a, b, 3)

However, that’s not as lazy as we would like to be. We could have
instead written:

.. code:: ipython3

    def power3(*args):
        return power(*args, 3)

.. code:: ipython3

    power3(5, 2)

.. parsed-literal::

    40

Why would this be helpful? Well, there are numerous reasons. One might
be error checking. It may be that ``power`` is from a module that is
very powerful so you want to use that. However, your code may call it
with arguments that are inappropriate for that library. Here I will use
a ``string``, but you can imagine that perhaps a complex number may not
be allowed. So, we can write:

.. code:: ipython3

    def power3(*args):
        if type(args[0]) is str:
            print('Oops. You sent me a string.')
            return
        else:
            return power(*args,3)

.. code:: ipython3

    power3(5, 2)

.. parsed-literal::

    40

.. code:: ipython3

    power3('Hello')

.. parsed-literal::

    Oops. You sent me a string.

Note that the string was packed into a tuple of length 1 so the code
must access the 0th value.

The key here is the ``*``, not the name ``args``. Any variable name
could have been used.

So what about ``**kwargs``?
---------------------------

This is the same situation, but this time with named variables and
dictionaries. This time consider writing a central finite differences
operator such that

.. math::

   \frac{df}{dt}:=\frac{f(t+\Delta t/2)-f(t-\Delta t/2)}{\Delta t}

However, if we want this to work for any function returning a numerical
value, but with an unknown set of unnamed and named arguments, we can
abstract by using ``*args`` and ``**kwargs``:

.. code:: ipython3

    def diff(f, t, dt, *args, **kwargs):
        return (f(t+dt/2, *args, **kwargs)
                -f(t-dt/2, *args, **kwargs))/dt

``f`` is the name of the function we will calculate the slope of, ``t``
is the variable we want the slope with respect to, ``dt`` is a step size
for that derivative. All other arguments, named or not, at passed
directly through to the function ``f``.

Let’s define our power function again.

.. code:: ipython3

    def power(t, coeff=5, exponent=3):
        return coeff*t**exponent

Next we obtain the slope when :math:`t=2`, with a coefficient of 2 and
exponent of 3.

.. code:: ipython3

    diff(power, 2, 0.001, coeff=2, exponent=3)

.. parsed-literal::

    24.012001999995647

This can work with any other similarly formed function. This is a simple
product of the three arguments, 2 unnamed, one named.

.. code:: ipython3

    def product(x, y, z=3):
        return x*y*z

We obtain the slope at :math:`x=2` with :math:`y=4` and :math:`z=3`.

.. code:: ipython3

    diff(product, 2, .01, 4, z=3)

.. parsed-literal::

    11.999999999999744

The keys for using ``**kwargs`` is to remember: - ``kwargs`` is your
variable name. You decide what it is. - ``kwargs`` is now a dictionary.
If you want to use them to call another function, make sure to unpack it
in the function call by using ``**``. - You can access parts of kwargs
just as you can any other dictionary.

Conclusion
----------

Hopefully this at least clarifies why they are useful and how you can apply them.  In my experience, they are most useful when a function is designed to call a future (as yet defined) that requires parameters that can not be anticipated. Regardless, please
leave your comments. I hope this helps.

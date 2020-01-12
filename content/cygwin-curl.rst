Getting cURL to work in Cygwin
###########################################

:date: 2016-Mar-01 14:00 EDT
:tags: Programming, Cygwin, cURL, Octave
:category: Programming
:slug: cygwin-curl
:author: Joseph C. Slater
:summary: Getting cURL to work in Cygwin
:Status: published

Cygwin is a great option for Windows users who want to run Linux
software. However, it doesn't always work "right." In my case, trying
to install packages in `Octave <octave.org>`_ from repositories on
`GitHub <github.com>`_ simply would not work. The root cause
seems to be that :code:`curl` wouldn't connect for a variety of
reasons, one being the inability to ''resolve the host'', the other
being the inability to follow redirects (which I wasn't aware of
happening for a very long time)

Two options came to solve the issue.

a. The -4 option, which helped resolve the host

b. The -L option, which enables curl to follow redirects.

With that, the call

.. code-block:: unix

		curl -4 -L https://github.com/vibrationtoolbox/ovtoolbox/archive/master.zip > vtoolbox_temp.zip

works and can be used in the `Octave <octave.org>`_ :code:`system`
command.

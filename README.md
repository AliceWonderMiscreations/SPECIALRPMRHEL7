SPECIALRPMRHEL7
===============

Spec files for software that is not provided via one of my yum repositories.

Most of these packages I can not distribute binary RPMs for due to legal
reasons. The LaTeX stuff is a work in progress.

NoSource Packages
-----------------

NoSource RPMs are available at http://awel.domblogger.net/7/special/

Adobe Flash Plugin
------------------

The Adobe Flash plugin is distributed as an RPM by Adobe but their RPM contains
a lot of stuff that I just do not want or need, such as iconds and KDE files to
run flash on the desktop, something I have no interest in ever doing and that I
suspect most people have no interest in doing.

The RPM spec file here allows you to take the Adobe Flash tarball release and
create an RPM package that will just install the plugin, and put it in the
right place.

Oracle Java
-----------

The open source Java stack has come a long way but there are still some parts
that are not implemented due to licensing issues. As such there is still a
need to use Oracle Java from time to time.

The RPM spec file here allows you to create an RPM file that will install
Oracle Java in `/opt/oracle-java` and will set up the necessary
`/etc/alternatives` symlinks for you.

It also installs a file into `/etc/profile.d` that sets your `JAVA_HOME`
environmental variable and puts the Oracle Java bin directory at the end of
your `PATH`.

texlive-usrlocal
----------------

README.md content to be written.

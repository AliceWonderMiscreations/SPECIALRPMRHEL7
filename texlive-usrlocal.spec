%define tlivev 2014

Name:		texlive-usrlocal
Version:	%{tlivev}
Release:	1.1
Summary:	Meta package to avoid RPM dependency hell

Group:		Applications/Publishing
License:	Public Domain
URL:		http://awel.domblogger.net/
BuildArch:	noarch

#for the tl-install.sh, tlmgr, etc
Requires:	perl(Digest::MD5)
#meta provides - will add to list as it grows
Provides:	tex(latex) = %{version}
# for -latex
Provides:	texlive-dvipng-bin = %{version}
# for dblatex
Provides:	texlive-base = %{version}
Provides:	texlive-collection-latex = %{version}
Provides:	texlive-collection-xetex = %{version}
Provides:	texlive-collection-htmlxml = %{version}
Provides:	texlive-collection-fontsrecommended = %{version}
Provides:	texlive-epstopdf-bin = %{version}
Provides:	texlive-passivetex = %{version}
Provides:	texlive-xmltex = %{version}
Provides:	texlive-xmltex-bin = %{version}
Provides:	texlive-anysize = %{version}
Provides:	texlive-appendix = %{version}
Provides:	texlive-bibtopic = %{version}
Provides:	texlive-changebar = %{version}
Provides:	texlive-ec = %{version}
Provides:	texlive-jknapltx = %{version}
Provides:	texlive-multirow = %{version}
Provides:	texlive-overpic = %{version}
Provides:	texlive-passivetex = %{version}
Provides:	texlive-pdfpages = %{version}
Provides:	texlive-subfigure = %{version}
Provides:	texlive-stmaryrd = %{version}


%description
Many of us like to use TeXLive installed within /usr/local/texlive rather than
the often outdated RPM install of TeXLive. The problem is that RPMs that have
a dependency on TeX will pull in hundreds of TeXLive packages that we do not
use not want. It is particularly annoying when there are a bunch of updates to
the texlive-* RPM packages that we do not even want in the first place.

This meta-package attempts to give virtual provides to satisfy packages that
explicitly require a TeX system so we can avoid that.

It also creates an /etc/profile.d/texlive.sh script to set up the path for
users so that the installed TeXLive is in their path.


%prep
%setup -q -c -T


%build


%install
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat <<EOF > %{buildroot}%{_sysconfdir}/profile.d/texlive.sh
# %{_sysconfdir}/profile.d/texlive.sh
export PATH=/usr/local/texlive/%{tlivev}/bin/\`uname -i\`-linux:\${PATH}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config %attr(0644,root,root) %{_sysconfdir}/profile.d/texlive.sh



%changelog
* Thu Oct 02 2014 Alice Wonder <alicewonder@shastaherps.org> - 2014-1.1
- Added a bunch of virtual provides
- TODO: Wrapper to /usr/bin stuff (e.g. texhash)
-       Consider setting up a TEXMF where RHEL packages put their
-         own custom macros
-       Properly version the provides

* Wed Oct 01 2014 Alice Wonder <alicewonder@shastaherps.org> - 2014-1
- Initial RPM spec file

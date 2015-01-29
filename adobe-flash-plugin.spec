%define majorversion 11
%define minorversion 2
%define subrelease 202.440
%define adobearch x86_64
%define debug_package %{nil}

Name:		adobe-flash-plugin
Version:	%{majorversion}.%{minorversion}.%{subrelease}
Release:	1
Summary:	Adobe Flash Plugin
ExclusiveArch:	x86_64

Group:		Applications/Multimedia
License:	http://www.adobe.com/products/eulas/players/flash/
URL:		http://get.adobe.com/flashplayer/otherversions/
Source0:	install_flash_player_%{majorversion}_linux.%{adobearch}.tar.gz
nosource:	0
#72054dbbceabda51bce37137568e2a1b  install_flash_player_11_linux.x86_64.tar.gz

#BuildRequires:	
Requires:	mozilla-filesystem
Obsoletes:	flash-plugin <= %{version}

%description
This package provides the Mozilla Plugin for Adobe Flash. Adobe Flash is used
to serve multimedia, games, advertisements, and malware on the World Wide Web.


%prep
%setup -q -c


%build


%install
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins
install -m755 libflashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc readme.txt
%{_libdir}/mozilla/plugins/libflashplayer.so



%changelog
* Thu Jan 29 2015 Alice Wonder <rpmbuild@domblogger.net> - 11.2.202.440-1
- update to 11.2.202.440

* Sat Dec 13 2014 Alice Wonder <rpmbuild@domblogger.net> - 11.2.202.425-1
- update to 11.2.202.425

* Wed Oct 01 2014 Alice Wonder <rpmbuild@domblogger.net> - 11.2-1
- Initial RPM spec file

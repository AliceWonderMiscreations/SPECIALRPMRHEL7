%define debug_package %{nil}

Name:		NeroAACCodec
Version:	1.5.1
Release:	1
Summary:	Nero ACC encoder / decoder for GNU/Linux

Group:		Applications/Multimedia
License:	Commercial
URL:		http://www.nero.com/enu/company/about-nero/nero-aac-codec.php
Source0:	%{name}-%{version}.zip
nosource:	0

%description
This package includes the Nero AAC encoder, decoder, and tag utility for i686
Linux. It will install on x86_64 if you also install some compatibility libs.


%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 linux/neroAacDec %{buildroot}%{_bindir}/
install -m755 linux/neroAacEnc %{buildroot}%{_bindir}/
install -m755 linux/neroAacTag %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc changelog.txt license.txt NeroAAC_tut.pdf readme.txt
%{_bindir}/*



%changelog
* Wed Oct 08 2014 Alice Wonder <alicewonder@shastaherps.org> - 1.5.1-1
- Initial spec file

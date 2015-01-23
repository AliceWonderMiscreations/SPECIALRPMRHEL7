%define majorversion 1.8.0
%define minorversion 31
%define sversion 8u%{minorversion}
%define sarch x64
%define jrearch amd64
%define debug_package %{nil}
# DO NOT REPACK THE JARS
%define __os_install_post \
  /usr/lib/rpm/redhat/brp-compress \
  /usr/lib/rpm/redhat/brp-strip %{__strip} \
  /usr/lib/rpm/redhat/brp-strip-static-archive %{__strip} \
  /usr/lib/rpm/redhat/brp-strip-comment-note %{__strip} %{__objdump} \
%{nil}

Name:		oracle-java-jdk
Version:	%{sversion}
Release:	1
Summary:	Oracle Java Developer Kit

Group:		System Environment/Java
License:	http://www.oracle.com/technetwork/java/javase/terms/license/index.html
URL:		http://www.oracle.com/technetwork/java/javase/downloads/index.html
Source0:	jdk-%{sversion}-linux-%{sarch}.tar.gz
ExclusiveArch:	x86_64

nosource:	0

AutoReqProv:	no
Requires(post):	%{_sbindir}/update-alternatives
Requires(preun):%{_sbindir}/update-alternatives

%description
This is Oracle Java. It sometimes is needed for applications that do not
properly work with Open Source Java implementations.


%prep
%setup -q -c


%build


%install
mkdir -p %{buildroot}/opt/oracle-java
cp -ar jdk%{majorversion}_%{minorversion} %{buildroot}/opt/oracle-java/
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat <<EOF > %{buildroot}%{_sysconfdir}/profile.d/oracle-java.sh
#/etc/profile.d/oracle-java.sh
export JAVA_HOME=/opt/oracle-java/jdk%{majorversion}_%{minorversion}
export PATH=\${PATH}:\${JAVA_HOME}/bin
EOF

%clean
rm -rf %{buildroot}

%post
%{_sbindir}/update-alternatives --install "%{_bindir}/java" "java" "/opt/oracle-java/jdk%{majorversion}_%{minorversion}/java" 1
%{_sbindir}/update-alternatives --install "%{_bindir}/javac" "javac" "/opt/oracle-java/jdk%{majorversion}_%{minorversion}/javac" 1
%{_sbindir}/update-alternatives --install "%{_bindir}/javaws" "javaws" "/opt/oracle-java/jdk%{majorversion}_%{minorversion}/javaws" 1
%{_sbindir}/update-alternatives --install "%{_libdir}/mozilla/plugins/libjavaplugin.so" "libjavaplugin.so" "/opt/oracle-java/jdk%{majorversion}_%{minorversion}/jre/lib/%{jrearch}/libnpjp2.so" 1

%{_sbindir}/update-alternatives --set java /opt/oracle-java/jdk%{majorversion}_%{minorversion}/java
%{_sbindir}/update-alternatives --set javac /opt/oracle-java/jdk%{majorversion}_%{minorversion}/javac
%{_sbindir}/update-alternatives --set javaws /opt/oracle-java/jdk%{majorversion}_%{minorversion}/javaws
%{_sbindir}/update-alternatives --set libjavaplugin.so /opt/oracle-java/jdk%{majorversion}_%{minorversion}/jre/lib/%{jrearch}/libnpjp2.so

%preun
%{_sbindir}/update-alternatives --remove "java" "/opt/oracle-java/jdk%{majorversion}_%{minorversion}/java"
%{_sbindir}/update-alternatives --remove "javac" "/opt/oracle-java/jdk%{majorversion}_%{minorversion}/javac"
%{_sbindir}/update-alternatives --remove "javaws" "/opt/oracle-java/jdk%{majorversion}_%{minorversion}/javaws"
%{_sbindir}/update-alternatives --remove "libjavaplugin.so" "/opt/oracle-java/jdk%{majorversion}_%{minorversion}/jre/lib/%{jrearch}/libnpjp2.so"

%files
%defattr(-,root,root,-)
%dir /opt/oracle-java
/opt/oracle-java/jdk%{majorversion}_%{minorversion}
%attr(0644,root,root) %{_sysconfdir}/profile.d/oracle-java.sh



%changelog
* Fri Jan 23 2015 Alice Wonder <rpmbuild@domblogger.net> - 8u31-1
- Update to 8u31

* Wed Oct 01 2014 Alice Wonder <rpmbuild@domblogger.net> - 8u20-1
- Initial spec file (admittedly somewhat dirty - should have some
-  subpackages)

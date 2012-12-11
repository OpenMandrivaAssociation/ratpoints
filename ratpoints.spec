%define		name		ratpoints

Name:		%{name}
Group:		Sciences/Mathematics
License:	GPLv2
Summary:	Find rational points on hyperelliptic curves
Version:	2.1.3
Release:	%mkrel 3
Source0:	http://www.mathe2.uni-bayreuth.de/stoll/programs/%{name}-%{version}.tar.gz
URL:		http://www.sagemath.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	gmp-devel
BuildRequires:	gzip

Patch0:		ratpoints-2.1.2.patch

%description
Ratpoints is a program that uses an optimized quadratic sieve algorithm
in order to find rational points on hyperelliptic curves.

%prep
%setup -q

%patch0	-p1

%build
%make CCFLAGS="%{optflags} -fPIC"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
%makeinstall_std LIBDIR=%{_libdir} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/ratpoints
%{_includedir}/ratpoints.h
%{_libdir}/libratpoints.a


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.3-3mdv2011.0
+ Revision: 614700
- the mass rebuild of 2010.1 packages

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 2.1.3-2mdv2010.1
+ Revision: 503624
- rebuild for new gmp

* Wed Jan 27 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.1.3-1mdv2010.1
+ Revision: 496891
- Update to newer version 2.1.3.

* Thu Jul 16 2009 Paulo Andrade <pcpa@mandriva.com.br> 2.1.2-2mdv2010.0
+ Revision: 396508
+ rebuild (emptylog)

* Wed Jul 15 2009 Paulo Andrade <pcpa@mandriva.com.br> 2.1.2-1mdv2010.0
+ Revision: 396435
- Initial import of ratpoints 2.1.2.
  http://www.mathe2.uni-bayreuth.de/stoll/programs/index.html
- ratpoints


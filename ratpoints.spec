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

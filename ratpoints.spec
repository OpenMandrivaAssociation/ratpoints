%global major	0

%ifarch %{x86_64}
%global use_sse -DUSE_SSE
%else
%global use_sse %{nil}
%endif

Name:		ratpoints
Version:	2.2.1
Release:	1%{?dist}
Summary:	Find rational points on hyperelliptic curves
License:	GPLv2+
URL:		http://www.mathe2.uni-bayreuth.de/stoll/programs/
Source0:	http://www.mathe2.uni-bayreuth.de/stoll/programs/%{name}-%{version}.tar.gz
# Initially generated with help2man as:
# LD_LIBRARY_PATH=$PWD: help2man --section=1 --no-info \
#    --version-string="%%{version}" \
#    -o $RPM_BUILD_ROOT/%%{_mandir}/man1/ratpoints.1 ./ratpoints
# but edited for better formatting.
Source1:	%{name}.1
Source2:	%{name}.rpmlintrc
BuildRequires:	gmp-devel
Patch0:		%{name}-shared.patch

%description
Ratpoints is a program that uses an optimized quadratic sieve algorithm
in order to find rational points on hyperelliptic curves.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Header and library for development with %{name}.

%prep
%autosetup -p1

sed -e "s/-Wall -O2 -fomit-frame-pointer/%{optflags} %{use_sse}/" \
   -e "s/-shared/& $RPM_LD_FLAGS -lgmp -lm/" \
   -i Makefile

%build
%make_build

%install
%make_install LIBDIR=%{_libdir}
install -p -D -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1

%check
LD_LIBRARY_PATH=$PWD: make test

%files
%doc gpl-2.0.txt
%doc ratpoints-doc.pdf
%{_bindir}/ratpoints
%{_libdir}/libratpoints.so.%{major}
%{_mandir}/man1/ratpoints.1*

%files		devel
%{_includedir}/ratpoints.h
%{_libdir}/libratpoints.so

%define		fversion	%(echo %{version} |tr r -)
%define		modulename	gee
Summary:	Generalized Estimation Equation solver
Summary(pl.UTF-8):	Rozwiązywanie uogólnionych równań estymacji
Name:		R-cran-%{modulename}
Version:	4.13r18
Release:	3
License:	GPL v2
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	7a74002026426cfbb58e212bf31af38c
BuildRequires:	R >= 2.8.1
BuildRequires:	blas-devel
BuildRequires:	gcc-fortran
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generalized Estimation Equation solver.

%description -l pl.UTF-8
Rozwiązywanie uogólnionych równań estymacji.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README*}
%{_libdir}/R/library/%{modulename}

%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pnam	Basic
Summary:	Inline::Basic perl module
Summary(pl):	Modu³ perla Inline::Basic
Name:		perl-Inline-Basic
Version:	0.01
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-IO-stringy >= 2.104
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-Language-Basic >= 1.44
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Basic - Write Perl subroutines in Basic.

%description -l pl
Modu³ Inline::Basic - pozwalaj±cy na pisanie procedur Perla w Basicu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Inline/Basic.pm
%{_mandir}/man3/*

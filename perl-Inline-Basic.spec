#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Basic
Summary:	Inline::Basic Perl module
Summary(cs):	Modul Inline::Basic pro Perl
Summary(da):	Perlmodul Inline::Basic
Summary(de):	Inline::Basic Perl Modul
Summary(es):	M�dulo de Perl Inline::Basic
Summary(fr):	Module Perl Inline::Basic
Summary(it):	Modulo di Perl Inline::Basic
Summary(ja):	Inline::Basic Perl �⥸�塼��
Summary(ko):	Inline::Basic �� ����
Summary(nb):	Perlmodul Inline::Basic
Summary(pl):	Modu� Perla Inline::Basic
Summary(pt):	M�dulo de Perl Inline::Basic
Summary(pt_BR):	M�dulo Perl Inline::Basic
Summary(ru):	������ ��� Perl Inline::Basic
Summary(sv):	Inline::Basic Perlmodul
Summary(uk):	������ ��� Perl Inline::Basic
Summary(zh_CN):	Inline::Basic Perl ģ��
Name:		perl-Inline-Basic
Version:	0.01
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68c9f06777d68133b5ebcdea3bba0f44
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-IO-stringy >= 2.104
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-Language-Basic >= 1.44
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Basic - Write Perl subroutines in Basic.

%description -l pl
Modu� Inline::Basic - pozwalaj�cy na pisanie procedur Perla w Basicu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Inline/Basic.pm
%{_mandir}/man3/*

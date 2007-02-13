#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Basic
Summary:	Inline::Basic Perl module
Summary(cs.UTF-8):	Modul Inline::Basic pro Perl
Summary(da.UTF-8):	Perlmodul Inline::Basic
Summary(de.UTF-8):	Inline::Basic Perl Modul
Summary(es.UTF-8):	Módulo de Perl Inline::Basic
Summary(fr.UTF-8):	Module Perl Inline::Basic
Summary(it.UTF-8):	Modulo di Perl Inline::Basic
Summary(ja.UTF-8):	Inline::Basic Perl モジュール
Summary(ko.UTF-8):	Inline::Basic 펄 모줄
Summary(nb.UTF-8):	Perlmodul Inline::Basic
Summary(pl.UTF-8):	Moduł Perla Inline::Basic
Summary(pt.UTF-8):	Módulo de Perl Inline::Basic
Summary(pt_BR.UTF-8):	Módulo Perl Inline::Basic
Summary(ru.UTF-8):	Модуль для Perl Inline::Basic
Summary(sv.UTF-8):	Inline::Basic Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Inline::Basic
Summary(zh_CN.UTF-8):	Inline::Basic Perl 模块
Name:		perl-Inline-Basic
Version:	0.01
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68c9f06777d68133b5ebcdea3bba0f44
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-IO-stringy >= 2.104
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-Language-Basic >= 1.44
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Basic - Write Perl subroutines in Basic.

%description -l pl.UTF-8
Moduł Inline::Basic - pozwalający na pisanie procedur Perla w Basicu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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

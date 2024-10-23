%define modname	Test-Base

%if %{_use_internal_dependency_generator}
%define __noautoreq 'Module::Install.*'
%else
%define _requires_exceptions Module::Install
%endif

Summary:	A Data Driven Testing Framework
Name:		perl-%{modname}
Version:	0.89
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Test::Base
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Spiffy)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl-devel

%description
Perl gives you a standard way to run tests with Test::Harness, and basic
testing primitives with Test::More. After that you are pretty much on your own
to develop a testing framework and philosophy. Test::More encourages you to
make your own framework by subclassing Test::Builder, but that is not trivial.
Test::Base gives you a way to write your own test framework base class that is
trivial.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/Test
# %{perl_vendorlib}/Module
%{_mandir}/man3/*

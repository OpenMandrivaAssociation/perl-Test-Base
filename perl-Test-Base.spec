%define modname	Test-Base
%define modver 0.89

%if %{_use_internal_dependency_generator}
%define __noautoreq 'Module::Install.*'
%else
%define _requires_exceptions Module::Install
%endif

Summary:	A Data Driven Testing Framework
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Test::Base
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Spiffy) >= 0.29
BuildRequires:	perl(Test::More) >= 0.62
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
%autosetup -p1 -n %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test
# %{perl_vendorlib}/Module
%{_mandir}/man3/*

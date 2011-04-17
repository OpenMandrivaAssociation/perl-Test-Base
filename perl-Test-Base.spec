%define upstream_name	 Test-Base
%define upstream_version 0.60

%define _requires_exceptions Module::Install

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A Data Driven Testing Framework
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Spiffy) >= 0.29
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(Test::Deep)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Perl gives you a standard way to run tests with Test::Harness, and basic
testing primitives with Test::More. After that you are pretty much on your own
to develop a testing framework and philosophy. Test::More encourages you to
make your own framework by subclassing Test::Builder, but that is not trivial.
Test::Base gives you a way to write your own test framework base class that is
trivial.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %buildroot
%makeinstall_std

%clean 
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%perl_vendorlib/Test
%perl_vendorlib/Module
%_mandir/*/*

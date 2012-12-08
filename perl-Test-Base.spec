%define upstream_name	 Test-Base
%define upstream_version 0.60

%define _requires_exceptions Module::Install

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5

Summary:	A Data Driven Testing Framework
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Spiffy) >= 0.29
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl-devel
BuildArch:	noarch

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
%makeinstall_std

%files
%doc Changes README
%perl_vendorlib/Test
%perl_vendorlib/Module
%_mandir/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.600.0-4mdv2012.0
+ Revision: 765673
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.600.0-3
+ Revision: 764184
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.600.0-2
+ Revision: 763101
- rebuild

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.600.0-1
+ Revision: 654379
- update to new version 0.60

* Mon Aug 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.590.0-1mdv2011.0
+ Revision: 420264
- update to 0.59

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.580.0-1mdv2010.0
+ Revision: 408086
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.58-1mdv2010.0
+ Revision: 370186
- update to new version 0.58

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.56-1mdv2009.1
+ Revision: 353023
- update to new version 0.56

* Mon Dec 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdv2009.1
+ Revision: 311973
- update to new version 0.55

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.54-3mdv2009.0
+ Revision: 224133
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.54-2mdv2008.1
+ Revision: 180585
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.54-1mdv2008.0
+ Revision: 46230
- 0.54


* Wed Dec 13 2006 Olivier Thauvin <nanardon@mandriva.org> 0.53-1mdv2007.0
+ Revision: 96137
- 0.53
- Import perl-Test-Base

* Tue Jun 20 2006 Scott Karns <scottk@mandriva.org> 0.52-1mdv2007.0
- 0.52

* Wed Mar 08 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.50-2mdk
- No Perl module should ever require Module::Install

* Mon Feb 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.50-1mdk
- 0.50

* Mon Jan 30 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.48-1mdk
- 0.48

* Tue Jan 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.47-1mdk
- 0.47

* Thu Jan 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.46-2mdk
- Add BuildRequires
- Fix source url

* Thu Jan 19 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.46-1mdk
- 0.46

* Wed Jan 11 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.45-1mdk
- Initial MDV release.


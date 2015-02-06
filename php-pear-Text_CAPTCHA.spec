%define		_class		Text
%define		_subclass	CAPTCHA
%define		upstream_name	%{_class}_%{_subclass}
Name:		php-pear-%{upstream_name}
Version:	1.0.2
Release:	2
Summary:	Generation of CAPTCHA imgaes
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Text_CAPTCHA/
Source0:	http://download.pear.php.net/package/Text_CAPTCHA-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Implementation of CAPTCHA (completely automated public Turing test to
tell computers and humans apart) images.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-6mdv2012.0
+ Revision: 742286
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-5
+ Revision: 679590
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-4mdv2011.0
+ Revision: 613782
- the mass rebuild of 2010.1 packages

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-3mdv2010.1
+ Revision: 466320
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-2mdv2010.0
+ Revision: 441656
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.3.1-1mdv2009.1
+ Revision: 368335
- Update php pear Text_CAPTCHA to 0.3.1 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-3mdv2009.1
+ Revision: 322671
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-2mdv2009.0
+ Revision: 237110
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-1mdv2008.0
+ Revision: 15754
- 0.2.1


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-1mdv2007.0
+ Revision: 82747
- Import php-pear-Text_CAPTCHA

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-1mdk
- 0.1.6
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-1mdk
- initial Mandriva package (PLD import)





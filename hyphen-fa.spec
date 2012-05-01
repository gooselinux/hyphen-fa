Name: hyphen-fa
Summary: Farsi hyphenation rules
%define upstreamid 20081119
Version: 0.%{upstreamid}
Release: 2.1%{?dist}
Source: http://www.ctan.org/get/language/hyphenation/fahyph.zip
Group: Applications/Text
URL: http://www.ctan.org/tex-archive/help/Catalogue/entries/fahyph.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LPPL
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Patch0: hyphen-fa-cleantex.patch

%description
Farsi hyphenation rules.

%prep
%setup -q -n fahyph
%patch0 -p1 -b .clean

%build
substrings.pl fahyph.tex hyph_fa_IR.dic UTF-8
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_fa_IR.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20081119-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 18 2009 Caolan McNamara <caolanm@redhat.com> - 0.20081119-1
- initial version

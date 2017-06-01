%global pixmaptarget %{_datadir}/lorax/product/usr/share/anaconda/pixmaps
%global pixmapsource %{_datadir}/anaconda/pixmaps/cloud

Name:           fedora-productimg-cloud
Version:        26
Release:        1%{?dist}
Summary:        Installer branding and configuration for Fedora Cloud

# Copyright and related rights waived via CC0
# http://creativecommons.org/publicdomain/zero/1.0/
License:        CC0

Source0:        anaconda-gtk.css
Source1:        fedora-cloud.py

BuildArch:      noarch

BuildRequires:  cpio
BuildRequires:  findutils
BuildRequires:  xz
BuildRequires:  python3-devel

Provides:       lorax-product-cloud
Conflicts:      fedora-productimg-workstation, fedora-productimg-server

%description
This package contains differentiated branding and configuration for Fedora
Cloud for use in a product.img file for Anaconda, the Fedora installer. It
is not useful on an installed system.

%prep

%build

%install

install -m 755 -d %{buildroot}%{pixmaptarget}

install -m 644 %{SOURCE0} %{buildroot}%{pixmaptarget}/../

mkdir -p %{buildroot}%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses

ln -sf %{pixmapsource}/sidebar-bg.png %{buildroot}%{pixmaptarget}
ln -sf %{pixmapsource}/topbar-bg.png %{buildroot}%{pixmaptarget}

# note filename change with this one
ln -sf %{pixmapsource}/sidebar-logo.png %{buildroot}%{pixmaptarget}/sidebar-logo_flavor.png

install -m 755 -d %{buildroot}%{_datadir}/fedora-productimg

pushd %{buildroot}%{_datadir}/lorax/product/
find %{buildroot}%{_datadir}/lorax/product/ -depth -printf '%%P\0' | \
   cpio --null --quiet -H newc -o | \
   xz -9 > \
   %{buildroot}%{_datadir}/fedora-productimg/product.img
popd


%files
%dir %{_datadir}/lorax/product/usr/share/anaconda
%{_datadir}/lorax/product/usr/share/anaconda/anaconda-gtk.css
%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses/fedora-cloud.py*
%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses/__pycache__/fedora-cloud.*.pyc
%dir %{_datadir}/lorax/product/usr/share
%dir %{_datadir}/lorax/product/usr
%dir %{pixmaptarget}
%{pixmaptarget}/*.png
%dir %{_datadir}/fedora-productimg
%{_datadir}/fedora-productimg/product.img

%changelog
* Thu Mar  2 2017 Peter Robinson <pbrobinson@fedoraproject.org> 26-1
- Add Fedora Cloud storage customisation

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Matthew Miller <mattdm@fedoraproject.org> 22-5
- correctly pregenerate product.img cpio archive

* Thu Nov 20 2014 Matthew Miller <mattdm@fedoraproject.org> 22-4
- provides lorax-product-cloud

* Thu Nov 20 2014 Matthew Miller <mattdm@fedoraproject.org> 22-3
- merge changes in from f21

* Fri Nov  7 2014 Matthew Miller <mattdm@fedoraproject.org> 22-1
- bump to 22 for rawhide

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-2
- conflict with the other fedora-productimg packages

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-1
- change license to CC0

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-0
- Initial creation for Fedora 21

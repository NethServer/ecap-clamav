Summary:	Clamav ecap module
Name:		ecap-clamav
Version:	2.0.0
Release:	1%{?dist}
License:	BSD
Group:		Networking/Other
URL:		http://www.ecap.org
Source0:	http://www.measurement-factory.com/tmp/ecap/ecap_clamav_adapter-%{version}.tar.gz
Patch0:		ecap_clamav_adapter-2.0.0-size-mismatch.patch
BuildRequires:	libecap-devel
BuildRequires:	libecap
BuildRequires:	clamav-devel
Requires:	squid

%description
The clamav component contains ecap interface for clamav.

%prep
%setup -n ecap_clamav_adapter-%{version}
%autopatch -p1

%build
%configure
make

%install
make install DESTDIR=%{buildroot}

%files
%{_libdir}/ecap_clamav_adapter.*


%changelog
* Wed Dec 16 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.0.1
- Rebuilt for CentOS 7

* Mon Mar 14 2016 luigiwalser <luigiwalser> 2.0.0-2.mga6
+ Revision: 990681
- add patch to fix data type mismatch

  + pterjan <pterjan>
    - Update to 2.0.0 to support current libecap

  + umeabot <umeabot>
    - Mageia 6 Mass Rebuild

  + tv <tv>
    - rebuild for new libecap + libclamav

  + daviddavid <daviddavid>
    - rebuild for new ecap

* Wed Oct 15 2014 umeabot <umeabot> 0.2.1-5.mga5
+ Revision: 745121
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 0.2.1-4.mga5
+ Revision: 678919
- Mageia 5 Mass Rebuild

* Sat Oct 19 2013 umeabot <umeabot> 0.2.1-3.mga4
+ Revision: 533834
- Mageia 4 Mass Rebuild

* Sat Sep 07 2013 dlucio <dlucio> 0.2.1-2.mga4
+ Revision: 475574
- spec fixes
- squid as a require

* Fri Sep 06 2013 dlucio <dlucio> 0.2.1-1.mga4
+ Revision: 475556
- P0 added
- imported package ecap-clamav


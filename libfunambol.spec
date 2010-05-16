Summary:	Funambol C++ API
Name:		libfunambol
Version:	7.0.2
Release:	0.1
License:	AFP v3
Group:		Libraries
Source0:	http://download.forge.objectweb.org/sync4j/funambol-cpp-api-%{version}.zip
# Source0-md5:	c3b04af2cda12e42e6822c8ee57c7112
URL:		http://www.funambol.org/
BuildRequires:	curl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This SDK allows to integrate a syncml stack in a C++ application on a
variety of platforms. Currently, Windows, WinMobile and Linux are
actively supported, but you can easily build it on other Unixes or
other mobile/embedded platforms.

%package devel
Summary:	Header files for Funambol C++ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Funambol C++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Funambol C++ library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Funambol C++.

%package static
Summary:	Static Funambol C++ library
Summary(pl.UTF-8):	Statyczna biblioteka Funambol C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Funambol C++ library.

%description static -l pl.UTF-8
Statyczna biblioteka Funambol C++.

%package apidocs
Summary:	Funambol C++ API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Funambol C++
Group:		Documentation

%description apidocs
API and internal documentation for Funambol C++ library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Funambol C++.

%prep
%setup -qc

%build
cd Funambol/sdk/c++/build/autotools
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C Funambol/sdk/c++/build/autotools install \
	DESTDIR=$RPM_BUILD_ROOT

# WTF? is under here? .h should go to include dir not test data
rm -rf $RPM_BUILD_ROOT%{_includedir}/funambol/test

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Funambol/sdk/c++/{changeslog.txt,cvshistory.txt,README,TODO.txt}
%attr(755,root,root) %{_libdir}/libfunambol.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfunambol.so.3

%files devel
%defattr(644,root,root,755)
%doc Funambol/sdk/c++/build/autotools/README
%{_includedir}/funambol
%{_libdir}/libfunambol.la
%{_libdir}/libfunambol.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libfunambol.a

Summary:	Exif and Iptc metadata manipulation tools
Name:		exiv2
Version:	0.24
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.exiv2.org/%{name}-%{version}.tar.gz
# Source0-md5:	b8a23dc56a98ede85c00718a97a8d6fc
Patch0:		%{name}-cmake_LIB_SUFFIX.patch
Patch1:		%{name}-cmake_mandir.patch
URL:		http://www.exiv2.org/
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exif and Iptc metadata manipulation tools.

%package libs
Summary:	Exif and Iptc metadata manipulation library
Group:		Libraries

%description libs
Exif and Iptc metadata manipulation library.

%package devel
Summary:	Exif and Iptc metadata manipulation library development files
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	zlib-devel

%description devel
Exif and Iptc metadata manipulation library development files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake .. \
	-DEXIV2_ENABLE_BUILD_PO:BOOL=ON	\
	-DEXIV2_ENABLE_BUILD_SAMPLES=ON

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/exiv2.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libexiv2.so.13
%attr(755,root,root) %{_libdir}/libexiv2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexiv2.so
%{_includedir}/%{name}
%{_pkgconfigdir}/exiv2.pc


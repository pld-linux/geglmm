Summary:	C++ bindings for GEGL
Summary(pl.UTF-8):	Wiązania C++ do GEGL
Name:		geglmm
Version:	0.0.22
Release:	1
License:	LGPL v3
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/geglmm/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	70cb8d6a97b0d51cc25bde84f4593786
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	gegl-devel >= 0.0.22
BuildRequires:	glibmm-devel >= 2.12.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ bindings for GEGL.

%description -l pl.UTF-8
Wiązania C++ do GEGL.

%package devel
Summary:	Header files for geglmm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki geglmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gegl-devel >= 0.0.22
Requires:	glibmm-devel >= 2.12.8

%description devel
Header files for geglmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki geglmm.

%package static
Summary:	Static geglmm library
Summary(pl.UTF-8):	Statyczna biblioteka geglmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static geglmm library.

%description static -l pl.UTF-8
Statyczna biblioteka geglmm.

%package examples
Summary:	geglmm - example programs
Summary(pl.UTF-8):	geglmm - przykładowe programy
Group:		Development/Libraries

%description examples
geglmm - example programs.

%description examples -l pl.UTF-8
geglmm - przykładowe programy.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Prepare examples
cp examples/*.cc $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgeglmm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgeglmm.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgeglmm.so
%{_libdir}/geglmm-1.0
%{_libdir}/libgeglmm.la
%{_includedir}/geglmm-1.0
%{_pkgconfigdir}/geglmm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgeglmm.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

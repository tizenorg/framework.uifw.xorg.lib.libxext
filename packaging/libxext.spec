Name:       libxext
Summary:    X.Org X11 libXext runtime library
Version:    1.2.0
Release:    2.4
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://cgit.freedesktop.org/xorg/lib/libXext/snapshot/%{name}-%{version}.tar.gz
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xau)


%description
Description: %{summary}


%package devel
Summary:    Development components for the libXext library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}


%prep
%setup -q -n %{name}-%{version}



%build
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"
%reconfigure 

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_libdir}/libXext.so.6
%{_libdir}/libXext.so.6.4.0


%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXext.so
%{_libdir}/pkgconfig/xext.pc
%doc %{_mandir}/man3/*.3*
%doc %{_docdir}/libXext/*


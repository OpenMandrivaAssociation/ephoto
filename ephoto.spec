%define	name	ephoto
%define version 4.15.0
%define release %mkrel 4

Summary: 	Enlightenment photo manager
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphics
URL: 		http://www.enlightenment.org
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.050, ewl-devel >= 0.5.3.050
Buildrequires:	efreet-devel
BuildRequires:	edje >= 0.9.9.050
Buildrequires:  gettext-devel

%description
Ephoto is an ewl app that is used for sophisticate image viewing.
This package is part of the Enlightenment DR17 desktop shell.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post 
%{update_menus} 
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus} 
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/pixmaps/ephoto.png
%{_datadir}/%name
%{_datadir}/applications/*


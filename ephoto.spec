%define efl_version 1.26.2

Summary:	Enlightenment photo manager
Name:		ephoto
Version:	1.6.0
Release:	1
Epoch:		1
License:	BSD
Group:		Graphics
Url:		https://www.enlightenment.org
Source0: 	https://download.enlightenment.org/rel/apps/ephoto/%{name}-%{version}.tar.xz

BuildRequires:  e
BuildRequires:  efl
BuildRequires:	meson
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(efl)
BuildRequires:	pkgconfig(libexif)

%description
Ephoto is an ewl app that is used for sophisticate image viewing.
This package is part of the Enlightenment desktop shell.

%files
%doc AUTHORS COPYING README
%{_bindir}/*
%{_libdir}/ephoto/ephoto_thumbnail
%{_datadir}/applications/ephoto.desktop
%{_datadir}/ephoto/*
%{_datadir}/locale/*/*/*.mo
%{_datadir}/icons/ephoto.png

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson

%meson_build

%install
%meson_install

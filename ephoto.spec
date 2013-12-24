%define gitdate 20131224

Summary:	Enlightenment photo manager
Name:		ephoto
Version:	0.1.1.80000
Release:	0.%{gitdate}.1
Epoch:		1
License:	BSD
Group:		Graphics
Url:		http://www.enlightenment.org
Source0: 	%{name}-%{gitdate}.tar.bz2

BuildRequires:	edje
BuildRequires:	elementary
BuildRequires:	evas
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(ecore-file)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(efreet-mime)
BuildRequires:	pkgconfig(eio)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(ethumb)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	evas_generic_loaders

%description
Ephoto is an ewl app that is used for sophisticate image viewing.
This package is part of the Enlightenment desktop shell.

%files
%doc AUTHORS ChangeLog COPYING COPYING.icons README
%{_bindir}/*
%{_libdir}/*.so
%{_datadir}/%{name}/themes/default/*.edj
%{_datadir}/%{name}/images/*.png
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/ephoto.desktop

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}

%build
autoreconf -fi
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std


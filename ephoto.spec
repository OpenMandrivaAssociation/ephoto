%define gitdate 20150504

Summary:	Enlightenment photo manager
Name:		ephoto
Version:	1.5
Release:	1
Epoch:		1
License:	BSD
Group:		Graphics
Url:		http://www.enlightenment.org
Source0: 	%{name}-%{version}.tar.xz

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
#BuildRequires:	evas_generic_loaders

%description
Ephoto is an ewl app that is used for sophisticate image viewing.
This package is part of the Enlightenment desktop shell.

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*
%{_libdir}/ephoto/ephoto_thumbnail
/usr/lib/debug/%{_libdir}/%{name}/ephoto_thumbnail-%{version}-%{release}.%{_arch}.debug
#%%{_libdir}/*.so
#%%{_datadir}/%%{name}/themes/*.edj
#%%{_datadir}/%%{name}/images/*.png
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/ephoto.desktop
%{_datadir}/ephoto/*
%{_datadir}/locale/*/*/*.mo



#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}

%build
autoreconf -fi
%configure \
	--disable-static

%make_build

%install
%makeinstall_std


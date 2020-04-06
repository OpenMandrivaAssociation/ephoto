%define efl_version 1.23.3

Summary:	Enlightenment photo manager
Name:		ephoto
Version:	1.5
Release:	2
Epoch:		1
License:	BSD
Group:		Graphics
Url:		http://www.enlightenment.org
Source0: 	https://download.enlightenment.org/rel/apps/ephoto/%{name}-%{version}.tar.xz

BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(ecore-file) >= %{efl_version}
BuildRequires:	pkgconfig(edje) >= %{efl_version}
BuildRequires:	pkgconfig(eet) >= %{efl_version}
BuildRequires:	pkgconfig(efreet-mime) >= %{efl_version}
BuildRequires:	pkgconfig(eio) >= %{efl_version}
BuildRequires:	pkgconfig(elementary) >= %{efl_version}
BuildRequires:	pkgconfig(ethumb) >= %{efl_version}
BuildRequires:	pkgconfig(evas) >= %{efl_version}
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
%make_install

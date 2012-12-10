#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/ephoto ephoto; \
#cd ephoto; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf ephoto-$PKG_VERSION.tar.xz ephoto/ --exclude .svn --exclude .*ignore

%define svnrev	79722

Summary: 	Enlightenment photo manager
Name: 		ephoto
Epoch:		1
Version: 	0.1.1.%{svnrev}
Release: 	0.%{svnrev}.1
License: 	BSD
Group: 		Graphics
URL: 		http://www.enlightenment.org
Source0: 	%{name}-%{version}.tar.xz

Buildrequires:	edje
Buildrequires:	elementary
Buildrequires:	evas
Buildrequires:	gettext-devel
BuildRequires:	pkgconfig(edje)
Buildrequires:	pkgconfig(efreet)
Buildrequires:	pkgconfig(eio)
Buildrequires:	pkgconfig(elementary)
Buildrequires:	pkgconfig(ethumb)
BuildRequires:	pkgconfig(evas)
Buildrequires:  pkgconfig(libexif)
Buildrequires:  pkgconfig(eweather)
Buildrequires:  evas_generic_loaders

%description
Ephoto is an ewl app that is used for sophisticate image viewing.
This package is part of the Enlightenment DR17 desktop shell.

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog COPYING COPYING.icons README
%{_bindir}/*
%{_libdir}/*.so
%{_datadir}/%{name}/themes/default/*.edj
%{_datadir}/%{name}/images/*.png
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/ephoto.desktop


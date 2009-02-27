%define	name	ephoto
%define version 4.15.0
%define release %mkrel 1

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment photo manager
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphics
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
Source1:	%name.desktop
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.050, ewl-devel >= 0.5.3.050
Buildrequires:  epsilon-devel >= 0.3.0.012, emotion-devel >= 0.1.0.042
BuildRequires:	ecore-devel >= 0.9.9.050, edje-devel >= 0.5.0.050,  edje >= 0.5.0.050
BuildRequires:	%{mklibname sqlite3_0}-devel, %{mklibname exif-gtk5}-devel
Buildrequires:  gettext-devel, cvs
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils


%description
Ephoto is an ewl app that is used for sophisticate image viewing.
This package is part of the Enlightenment DR17 desktop shell.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# %lang(fr) /usr/share/locale/fr/LC_MESSAGES/ephoto.mo
%find_lang %{name}
for mo in `ls %buildroot%_datadir/locale/` ;
do Y=`echo -n $mo | sed -e "s|/||"`;
echo "%lang($Y) $(echo %_datadir/locale/${mo}/LC_MESSAGES/%{name}.mo)" >> $RPM_BUILD_DIR/%{name}-%{version}/%{name}.lang
done



mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cp -vf %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Graphics" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%name.desktop

mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 data/images/emblem-photos.png %buildroot%_liconsdir/ephoto.png
convert -resize 32x32 data/images/emblem-photos.png %buildroot%_iconsdir/ephoto.png
convert -resize 16x16 data/images/emblem-photos.png %buildroot%_miconsdir/ephoto.png

mkdir -p %buildroot%{_datadir}/pixmaps
cp data/images/emblem-photos.png %buildroot%{_datadir}/pixmaps/ephoto.png

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
%{_datadir}/%name
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png
%_datadir/pixmaps/*.png
%{_datadir}/applications/*


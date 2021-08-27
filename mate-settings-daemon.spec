%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Settings Daemon
Name:		mate-settings-daemon
Version:	1.26.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	autoconf-archive
BuildRequires:	intltool
BuildRequires:	ldetect-lst
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libmatekbdui)
BuildRequires:	pkgconfig(libmatemixer)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xxf86misc)

#Requires:      mate-control-center >= %{url_ver}
Requires:      matemixer-backend >= %{url_ver}

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides MATE settings daemon, a daemon to manage the
configuration of the MATE session in the background.

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS
%dir %{_sysconfdir}/mate-settings-daemon
%dir %{_sysconfdir}/mate-settings-daemon/xrandr
%dir %{_sysconfdir}/xrdb
%config(noreplace)%{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop
%{_sysconfdir}/xrdb/*ad
%{_libexecdir}/mate-settings-daemon
%{_libexecdir}/msd-datetime-mechanism
%{_libexecdir}/msd-locate-pointer
%{_udevrulesdir}/61-mate-settings-daemon-rfkill.rules
%{_libdir}/%{name}/libbackground.so
%{_libdir}/%{name}/liba11y-keyboard.so
%{_libdir}/%{name}/liba11y-settings.so
%{_libdir}/%{name}/libclipboard.so
%{_libdir}/%{name}/libhousekeeping.so
%{_libdir}/%{name}/libkeybindings.so
%{_libdir}/%{name}/libkeyboard.so
%{_libdir}/%{name}/libmedia-keys.so
%{_libdir}/%{name}/libmouse.so
%{_libdir}/%{name}/libmpris.so
%{_libdir}/%{name}/librfkill.so
%{_libdir}/%{name}/libsmartcard.so
%{_libdir}/%{name}/libsound.so
%{_libdir}/%{name}/libxrandr.so
%{_libdir}/%{name}/libtyping-break.so
%{_libdir}/%{name}/libxrdb.so
%{_libdir}/%{name}/libxsettings.so
%{_libdir}/%{name}/*.mate-settings-plugin
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/org.mate.SettingsDaemon.service
%{_datadir}/dbus-1/system-services/org.mate.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/dbus-1/system.d/org.mate.SettingsDaemon.DateTimeMechanism.conf
%{_datadir}/glib-2.0/schemas/org.mate.*.xml
%{_datadir}/polkit-1/actions/org.mate.settingsdaemon.datetimemechanism.policy
%{_iconsdir}/hicolor/*/*/*.*
%{_mandir}/man1/mate-settings-daemon.1*
%{_mandir}/man1/msd-datetime-mechanism.1*
%{_mandir}/man1/msd-locate-pointer.1*
%{_datadir}/mate-control-center/keybindings/50-accessibility.xml

#---------------------------------------------------------------------------

%package devel
Summary:	Include files for the MATE settings daemon
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains includes files for the MATE settings daemon.

%files devel
%dir %{_includedir}/mate-settings-daemon
%{_includedir}/mate-settings-daemon/*
%{_libdir}/pkgconfig/mate-settings-daemon.pc

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--disable-schemas-compile \
	--enable-polkit \
	--enable-profiling \
	--enable-pulse \
	%{nil}
%make_build

%install
%make_install

# fix path
install -dm 0755 %{buildroot}/lib/udev/rules.d/
mv %{buildroot}/usr/lib/udev/rules.d/61-mate-settings-daemon-rfkill.rules %{buildroot}%{_udevrulesdir}/

# locales
%find_lang %{name} --with-gnome --all-name

%pre
if [ -d %{_libexecdir}/%{name} ]
  then rm -rf %{_libexecdir}/%{name}
fi

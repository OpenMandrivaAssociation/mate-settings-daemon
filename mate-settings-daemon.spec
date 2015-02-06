%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Settings Daemon
Name:		mate-settings-daemon
Version:	1.8.2
Release:	2
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	ldetect-lst
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libmatekbdui)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xi)

%description
MATE settings daemon manages the configuration of the desktop in the
background.

%package devel
Summary:	Include files for the MATE settings daemon
Group:		Development/Other

%description devel
Include files for the MATE settings daemon

%prep
%setup -q 
%apply_patches
NOCONFIGURE=yes ./autogen.sh

%build
%configure \
	--enable-polkit \
	--enable-profiling \
	--enable-pulse \
	--disable-gstreamer

%make

%install
%makeinstall_std

# remove unneeded converters
rm -fr %{buildroot}%{_datadir}/MateConf

%find_lang %{name} --with-gnome --all-name

%pre
if [ -d %{_libexecdir}/%{name} ]
  then rm -rf %{_libexecdir}/%{name} 
fi

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS
%dir %{_sysconfdir}/mate-settings-daemon
%dir %{_sysconfdir}/mate-settings-daemon/xrandr
%{_sysconfdir}/dbus-1/system.d/org.mate.SettingsDaemon.DateTimeMechanism.conf
%{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop
%{_libexecdir}/mate-settings-daemon
%{_libexecdir}/msd-datetime-mechanism
%{_libexecdir}/msd-locate-pointer
%{_libdir}/%{name}/liba11y-keyboard.so
%{_libdir}/%{name}/libkeybindings.so
%{_libdir}/%{name}/libmpris.so
%{_libdir}/%{name}/libxrandr.so
%{_libdir}/%{name}/libbackground.so
%{_libdir}/%{name}/libkeyboard.so
%{_libdir}/%{name}/libsmartcard.so
%{_libdir}/%{name}/libxrdb.so
%{_libdir}/%{name}/libclipboard.so
%{_libdir}/%{name}/libxsettings.so
%{_libdir}/%{name}/libhousekeeping.so
%{_libdir}/%{name}/libmouse.so
%{_libdir}/%{name}/libtyping-break.so
%{_libdir}/%{name}/libmedia-keys.so
%{_libdir}/%{name}/libsound.so
%{_libdir}/%{name}/*.mate-settings-plugin
%{_datadir}/dbus-1/services/org.mate.SettingsDaemon.service
%{_datadir}/dbus-1/system-services/org.mate.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/%{name}/*
%{_datadir}/glib-2.0/schemas/org.mate.*.xml
%{_datadir}/polkit-1/actions/org.mate.settingsdaemon.datetimemechanism.policy
%{_iconsdir}/mate/*/*/*
%{_mandir}/man1/mate-settings-daemon.1*

%files devel
%{_libdir}/pkgconfig/mate-settings-daemon.pc
%dir %{_includedir}/mate-settings-daemon
%{_includedir}/mate-settings-daemon/*


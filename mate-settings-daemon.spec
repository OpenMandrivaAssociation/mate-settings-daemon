Summary:	MATE Settings Daemon
Name:		mate-settings-daemon
Version:	1.2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	ldetect-lst
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libmatekbdui)
BuildRequires:	pkgconfig(libmatenotify)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(polkit-gobject-1)
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

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--enable-polkit \
	--enable-profiling

%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

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
%{_sysconfdir}/mateconf/schemas/apps_mate_settings_daemon_housekeeping.schemas
%{_sysconfdir}/mateconf/schemas/apps_mate_settings_daemon_keybindings.schemas
%{_sysconfdir}/mateconf/schemas/apps_mate_settings_daemon_xrandr.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_font_rendering.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_keybindings.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_smartcard.schemas
%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_touchpad.schemas
%{_sysconfdir}/mateconf/schemas/mate-settings-daemon.schemas
%{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop
%{_libexecdir}/mate-settings-daemon
%{_libexecdir}/msd-datetime-mechanism
%{_libexecdir}/msd-locate-pointer
%dir %{_libdir}/mate-settings-daemon-1.2.0
%{_libdir}/mate-settings-daemon-1.2.0/a11y-keyboard.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/background.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/clipboard.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/font.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/housekeeping.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/keybindings.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/keyboard.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/liba11y-keyboard.so
%{_libdir}/mate-settings-daemon-1.2.0/libbackground.so
%{_libdir}/mate-settings-daemon-1.2.0/libclipboard.so
%{_libdir}/mate-settings-daemon-1.2.0/libfont.so
%{_libdir}/mate-settings-daemon-1.2.0/libhousekeeping.so
%{_libdir}/mate-settings-daemon-1.2.0/libkeybindings.so
%{_libdir}/mate-settings-daemon-1.2.0/libkeyboard.so
%{_libdir}/mate-settings-daemon-1.2.0/libmedia-keys.so
%{_libdir}/mate-settings-daemon-1.2.0/libmouse.so
%{_libdir}/mate-settings-daemon-1.2.0/libsmartcard.so
%{_libdir}/mate-settings-daemon-1.2.0/libsound.so
%{_libdir}/mate-settings-daemon-1.2.0/libtyping-break.so
%{_libdir}/mate-settings-daemon-1.2.0/libxrandr.so
%{_libdir}/mate-settings-daemon-1.2.0/libxrdb.so
%{_libdir}/mate-settings-daemon-1.2.0/libxsettings.so
%{_libdir}/mate-settings-daemon-1.2.0/media-keys.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/mouse.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/smartcard.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/sound.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/typing-break.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/xrandr.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/xrdb.mate-settings-plugin
%{_libdir}/mate-settings-daemon-1.2.0/xsettings.mate-settings-plugin
%{_datadir}/dbus-1/services/org.mate.SettingsDaemon.service
%{_datadir}/dbus-1/system-services/org.mate.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/mate-control-center/keybindings/50-accessibility.xml
%{_datadir}/mate-settings-daemon/*
%{_datadir}/polkit-1/actions/org.mate.settingsdaemon.datetimemechanism.policy
%{_iconsdir}/mate/*/*/*

%files devel
%{_libdir}/pkgconfig/mate-settings-daemon.pc
%dir %{_includedir}/mate-settings-daemon
%{_includedir}/mate-settings-daemon/*



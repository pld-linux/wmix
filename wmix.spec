Summary:	WMix - Yet another Window Maker Mixer Applet
Summary(pl):	WMix - jeszcze jeden mikser dla WindowMakera
Name:		wmix
Version: 	1.5
Release:	1
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source:		http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/wmixer-%{version}.tar.gz
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildPrereq:	alsa-lib-devel
BuildPrereq:	alsa-driver-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
WMix is a very nice mixer for WindowMaker Dock.
It uses ALSA sound drivers.

%description -l pl
WMix jest bardzo przyjemnym mikserem, zaprojektowanym 
dla Doku WindowMakera i korzystaj±cym ze sterowników ALSA.

%prep
%setup -q -n wm

%build
make -C %{name} \
	FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} 
install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Tue May 25 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [1.5-1]
- initial RPM release.

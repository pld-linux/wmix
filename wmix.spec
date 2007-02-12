Summary:	WMix - Yet another Window Maker Mixer Applet
Summary(pl.UTF-8):   WMix - jeszcze jeden mikser dla WindowMakera
Name:		wmix
Version:	3.2
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.dockapps.org/download.php/id/528/%{name}-%{version}.tar.gz
# Source0-md5:	ce87c48cadf51b3cd6224ef698d3f2cc
Source1:	%{name}.desktop
URL:		http://www.ne.jp/asahi/linux/timecop/#wmix
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
WMix is a very nice mixer for WindowMaker Dock. It uses ALSA or OSS
sound drivers.

%description -l pl.UTF-8
WMix jest bardzo przyjemnym mikserem, zaprojektowanym dla Doku
WindowMakera i korzystającym ze sterowników ALSA lub OSS.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -I%{_includedir}" \
	LDFLAGS="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install wmix $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README sample.wmixrc
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/*

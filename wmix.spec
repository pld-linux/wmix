Summary:	WMix - Yet another Window Maker Mixer Applet
Summary(pl):	WMix - jeszcze jeden mikser dla WindowMakera
Name:		wmix
Version:	3.1
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.ne.jp/asahi/linux/timecop/software/%{name}-%{version}.tar.gz
# Source0-md5:	62f6e86f7558f193e081dc29444a6699
Source1:	%{name}.desktop
URL:		http://www.ne.jp/asahi/linux/timecop/#wmix
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
WMix is a very nice mixer for WindowMaker Dock. It uses ALSA or OSS
sound drivers.

%description -l pl
WMix jest bardzo przyjemnym mikserem, zaprojektowanym dla Doku
WindowMakera i korzystaj±cym ze sterowników ALSA lub OSS.

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

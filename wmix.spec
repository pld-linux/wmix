Summary:	WMix - Yet another Window Maker Mixer Applet
Summary(pl):	WMix - jeszcze jeden mikser dla WindowMakera
Name:		wmix
Version:	1.5
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/%{name}er-%{version}.tar.gz
Source1:	%{name}.desktop
#URL:		http://www.ne.jp/asahi/linux/timecop/#wmix
URL:		http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/mmedia.html#wmmixer
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
WMix is a very nice mixer for WindowMaker Dock. It uses ALSA sound
drivers.

%description -l pl
WMix jest bardzo przyjemnym mikserem, zaprojektowanym dla Doku
WindowMakera i korzystaj±cym ze sterowników ALSA.

%prep
%setup -q -n wm

%build
%{__make} -C %{name} \
	FLAGS="%{rpmcflags} -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/%{name}

#%%{_applnkdir}/DockApplets/wmix.desktop

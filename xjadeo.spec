Summary:	Simple video player that receives sync from jack transport
Name:		xjadeo
Version:	0.7.5
Release:	1
Group:		Video
License:	GPLv2+
Url:		http://xjadeo.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	ffmpeg-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(ltc)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xv)
Suggests:	mencoder
Suggests:	qjadeo

%description
Simple video player that receives sync from jackd or MTC.
It has applications in soundtrack creation, video monitoring or any task that
requires to associate movie frames with audio events.

For instance when a jack-client (like Muse, Rosegarden or Ardour) acts as a
timebase master, xjadeo will display the video synchronized to JACK transport.
xjadeo is capable to read Midi Time Clock as an alternate sync source and comes
along with an optional QT-GUI.

xjadeo reads only seekable media by default. Installing a transcoding utility
like mencoder or transcode is highly recommended.

%files
%{_bindir}/xjadeo
%{_bindir}/xjinfo
%{_bindir}/xjremote
%{_mandir}/man1/xjadeo.1*
%{_mandir}/man1/xjinfo.1*
%{_mandir}/man1/xjremote.1*

#----------------------------------------------------------------------------

%package -n qjadeo
Summary:	Qt-based GUI for xjadeo
Requires:	%{name}

%description -n qjadeo
Qt-based GUI for xjadeo, a simple video player that receives sync
from jack transport.

%files  -n qjadeo -f qjadeo.lang
%{_bindir}/qjadeo
%{_datadir}/applications/qjadeo.desktop
%{_iconsdir}/hicolor/*/apps/qjadeo.png
%{_mandir}/man1/qjadeo.1*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --enable-qtgui
%make

%install
%makeinstall_std

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/qjadeo.desktop << EOF
[Desktop Entry]
Type=Application
Name=Qjadeo
GenericName=X jack video monitor
Comment=A simple video player that gets sync from jack transport
Icon=qjadeo
Exec=/usr/bin/qjadeo
Terminal=false
Categories=AudioVideo;Video;Player;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert doc/%{name}.png -resize ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/qjadeo.png
done

%find_lang qjadeo --with-qt


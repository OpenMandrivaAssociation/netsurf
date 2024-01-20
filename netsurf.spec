Summary:	Compact graphical web browser
Name:		netsurf
Version:	3.11
Release:	1
# There are MIT licensed bits as well as LGPL-licensed talloc, but most
# files are GPLv2 and that is the computed effective license.
License:	GPLv2
Group:		Networking/WWW
URL:		https://www.netsurf-browser.org/
Source0:	https://download.netsurf-browser.org/netsurf/releases/source-full/netsurf-all-%{version}.tar.gz
Patch0:		netsurf-3.11-clang.patch

BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	gperf
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(IO::Compress::Gzip)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libvncserver)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb-atom)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	xxd

%description
NetSurf is a compact graphical web browser which aims for HTML5, CSS and
JavaScript support.

This package ships the version with GTK3 frontend that most users will
want to use.

%files
%{_bindir}/netsurf-gtk3
%{_datadir}/netsurf
%{_datadir}/applications/netsurf-gtk.desktop
%{_datadir}/pixmaps/netsurf.xpm

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n netsurf-all-%{version}

# GTK£ frontend
%global frontend_gtk3  V=1 \\\
	PREFIX=%{_prefix} \\\
	NETSURF_USE_HARU_PDF=NO \\\
	NETSURF_USE_NSLOG=YES \\\
	NETSURF_USE_NSPSL=YES \\\
	NETSURF_USE_NSSVG=YES \\\
	NETSURF_USE_ROSPRITE=NO \\\
	NETSURF_USE_RSVG=YES \\\
	NETSURF_USE_VIDEO=NO \\\
	NETSURF_USE_WEBP=YES \\\
	TARGET=gtk3

%build
# (mandian) workaround for https://github.com/OpenMandrivaAssociation/distribution/issues/2746
%global optflags %{optflags} -O2

%set_build_flags
%make_build %{frontend_gtk3}

%install
%make_install %{frontend_gtk3}

# icon
install -pm 0755 -d %{buildroot}%{_datadir}/pixmaps/
install -pm 0644 netsurf/frontends/gtk/res/netsurf.xpm %{buildroot}%{_datadir}/pixmaps/

# .desktop
install -pm 0755 -d %{buildroot}%{_datadir}/applications/
sed 's/Exec=netsurf-gtk/Exec=netsurf-gtk3/;s/netsurf.png/netsurf/' \
	netsurf/frontends/gtk/res/netsurf-gtk.desktop \
	>%{buildroot}%{_datadir}/applications/netsurf-gtk.desktop


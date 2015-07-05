Summary:	KDE games library
Name:		libkdegames4
Version:	4.14.3
Release:	3
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://games.kde.org/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/libkdegames-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sndfile)

%description
This packages provides common code and data for many KDE games.

#-------------------------------------------------------------------------------

%package common
Summary:	Common files needed by KDE games
Group:		Graphical desktop/KDE
BuildArch:	noarch
Obsoletes:	kdegames4-core < 1:4.9.80

%description common
This package provides common files needed by KDE games such as carddecks
for KDE cardgames.

%files common
%{_kde_appsdir}/carddecks/
%{_kde_appsdir}/kconf_update/kgthemeprovider-migration.upd

#-------------------------------------------------------------------------------

%package corebindings
Summary:	Qml plugins for KDE games
Group:		Graphical desktop/KDE

%description corebindings
Qml plugins for KDE games.

%files corebindings
%{_kde_libdir}/kde4/imports/org/kde/games/core/KgItem.qml
%{_kde_libdir}/kde4/imports/org/kde/games/core/libcorebindingsplugin.so
%{_kde_libdir}/kde4/imports/org/kde/games/core/qmldir

#-------------------------------------------------------------------------------

%define libkdegames_major 6
%define libkdegames %mklibname kdegames %{libkdegames_major}

%package -n %{libkdegames}
Summary:	Runtime Library for KDE games
Group:		System/Libraries
Obsoletes:	%{_lib}kdegames4 < 1:4.8.0
Obsoletes:	%{_lib}kdegames5 < 1:4.9.0
Obsoletes:	%{_lib}kggzgames4 < 1:4.8.0
Obsoletes:	%{_lib}kggzmod4 < 1:4.8.0
Obsoletes:	%{_lib}kggznet4 < 1:4.8.0

%description -n %{libkdegames}
Runtime Library for KDE games.

%files -n %{libkdegames}
%{_kde_libdir}/libkdegames.so.%{libkdegames_major}*

#-------------------------------------------------------------------------------

%define libkdegamesprivate_major 1
%define libkdegamesprivate %mklibname kdegamesprivate 1

%package -n %{libkdegamesprivate}
Summary:	Runtime Library for KDE games
Group:		System/Libraries

%description -n %{libkdegamesprivate}
Runtime Library for KDE games.

%files -n %{libkdegamesprivate}
%{_kde_libdir}/libkdegamesprivate.so.%{libkdegamesprivate_major}*

#-------------------------------------------------------------------------------

%package devel
Summary:	Headers files for KDE games library
Group:		Development/KDE and Qt
Requires:	kdelibs-devel
Obsoletes:	kdegames4-devel < 1:4.9.80
Provides:	kdegames4-devel = %{EVRD}
Requires:	%{libkdegames} = %{EVRD}
Requires:	%{libkdegamesprivate} = %{EVRD}

%description devel
Headers files needed to build applications based on KDE games library.

%files devel
%{_kde_libdir}/cmake/KDEGames/*.cmake
%{_kde_libdir}/libkdegamesprivate.so
%{_kde_libdir}/libkdegames.so
%{_kde_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
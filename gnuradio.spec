%ifarch aarch64
%global _smp_ncpus_max	4
%endif

%define major		3
%define libuhd		%mklibname %{name}-uhd %{major}
%define devuhd		%mklibname %{name}-uhd -d
%define libaudio	%mklibname %{name}-audio %{major}
%define devaudio	%mklibname %{name}-audio -d
%define libruntime	%mklibname %{name}-runtime %{major}
%define devruntime	%mklibname %{name}-runtime -d
%define libvocoder	%mklibname %{name}-vocoder %{major}
%define devvocoder	%mklibname %{name}-vocoder -d
%define libqtgui	%mklibname %{name}-qtgui %{major}
%define devqtgui	%mklibname %{name}-qtgui -d
%define libtrellis	%mklibname %{name}-trellis %{major}
%define devtrellis	%mklibname %{name}-trellis -d
%define libvideo_sdl %mklibname %{name}-video-sdl %{major}
%define devvideo_sdl %mklibname %{name}-video-sdl -d
%define libwavelet	%mklibname %{name}-wavelet %{major}
%define devwavelet	%mklibname %{name}-wavelet -d
%define libfft		%mklibname %{name}-fft %{major}
%define devfft		%mklibname %{name}-fft -d
%define libfilter	%mklibname %{name}-filter %{major}
%define devfilter	%mklibname %{name}-filter -d
%define libanalog	%mklibname %{name}-analog %{major}
%define devanalog	%mklibname %{name}-analog -d
%define libblocks	%mklibname %{name}-blocks %{major}
%define devblocks	%mklibname %{name}-blocks -d
%define libchannels	%mklibname %{name}-channels %{major}
%define devchannels	%mklibname %{name}-channels -d
%define libfec		%mklibname %{name}-fec %{major}
%define devfec		%mklibname %{name}-fec -d
%define libpmt		%mklibname %{name}-pmt %{major}
%define devpmt		%mklibname %{name}-pmt -d
%define libzeromq	%mklibname %{name}-zeromq %{major}
%define devzeromq	%mklibname %{name}-zeromq -d
%define libdtv		%mklibname %{name}-dtv %{major}
%define devdtv		%mklibname %{name}-dtv -d
%define libdigital	%mklibname %{name}-digital %{major}
%define devdigital	%mklibname %{name}-digital -d

# For obsoletes only
%define libatsc		%mklibname %{name}-atsc 0
%define devatsc		%mklibname %{name}-atsc -d
%define libnoaa		%mklibname %{name}-noaa 0
%define devnoaa		%mklibname %{name}-noaa -d
%define libpager	%mklibname %{name}-pager 0
%define devpager	%mklibname %{name}-pager -d
%define libfcd		%mklibname %{name}-fcd 0
%define devfcd		%mklibname %{name}-fcd -d
%define libwxgui	%mklibname %{name}-wxgui 0
%define devwxgui	%mklibname %{name}-wxgui -d

Name:		gnuradio
Version:	3.8.2.0
Release:	%mkrel 7
Summary:	Software defined radio framework
Group:		Communications/Radio
License:	GPLv3+
URL:		http://www.gnuradio.org
Source0:	https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:		gnuradio-3.7.1-mga-cmakelists.patch
Patch1:		gnuradio-3.7.9-ubu-FindGSL.cmake.patch
Patch2:		gnuradio-allow-overriding-GR_PYTHON_DIR-from-cmd-line.patch
Patch3:		gnuradio-bind-placeholders.patch


BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	cppzmq-devel
BuildRequires:	doxygen
BuildRequires:	git
BuildRequires:	qt5-qtbase-devel
BuildRequires:	gmp-devel
BuildRequires:	gmpxx-devel
BuildRequires:	graphviz
BuildRequires:	gsm-devel
BuildRequires:	libatlas-devel
BuildRequires:	libtool
BuildRequires:	mpir-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(codec2) >= 0.5
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(gtk+-3.0)
#BuildRequires:	pkgconfig(guile-2.0)
BuildRequires:	guile-devel
BuildRequires:	pkgconfig(ice)
#BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(log4cpp)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(Qt5Qwt6)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(uhd) >= 3.15
BuildRequires:	pkgconfig(volk) >= 2.4
BuildRequires:	python-cheetah
BuildRequires:	python-click
BuildRequires:	python-click-plugins
#BuildRequires:	python-ice-devel
BuildRequires:	python-gobject
BuildRequires:	python-gi
BuildRequires:	python-gi-cairo
BuildRequires:	python-numpy
BuildRequires:	python-pyzmq
BuildRequires:	python-qt5-core
BuildRequires:	python-qt5-devel
BuildRequires:	python-mako
BuildRequires:	python-six
BuildRequires:	python-sphinx
BuildRequires:	python-yaml
BuildRequires:	swig
#BuildRequires:	texlive
BuildRequires:	xdg-utils
# For tests
BuildRequires:	python-scipy

Requires(pre):	shadow-utils

Recommends:	%{name}-doc = %{version}-%{release}
Requires:	%{name}-companion = %{version}-%{release}
Requires:	%{name}-examples = %{version}-%{release}
Requires:	%{name}-utils = %{version}-%{release}
Requires:	%{libruntime} = %{version}-%{release}
Requires:	%{libqtgui} = %{version}-%{release}
Requires:	%{libtrellis} = %{version}-%{release}
Requires:	%{libvideo_sdl} = %{version}-%{release}
Requires:	%{libuhd} = %{version}-%{release}
Requires:	%{libaudio} = %{version}-%{release}
Requires:	%{libvocoder} = %{version}-%{release}
Requires:	%{libwavelet} = %{version}-%{release}
Requires:	%{libfft} = %{version}-%{release}
Requires:	%{libfilter} = %{version}-%{release}
Requires:	%{libanalog} = %{version}-%{release}
Requires:	%{libblocks} = %{version}-%{release}
Requires:	%{libchannels} = %{version}-%{release}
Requires:	%{libfec} = %{version}-%{release}
Requires:	%{libpmt} = %{version}-%{release}
Requires:	%{libzeromq} = %{version}-%{release}
Requires:	%{libdtv} = %{version}-%{release}
Requires:	%{libdigital} = %{version}-%{release}

Requires:	python-%{name}-runtime = %{version}-%{release}
Requires:	python-%{name}-qtgui = %{version}-%{release}
Requires:	python-%{name}-trellis = %{version}-%{release}
Requires:	python-%{name}-video-sdl = %{version}-%{release}
Requires:	python-%{name}-vocoder = %{version}-%{release}
Requires:	python-%{name}-audio = %{version}-%{release}
Requires:	python-%{name}-uhd = %{version}-%{release}
Requires:	python-%{name}-wavelet = %{version}-%{release}
Requires:	python-%{name}-fft = %{version}-%{release}
Requires:	python-%{name}-filter = %{version}-%{release}
Requires:	python-%{name}-channels = %{version}-%{release}
Requires:	python-%{name}-fec = %{version}-%{release}
Requires:	python-%{name}-pmt = %{version}-%{release}
Requires:	python-%{name}-blocks = %{version}-%{release}
Requires:	python-%{name}-analog = %{version}-%{release}
Requires:	python-%{name}-zeromq = %{version}-%{release}
Requires:	python-%{name}-dtv = %{version}-%{release}
Requires:	python-%{name}-digital = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}

Obsoletes:  %{libatsc} < 3.8.0.0
Obsoletes:  %{devatsc} < 3.8.0.0
Obsoletes:  %{libnoaa} < 3.8.0.0
Obsoletes:  %{devnoaa} < 3.8.0.0
Obsoletes:  %{libpager} < 3.8.0.0
Obsoletes:  %{devpager} < 3.8.0.0
Obsoletes:  %{libfcd} < 3.8.0.0
Obsoletes:  %{devfcd} < 3.8.0.0
Obsoletes:  %{libwxgui} < 3.8.0.0
Obsoletes:  %{devwxgui} < 3.8.0.0
Obsoletes:  python-%{name}-atsc < 3.8.0.0
Obsoletes:  python-%{name}-wxgui < 3.8.0.0
Obsoletes:  python-%{name}-fcd < 3.8.0.0

%description
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual wave forms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.
This is a virtual package that installs the entire GNU Radio software set.

%files

############################
%package doc
Summary:	Software Defined Radio
Group:		Communications/Radio
BuildArch:	noarch

%description doc
This package contains the documentation for the GNU Radio software
defined radio system.

%files doc
%doc %{_docdir}/*
%{_datadir}/applications/%{name}-doc.desktop

############################
%package examples
Summary:	GNU Radio Example Programs
Group:		Communications/Radio

%description examples
This package provides examples of GNU Radio usage using Python.

%files examples
%{_datadir}/%{name}/examples

#######################################################
#######################################################
#
# Lib and devel packages
#
#######################################################
#######################################################

############################
%package -n %{libuhd}
Summary:	uhd
Group:		System/Libraries

%description -n %{libuhd}
This is the GNU Radio UHD package.
It is the interface to the UHD library to connect to and send and receive data
between the Ettus Research, LLC product line.

%files -n %{libuhd}
%{_libdir}/lib%{name}-uhd*.so.%{major}{,.*}

############################
%package -n %{devuhd}
Summary:	Uhd devel files
Group:		Development/Other
Requires:	%{libuhd} = %{version}-%{release}
Requires:	%{devruntime} = %{version}-%{release}
Provides:	%{name}-uhd-devel = %{version}-%{release}

%description -n %{devuhd}
This package contains header files needed by developers.

%files -n %{devuhd}
%{_includedir}/%{name}/uhd/*.h
%{_libdir}/pkgconfig/%{name}-uhd.pc
%{_libdir}/lib%{name}-uhd*.so

############################
%package -n %{libaudio}
Summary:	GNU Radio audio interfaces
Group:		System/Libraries

%description -n %{libaudio}
This package includes all of the supported audio interfaces.

%files -n %{libaudio}
%{_libdir}/lib%{name}-audio*.so.%{major}{,.*}
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio-*.conf

############################
%package -n %{devaudio}
Summary:	GNU Radio audio interfaces - devel files
Group:		Development/Other
Requires:	%{libaudio} = %{version}-%{release}
Requires:	%{devruntime} = %{version}-%{release}
Provides:	%{name}-audio-devel = %{version}-%{release}

%description -n %{devaudio}
This package contains header files needed by developers.

%files -n %{devaudio}
%{_includedir}/%{name}/audio/*.h
%{_libdir}/pkgconfig/%{name}-audio.pc
%{_libdir}/lib%{name}-audio*.so

############################
%package -n %{libruntime}
Summary:	The GNU Radio Runtime Library
Group:		System/Libraries

%description -n %{libruntime}
This package contains the GNU Radio runtime libraries.

%files -n %{libruntime}
%{_libdir}/lib%{name}-runtime*.so.%{major}{,.*}

############################
%package -n %{devruntime}
Summary:	The GNU Radio runtime devel files
Group:		Development/Other
Requires:	%{libruntime} = %{version}-%{release}
Provides:	%{devruntime} = %{version}-%{release}
Provides:	%{name}-runtime-devel = %{version}-%{release}

%description -n %{devruntime}
This package contains header files needed by developers.

%files -n %{devruntime}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_includedir}/%{name}/messages/*.h
%{_includedir}/%{name}/thread/*.h
%{_includedir}/%{name}/swig
%{_libdir}/pkgconfig/%{name}-runtime.pc
%{_libdir}/lib%{name}-runtime*.so

############################

%package -n %{libvocoder}
Summary:	GNU Radio C++ vocoder blocks
Group:		System/Libraries

%description -n %{libvocoder}
This is the gr-vocoder package.
It contains all available vocoders in GNU Radio.

%files -n %{libvocoder}
%{_libdir}/lib%{name}-vocoder*.so.%{major}{,.*}

############################
%package -n %{devvocoder}
Summary:	GNU Radio vocoder devel files
Group:		Development/Other
Requires:	%{libvocoder} = %{version}-%{release}
Provides:	%{name}-vocoder-devel = %{version}-%{release}

%description -n %{devvocoder}
This package contains header files needed by developers.

%files -n %{devvocoder}
%{_includedir}/%{name}/vocoder/*.h
%{_libdir}/pkgconfig/%{name}-vocoder.pc
%{_libdir}/lib%{name}-vocoder*.so

############################
%package -n %{libqtgui}
Summary:	GNU Radio C++ blocks for QT-based GUI applications
Group:		System/Libraries

%description -n %{libqtgui}
This package contains the C++ library for using GNU Radio inside
QT-based GUI applications.

%files -n %{libqtgui}
%{_libdir}/lib%{name}-qtgui*.so.%{major}{,.*}
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-qtgui.conf

############################
%package -n %{devqtgui}
Summary:	GNU Radio C++ blocks for QT-based GUI applications
Group:		Development/Other
Requires:	%{libqtgui} = %{version}-%{release}
Provides:	%{name}-qtgui-devel = %{version}-%{release}

%description -n %{devqtgui}
This package contains the C++ library for using GNU Radio inside
QT-based GUI applications.
This package contains header files needed by developers.

%files -n %{devqtgui}
%{_includedir}/%{name}/qtgui/*.h
%{_includedir}/%{name}/qtgui/CMakeLists.txt
%{_libdir}/pkgconfig/%{name}-qtgui.pc
%{_libdir}/lib%{name}-qtgui*.so

############################
%package -n  %{libtrellis}
Summary:	GNU Radio C++ block implementing trellis-coded modulation
Group:		System/Libraries

%description -n %{libtrellis}
This package provides an implementation of tellis-coded modulation
for GNU Radio.

%files -n %{libtrellis}
%{_libdir}/lib%{name}-trellis*.so.%{major}{,.*}

############################
%package -n %{devtrellis}
Summary:	GNU Radio C++ block implementing trellis-coded modulation
Group:		Development/Other
Requires:	%{libtrellis} = %{version}-%{release}
Provides:	%{name}-trellis-devel = %{version}-%{release}

%description -n %{devtrellis}
This package contains header files needed by developers.

%files -n %{devtrellis}
%{_includedir}/%{name}/trellis/*.h
%{_libdir}/pkgconfig/%{name}-trellis.pc
%{_libdir}/lib%{name}-trellis*.so

############################
%package -n %{libvideo_sdl}
Summary:	GNU Radio C++ block implementing video-sdl-coded modulation
Group:		System/Libraries

%description -n %{libvideo_sdl}
This package provides an interface to the SDL rendering library
for GNU Radio.

%files -n %{libvideo_sdl}
%{_libdir}/lib%{name}-video-sdl*.so.%{major}{,.*}

############################
%package -n %{devvideo_sdl}
Summary:	GNU Radio C++ block implementing video-sdl-coded modulation
Group:		Development/Other
Requires:	%{libvideo_sdl} = %{version}-%{release}
Provides:	%{name}-video-sdl-devel = %{version}-%{release}

%description -n %{devvideo_sdl}
This package provides an interface to the SDL rendering library
for GNU Radio.

This package contains header files needed by developers.

%files -n %{devvideo_sdl}
%{_includedir}/%{name}/video_sdl/*.h
%{_libdir}/pkgconfig/%{name}-video-sdl.pc
%{_libdir}/lib%{name}-video-sdl*.so

############################
%package -n %{libwavelet}
Summary:	GnuRadio Wavelet
Group:		System/Libraries

%description -n %{libwavelet}
GnuRadio Wavelet module.

%files -n %{libwavelet}
%{_libdir}/lib%{name}-wavelet*.so.%{major}{,.*}

############################
%package -n %{devwavelet}
Summary:	GnuRadio Wavelet development files
Group:		System/Libraries
Requires:	%{libwavelet} = %{version}-%{release}
Provides:	%{name}-wavelet-devel = %{version}-%{release}

%description -n %{devwavelet}
This package contains header files needed by developers.

%files -n %{devwavelet}
%{_includedir}/%{name}/wavelet/*.h
%{_libdir}/lib%{name}-wavelet*.so
%{_libdir}/pkgconfig/%{name}-wavelet.pc

############################
%package -n %{libfft}
Summary:	GnuRadio fft
Group:		System/Libraries

%description -n %{libfft}
GnuRadio fft module.

%files -n %{libfft}
%{_libdir}/lib%{name}-fft*.so.%{major}{,.*}

############################
%package -n %{devfft}
Summary:	GnuRadio fft development files
Group:		System/Libraries
Requires:	%{libfft} = %{version}-%{release}
Provides:	%{name}-fft-devel = %{version}-%{release}

%description -n %{devfft}
This package contains header files needed by developers.

%files -n %{devfft}
%{_includedir}/%{name}/fft/*.h
%{_libdir}/lib%{name}-fft*.so
%{_libdir}/pkgconfig/%{name}-fft.pc

############################
%package -n %{libfilter}
Summary:	GnuRadio filters
Group:		System/Libraries

%description -n %{libfilter}
GnuRadio filter module.

%files -n %{libfilter}
%{_libdir}/lib%{name}-filter*.so.%{major}{,.*}

############################
%package -n %{devfilter}
Summary:	GnuRadio filter development files
Group:		System/Libraries
Requires:	%{libfilter} = %{version}-%{release}
Provides:	%{name}-filter-devel = %{version}-%{release}

%description -n %{devfilter}
This package contains header files needed by developers.

%files -n %{devfilter}
%{_includedir}/%{name}/filter/*.h
%{_libdir}/lib%{name}-filter*.so
%{_libdir}/pkgconfig/%{name}-filter.pc

############################
%package -n %{libanalog}
Summary:	GnuRadio analog
Group:		System/Libraries

%description -n %{libanalog}
GnuRadio analog module.

%files -n %{libanalog}
%{_libdir}/lib%{name}-analog*.so.%{major}{,.*}

############################
%package -n %{devanalog}
Summary:	GnuRadio analog development files
Group:		System/Libraries
Requires:	%{libanalog} = %{version}-%{release}
Provides:	%{name}-analog-devel = %{version}-%{release}

%description -n %{devanalog}
This package contains header files needed by developers.

%files -n %{devanalog}
%{_includedir}/%{name}/analog/*.h
%{_libdir}/lib%{name}-analog*.so
%{_libdir}/pkgconfig/%{name}-analog.pc

############################
%package -n %{libblocks}
Summary:	GnuRadio blocks
Group:		System/Libraries

%description -n %{libblocks}
GnuRadio blocks module.

%files -n %{libblocks}
%{_libdir}/lib%{name}-blocks*.so.%{major}{,.*}

############################
%package -n %{devblocks}
Summary:	GnuRadio blocks development files
Group:		System/Libraries
Requires:	%{libblocks} = %{version}-%{release}
Provides:	%{name}-blocks-devel = %{version}-%{release}

%description -n %{devblocks}
This package contains header files needed by developers.

%files -n %{devblocks}
%{_includedir}/%{name}/blocks/*.h
%{_libdir}/lib%{name}-blocks*.so
%{_libdir}/pkgconfig/%{name}-blocks.pc

############################
%package -n %{libchannels}
Summary:	GnuRadio channels
Group:		System/Libraries

%description -n %{libchannels}
GnuRadio channels module.

%files -n %{libchannels}
%{_libdir}/lib%{name}-channels*.so.%{major}{,.*}

############################
%package -n %{devchannels}
Summary:	GnuRadio channels development files
Group:		System/Libraries
Requires:	%{libchannels} = %{version}-%{release}
Provides:	%{name}-channels-devel = %{version}-%{release}

%description -n %{devchannels}
This package contains header files needed by developers.

%files -n %{devchannels}
%{_includedir}/%{name}/channels/*.h
%{_libdir}/lib%{name}-channels*.so
%{_libdir}/pkgconfig/%{name}-channels.pc

############################
%package -n %{libfec}
Summary:	GnuRadio fec
Group:		System/Libraries

%description -n %{libfec}
GnuRadio fec module.

%files -n %{libfec}
%{_libdir}/lib%{name}-fec*.so.%{major}{,.*}
%{_datadir}/%{name}/fec/ldpc/*

############################
%package -n %{devfec}
Summary:	GnuRadio fec development files
Group:		System/Libraries
Requires:	%{libfec} = %{version}-%{release}
Provides:	%{name}-fec-devel = %{version}-%{release}

%description -n %{devfec}
This package contains header files needed by developers.

%files -n %{devfec}
%{_includedir}/%{name}/fec/*.h
%{_libdir}/lib%{name}-fec*.so
%{_libdir}/pkgconfig/%{name}-fec.pc

############################
%package -n %{libpmt}
Summary:	GnuRadio pmt
Group:		System/Libraries

%description -n %{libpmt}
GnuRadio pmt module.

%files -n %{libpmt}
%{_libdir}/lib%{name}-pmt*.so.%{major}{,.*}

############################
%package -n %{devpmt}
Summary:	GnuRadio pmt development files
Group:		System/Libraries
Requires:	%{libpmt} = %{version}-%{release}
Provides:	%{name}-pmt-devel = %{version}-%{release}

%description -n %{devpmt}
This package contains header files needed by developers.

%files -n %{devpmt}
%{_libdir}/lib%{name}-pmt*.so
%{_includedir}/pmt/*.h

############################
%package -n %{libzeromq}
Summary:	GnuRadio zeromq
Group:		System/Libraries

%description -n %{libzeromq}
GnuRadio zeromq module.

%files -n %{libzeromq}
%{_libdir}/lib%{name}-zeromq*.so.%{major}{,.*}

############################
%package -n %{devzeromq}
Summary:	GnuRadio zeromq development files
Group:		System/Libraries
Requires:	%{libzeromq} = %{version}-%{release}
Provides:	%{name}-zeromq-devel = %{version}-%{release}

%description -n %{devzeromq}
This package contains header files needed by developers.

%files -n %{devzeromq}
%{_libdir}/lib%{name}-zeromq*.so
%{_includedir}/%{name}/zeromq/*.h
%{_libdir}/pkgconfig/%{name}-zeromq.pc

############################
%package -n %{libdtv}
Summary:	GnuRadio dtv
Group:		System/Libraries

%description -n %{libdtv}
GnuRadio dtv module.

%files -n %{libdtv}
%{_libdir}/lib%{name}-dtv*.so.%{major}{,.*}

############################
%package -n %{devdtv}
Summary:	GnuRadio dtv development files
Group:		System/Libraries
Requires:	%{libdtv} = %{version}-%{release}
Provides:	%{name}-dtv-devel = %{version}-%{release}

%description -n %{devdtv}
This package contains header files needed by developers.

%files -n %{devdtv}
%{_libdir}/lib%{name}-dtv*.so
%{_includedir}/%{name}/dtv/*.h
%{_libdir}/pkgconfig/%{name}-dtv.pc

############################
%package -n %{libdigital}
Summary:	GnuRadio digital
Group:		System/Libraries

%description -n %{libdigital}
GnuRadio digital module.

%files -n %{libdigital}
%{_libdir}/lib%{name}-digital*.so.%{major}{,.*}

############################
%package -n %{devdigital}
Summary:	GnuRadio digital development files
Group:		System/Libraries
Requires:	%{libdigital} = %{version}-%{release}
Provides:	%{name}-digital-devel = %{version}-%{release}

%description -n %{devdigital}
This package contains header files needed by developers.

%files -n %{devdigital}
%{_libdir}/lib%{name}-digital*.so
%{_includedir}/%{name}/digital/*.h
%{_libdir}/pkgconfig/%{name}-digital.pc

#######################################################
#######################################################
#
# Python packages
#
#######################################################
#######################################################

############################
%package -n python-%{name}-runtime
Summary:	Python bindings for GNU Radio runtime library
Group:		Development/Python
Requires:	python3-mako
Requires:	python3-numpy
Requires:	python3-cheetah
Requires:	python3-scipy
Requires:	python3-opengl
Requires:	python3-pyzmq
Requires:	python3-six

%description -n python-%{name}-runtime
This package provides the modules that enable one to use gnuradio from
Python scripts.

%files -n python-%{name}-runtime
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/%{name}-runtime.conf
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/gr
%{python3_sitelib}/%{name}/gru
%{python3_sitelib}/%{name}/__init__.*
%{python3_sitelib}/%{name}/eng_notation.*
%{python3_sitelib}/%{name}/eng_option.*
%{python3_sitelib}/%{name}/gr_unittest.*

############################
%package -n python-%{name}-vocoder
Summary:	Python bindings for GNU Radio vocoder
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-vocoder
This package contains Python bindings for GNU Radio ATSC decoding.

%files -n python-%{name}-vocoder
%{python3_sitelib}/%{name}/vocoder/*

############################
%package -n python-%{name}-audio
Summary:	GNU Radio Python Audio Driver
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-audio
This package provides the Python interface to the GNU Radio driver for the
audio system.

%files -n python-%{name}-audio
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio.conf
%{python3_sitelib}/%{name}/audio/*

############################
%package -n python-%{name}-qtgui
Summary:	GNU Radio Graphical Interface Routines based on QT
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-qtgui
This package provides the Python wrappers around the GNU Radio QT GUI
C++ blocks.

%files -n python-%{name}-qtgui
%{python3_sitelib}/%{name}/qtgui

############################
%package -n python-%{name}-trellis
Summary:	GNU Radio Trellis-Coded Modulation library
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-trellis
This package provides an implementation of trellis-coded modulation for
GNU Radio.

%files -n python-%{name}-trellis
%{python3_sitelib}/%{name}/trellis/*

############################
%package -n python-%{name}-uhd
Summary:	Python bindings for GNU Radio uhd driver
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-uhd
This package provides the Python interface to the GNU Radio uhd driver
and daughterboard drivers.

%files -n python-%{name}-uhd
%{python3_sitelib}/%{name}/uhd

############################
%package -n python-%{name}-video-sdl
Summary:	GNU Radio SDL Interface Library
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-video-sdl
This package provides an interface to the SDL rendering library for GNU Radio.

%files -n python-%{name}-video-sdl
%{python3_sitelib}/%{name}/video_sdl/*

############################
%package -n python-%{name}-channels
Summary:	GNU Radio channels
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-channels
GNU Radio channels

%files -n python-%{name}-channels
%{python3_sitelib}/%{name}/channels

############################
%package -n python-%{name}-fec
Summary:	GNU Radio fec
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-fec
GNU Radio fec

%files -n python-%{name}-fec
%{python3_sitelib}/%{name}/fec

############################
%package -n python-%{name}-pmt
Summary:	GNU Radio pmt
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}
Requires:	python3-numpy
Requires:	python3-opengl

%description -n python-%{name}-pmt
GNU Radio pmt

%files -n python-%{name}-pmt
%{python3_sitelib}/pmt/*

############################
%package -n python-%{name}-wavelet
Summary:	GNU Radio wavelet
Group:		Development/Python

%description -n python-%{name}-wavelet
GNU Radio wavelet

%files -n python-%{name}-wavelet
%{python3_sitelib}/%{name}/wavelet

############################
%package -n python-%{name}-fft
Summary:	GNU Radio fft
Group:		Development/Python

%description -n python-%{name}-fft
GNU Radio fft

%files -n python-%{name}-fft
%{python3_sitelib}/%{name}/fft
%{python3_sitelib}/%{name}/plot_fft_base.*

############################
%package -n python-%{name}-filter
Summary:	GNU Radio filter
Group:		Development/Python
Requires:	python3-pyqtgraph

%description -n python-%{name}-filter
GNU Radio filter

%files -n python-%{name}-filter
%{python3_sitelib}/%{name}/filter
%{python3_sitelib}/%{name}/pyqt_filter.*

############################
%package -n python-%{name}-analog
Summary:	GNU Radio analog
Group:		Development/Python

%description -n python-%{name}-analog
GNU Radio analog

%files -n python-%{name}-analog
%{python3_sitelib}/%{name}/analog

############################
%package -n python-%{name}-blocks
Summary:	GNU Radio blocks
Group:		Development/Python

%description -n python-%{name}-blocks
GNU Radio blocks

%files -n python-%{name}-blocks
%{python3_sitelib}/%{name}/blocks

############################
%package -n python-%{name}-modtool
Summary:	GNU Radio modtool
Group:		Development/Python

%description -n python-%{name}-modtool
GNU Radio modtool

%files -n python-%{name}-modtool
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/modtool.conf
%{python3_sitelib}/%{name}/modtool
%{_datadir}/%{name}/modtool/templates

############################
%package -n python-%{name}-ctrlport
Summary:	GNU Radio ctrlport
Group:		Development/Python

%description -n python-%{name}-ctrlport
GNU Radio ctrlport

%files -n python-%{name}-ctrlport
%{python3_sitelib}/%{name}/ctrlport

############################
%package -n python-%{name}-zeromq
Summary:	GNU Radio zeromq
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}
Requires:	python3-numpy
Requires:	python3-opengl

%description -n python-%{name}-zeromq
GNU Radio zeromq

%files -n python-%{name}-zeromq
%{python3_sitelib}/%{name}/zeromq

############################
%package -n python-%{name}-dtv
Summary:	GNU Radio dtv
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}
Requires:	python3-numpy
Requires:	python3-opengl

%description -n python-%{name}-dtv
GNU Radio dtv

%files -n python-%{name}-dtv
%{python3_sitelib}/%{name}/dtv

###########################
%package -n python-%{name}-digital
Summary:	GNU Radio digital
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}
Requires:	python3-numpy
Requires:	python3-opengl

%description -n python-%{name}-digital
GNU Radio digital

%files -n python-%{name}-digital
%{python3_sitelib}/%{name}/digital

#######################################################
#######################################################
#
# Software packages and others
#
#######################################################
#######################################################

%package companion
Summary:	The GNU Radio Companion
Group:		Communications/Radio
Requires:	python-%{name}-runtime = %{version}-%{release}
Requires:	python-gnuradio-pmt = %{version}-%{release}
Recommends:	%{name}-examples = %{version}-%{release}
Requires:	python3-cheetah

%description companion
GRC is a graphical flowgraph editor for the GNU Software Radio.

%files companion
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/grc.conf
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/00-grc-docs.conf
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr_log_default.conf
%{_bindir}/%{name}-companion
%{_datadir}/applications/%{name}-grc.desktop
%{_datadir}/mime/packages/*
%{_datadir}/%{name}/grc
%{_datadir}/%{name}/themes/*.qss
%{_iconsdir}/hicolor/*
%{_iconsdir}/gnome/*
%{python3_sitelib}/%{name}/grc

############################
%package utils
Summary:	GNU Radio Utilities
Group:		Communications/Radio
Requires:	python-matplotlib
Requires:	python-scipy

%description utils
This package provides commonly used utilities for GNU Radio.

%files utils
%{python3_sitelib}/%{name}/__pycache__/*
%{python3_sitelib}/%{name}/plot_psd_base.*
%{python3_sitelib}/%{name}/plot_data.*
%{python3_sitelib}/%{name}/pyqt_plot.*
%{python3_sitelib}/%{name}/eng_arg.*
%{_bindir}/%{name}-config-info
%{_bindir}/gr_filter_design
%{_bindir}/gr_plot
%{_bindir}/uhd_*
%{_bindir}/gr_read_file_metadata
%{_bindir}/grcc
%{_bindir}/gr_modtool
%{_bindir}/gr_plot_const
%{_bindir}/gr_plot_fft
%{_bindir}/gr_plot_iq
%{_bindir}/gr_plot_psd
%{_bindir}/gr_plot_qt
%{_bindir}/gr-ctrlport-monitor
%{_bindir}/gr-perf-monitorx
%{_bindir}/polar_channel_construction
%{_libdir}/cmake/%{name}

#######################################################
#######################################################
%prep
%autosetup -p1

%build
export LDFLAGS="%{ldflags} -L%{_libdir}/atlas"
%global _cmake_module_linker_flags_extra -L%{_libdir}/atlas
%cmake -DENABLE_INTERNAL_VOLK=OFF \
       -DGR_PYTHON_DIR=%{python_sitelib}
       
%make_build

%check
# Some tests fail only in i586 build.
# qa_qtgui test fail is expected in headless BS.
# Test failures do not halt builds, so check the log.
# Skip tests on ARM
%ifnarch %arm
cd %{_vpath_builddir}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
# https://github.com/gnuradio/gnuradio/issues/989
	%ifarch i586
		ctest -V -E '(qa_fecapi_ldpc|qa_qtgui)' ||:
	%else
		ctest -V -E qa_qtgui ||:
	%endif
%endif

%install
%make_install -C build

############################
# Desktop files

cat > %{name}-doc.desktop << EOF
[Desktop Entry]
Version=1.0
Name=Gnu Radio C++ API Documentation
GenericName=Gnu Radio C++ API Documentation
Exec=xdg-open /usr/share/doc/%{name}-%{version}/html/index.html
Icon=%{name}-grc
Terminal=false
Type=Application
Categories=System;Documentation;X-Mageia-CrossDesktop;
X-Desktop-File-Install-Version=0.19
EOF

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{name}-doc.desktop

desktop-file-install \
--add-category='X-Mageia-CrossDesktop' \
--set-key=Name \
--set-value='Gnu Radio Companion' \
--dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/%{name}/grc/freedesktop/%{name}-grc.desktop

############################
# We don't need these:
find %{buildroot} -name "*.la" -delete
rm -f %{buildroot}%{_libexecdir}/%{name}/grc_setup_freedesktop

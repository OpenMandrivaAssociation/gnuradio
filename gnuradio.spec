%ifarch %{aarch64}
%global _smp_ncpus_max	4
%endif

%define major		3
%define libuhd		%mklibname %{name}-uhd
%define devuhd		%mklibname %{name}-uhd -d
%define libaudio	%mklibname %{name}-audio
%define devaudio	%mklibname %{name}-audio -d
%define libruntime	%mklibname %{name}-runtime
%define devruntime	%mklibname %{name}-runtime -d
%define libvocoder	%mklibname %{name}-vocoder
%define devvocoder	%mklibname %{name}-vocoder -d
%define libqtgui	%mklibname %{name}-qtgui
%define devqtgui	%mklibname %{name}-qtgui -d
%define libtrellis	%mklibname %{name}-trellis
%define devtrellis	%mklibname %{name}-trellis -d
%define libvideo_sdl %mklibname %{name}-video-sdl
%define devvideo_sdl %mklibname %{name}-video-sdl -d
%define libwavelet	%mklibname %{name}-wavelet
%define devwavelet	%mklibname %{name}-wavelet -d
%define libfft		%mklibname %{name}-fft
%define devfft		%mklibname %{name}-fft -d
%define libfilter	%mklibname %{name}-filter
%define devfilter	%mklibname %{name}-filter -d
%define libanalog	%mklibname %{name}-analog
%define devanalog	%mklibname %{name}-analog -d
%define libblocks	%mklibname %{name}-blocks
%define devblocks	%mklibname %{name}-blocks -d
%define libchannels	%mklibname %{name}-channels
%define devchannels	%mklibname %{name}-channels -d
%define libfec		%mklibname %{name}-fec
%define devfec		%mklibname %{name}-fec -d
%define libpmt		%mklibname %{name}-pmt
%define devpmt		%mklibname %{name}-pmt -d
%define libzeromq	%mklibname %{name}-zeromq
%define devzeromq	%mklibname %{name}-zeromq -d
%define libdtv		%mklibname %{name}-dtv
%define devdtv		%mklibname %{name}-dtv -d
%define libdigital	%mklibname %{name}-digital
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
Version:	3.10.7.0
Release:	1
Summary:	Software defined radio framework
Group:		Communications/Radio
License:	GPLv3+
URL:		https://www.gnuradio.org
Source0:	https://github.com/gnuradio/gnuradio/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
#Patch1:		gnuradio-3.7.9-ubu-FindGSL.cmake.patch
#Patch2:		gnuradio-allow-overriding-GR_PYTHON_DIR-from-cmd-line.patch
#Patch3:		gnuradio-bind-placeholders.patch


BuildRequires:	boost-devel
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	ninja
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
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(Qt5Qwt6)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(uhd) >= 3.15
BuildRequires:	pkgconfig(volk) >= 2.4
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(libiio)
BuildRequires:	pkgconfig(spdlog)
BuildRequires:	python%{pyver}dist(pybind11)
BuildRequires:	cmake(pybind11)
BuildRequires:	cmake(SoapySDR)
BuildRequires:	python-cheetah
BuildRequires:	python-click
BuildRequires:	python-click-plugins
#BuildRequires:	python-ice-devel
#BuildRequires:	python-gobject
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
BuildRequires:	texlive
BuildRequires:	texlive-unicode-data
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
%{_datadir}/metainfo/org.gnuradio.grc.metainfo.xml
%{_mandir}/man1/dial_tone.1*
%{_mandir}/man1/display_qt.1*
%{_mandir}/man1/gnuradio-companion.1*
%{_mandir}/man1/gnuradio-config-info.1*
%{_mandir}/man1/gr-ctrlport-monitor.1*
%{_mandir}/man1/gr-perf-monitorx.1*
%{_mandir}/man1/gr_filter_design.1*
%{_mandir}/man1/gr_modtool.1*
%{_mandir}/man1/gr_plot_const.1*
%{_mandir}/man1/gr_plot_fft.1*
%{_mandir}/man1/gr_plot_iq.1*
%{_mandir}/man1/gr_plot_psd.1*
%{_mandir}/man1/gr_plot_qt.1*
%{_mandir}/man1/gr_plot_time.1*
%{_mandir}/man1/gr_read_file_metadata.1*
%{_mandir}/man1/grcc.1*
%{_mandir}/man1/polar_channel_construction.1*
%{_mandir}/man1/tags_demo.1*
%{_mandir}/man1/uhd_fft.1*
%{_mandir}/man1/uhd_rx_cfile.1*
%{_mandir}/man1/uhd_rx_nogui.1*
%{_mandir}/man1/uhd_siggen.1*
%{_mandir}/man1/uhd_siggen_gui.1*

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
%{_includedir}/%{name}/uhd
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
%{_includedir}/%{name}/audio
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
%{_libdir}/lib%{name}-iio*.so.%{major}{,.*}
%{_libdir}/lib%{name}-network*.so.%{major}{,.*}
%{_libdir}/lib%{name}-pdu*.so.%{major}{,.*}
%{_libdir}/lib%{name}-soapy*.so.%{major}{,.*}

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
%{_includedir}/%{name}/messages
%{_includedir}/%{name}/thread
%{_includedir}/%{name}/iio
%{_includedir}/%{name}/network
%{_includedir}/%{name}/pdu
%{_includedir}/%{name}/soapy
%{_libdir}/pkgconfig/%{name}-runtime.pc
%{_libdir}/pkgconfig/%{name}-iio.pc
%{_libdir}/pkgconfig/%{name}-network.pc
%{_libdir}/pkgconfig/%{name}-pdu.pc
%{_libdir}/pkgconfig/%{name}-soapy.pc
%{_libdir}/lib%{name}-runtime*.so
%{_libdir}/lib%{name}-iio*.so
%{_libdir}/lib%{name}-network*.so
%{_libdir}/lib%{name}-pdu*.so
%{_libdir}/lib%{name}-soapy*.so
%{_datadir}/gnuradio/clang-format.conf

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
%{_includedir}/%{name}/vocoder
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
%{_includedir}/%{name}/qtgui
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
%{_includedir}/%{name}/trellis
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
%{_includedir}/%{name}/video_sdl
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
%{_includedir}/%{name}/wavelet
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
%{_includedir}/%{name}/fft
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
%{_includedir}/%{name}/filter
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
%{_includedir}/%{name}/analog
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
%{_includedir}/%{name}/blocks
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
%{_includedir}/%{name}/channels
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
%{_includedir}/%{name}/fec
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
%{_includedir}/pmt

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
%{_includedir}/%{name}/zeromq
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
%{_includedir}/%{name}/dtv
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
%{_includedir}/%{name}/digital
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
Requires:	python-mako
Requires:	python-numpy
Requires:	python-cheetah
Requires:	python-scipy
Requires:	python-opengl
Requires:	python-pyzmq
Requires:	python-six

%description -n python-%{name}-runtime
This package provides the modules that enable one to use gnuradio from
Python scripts.

%files -n python-%{name}-runtime
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/%{name}-runtime.conf
%dir %{python_sitelib}/%{name}
%{python_sitelib}/%{name}/bindtool
%{python_sitelib}/%{name}/blocktool
%{python_sitelib}/%{name}/gr
%{python_sitelib}/%{name}/__init__.*
%{python_sitelib}/%{name}/eng_notation.*
%{python_sitelib}/%{name}/eng_option.*
%{python_sitelib}/%{name}/gr_unittest.*
%{python_sitelib}/%{name}/iio
%{python_sitelib}/%{name}/network
%{python_sitelib}/%{name}/pdu
%{python_sitelib}/%{name}/soapy

############################
%package -n python-%{name}-vocoder
Summary:	Python bindings for GNU Radio vocoder
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-vocoder
This package contains Python bindings for GNU Radio ATSC decoding.

%files -n python-%{name}-vocoder
%{python_sitelib}/%{name}/vocoder/*

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
%{python_sitelib}/%{name}/audio/*

############################
%package -n python-%{name}-qtgui
Summary:	GNU Radio Graphical Interface Routines based on QT
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-qtgui
This package provides the Python wrappers around the GNU Radio QT GUI
C++ blocks.

%files -n python-%{name}-qtgui
%{python_sitelib}/%{name}/qtgui

############################
%package -n python-%{name}-trellis
Summary:	GNU Radio Trellis-Coded Modulation library
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-trellis
This package provides an implementation of trellis-coded modulation for
GNU Radio.

%files -n python-%{name}-trellis
%{python_sitelib}/%{name}/trellis/*

############################
%package -n python-%{name}-uhd
Summary:	Python bindings for GNU Radio uhd driver
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-uhd
This package provides the Python interface to the GNU Radio uhd driver
and daughterboard drivers.

%files -n python-%{name}-uhd
%{python_sitelib}/%{name}/uhd

############################
%package -n python-%{name}-video-sdl
Summary:	GNU Radio SDL Interface Library
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-video-sdl
This package provides an interface to the SDL rendering library for GNU Radio.

%files -n python-%{name}-video-sdl
%{python_sitelib}/%{name}/video_sdl/*

############################
%package -n python-%{name}-channels
Summary:	GNU Radio channels
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-channels
GNU Radio channels

%files -n python-%{name}-channels
%{python_sitelib}/%{name}/channels

############################
%package -n python-%{name}-fec
Summary:	GNU Radio fec
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}

%description -n python-%{name}-fec
GNU Radio fec

%files -n python-%{name}-fec
%{python_sitelib}/%{name}/fec

############################
%package -n python-%{name}-pmt
Summary:	GNU Radio pmt
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}
Requires:	python-numpy
Requires:	python-opengl

%description -n python-%{name}-pmt
GNU Radio pmt

%files -n python-%{name}-pmt
%{python_sitelib}/pmt/*

############################
%package -n python-%{name}-wavelet
Summary:	GNU Radio wavelet
Group:		Development/Python

%description -n python-%{name}-wavelet
GNU Radio wavelet

%files -n python-%{name}-wavelet
%{python_sitelib}/%{name}/wavelet

############################
%package -n python-%{name}-fft
Summary:	GNU Radio fft
Group:		Development/Python

%description -n python-%{name}-fft
GNU Radio fft

%files -n python-%{name}-fft
%{python_sitelib}/%{name}/fft
%{python_sitelib}/%{name}/plot_fft_base.*

############################
%package -n python-%{name}-filter
Summary:	GNU Radio filter
Group:		Development/Python
Requires:	python-pyqtgraph

%description -n python-%{name}-filter
GNU Radio filter

%files -n python-%{name}-filter
%{python_sitelib}/%{name}/filter
%{python_sitelib}/%{name}/pyqt_filter.*

############################
%package -n python-%{name}-analog
Summary:	GNU Radio analog
Group:		Development/Python

%description -n python-%{name}-analog
GNU Radio analog

%files -n python-%{name}-analog
%{python_sitelib}/%{name}/analog

############################
%package -n python-%{name}-blocks
Summary:	GNU Radio blocks
Group:		Development/Python

%description -n python-%{name}-blocks
GNU Radio blocks

%files -n python-%{name}-blocks
%{python_sitelib}/%{name}/blocks

############################
%package -n python-%{name}-modtool
Summary:	GNU Radio modtool
Group:		Development/Python

%description -n python-%{name}-modtool
GNU Radio modtool

%files -n python-%{name}-modtool
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/modtool.conf
%{python_sitelib}/%{name}/modtool
%{_datadir}/%{name}/modtool/templates

############################
%package -n python-%{name}-ctrlport
Summary:	GNU Radio ctrlport
Group:		Development/Python

%description -n python-%{name}-ctrlport
GNU Radio ctrlport

%files -n python-%{name}-ctrlport
%{python_sitelib}/%{name}/ctrlport

############################
%package -n python-%{name}-zeromq
Summary:	GNU Radio zeromq
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}
Requires:	python-numpy
Requires:	python-opengl

%description -n python-%{name}-zeromq
GNU Radio zeromq

%files -n python-%{name}-zeromq
%{python_sitelib}/%{name}/zeromq

############################
%package -n python-%{name}-dtv
Summary:	GNU Radio dtv
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}
Requires:	python-numpy
Requires:	python-opengl

%description -n python-%{name}-dtv
GNU Radio dtv

%files -n python-%{name}-dtv
%{python_sitelib}/%{name}/dtv

###########################
%package -n python-%{name}-digital
Summary:	GNU Radio digital
Group:		Development/Python
Requires:	python-%{name}-runtime = %{version}-%{release}
Requires:	python-numpy
Requires:	python-opengl

%description -n python-%{name}-digital
GNU Radio digital

%files -n python-%{name}-digital
%{python_sitelib}/%{name}/digital

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
Requires:	python-cheetah

%description companion
GRC is a graphical flowgraph editor for the GNU Software Radio.

%files companion
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/grc.conf
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/00-grc-docs.conf
%{_bindir}/%{name}-companion
%{_datadir}/applications/%{name}-grc.desktop
%{_datadir}/%{name}/grc
%{_datadir}/%{name}/themes/*.qss
%{python_sitelib}/%{name}/grc

############################
%package utils
Summary:	GNU Radio Utilities
Group:		Communications/Radio
Requires:	python-matplotlib
Requires:	python-scipy

%description utils
This package provides commonly used utilities for GNU Radio.

%files utils
%{python_sitelib}/%{name}/plot_psd_base.*
%{python_sitelib}/%{name}/plot_data.*
%{python_sitelib}/%{name}/pyqt_plot.*
%{python_sitelib}/%{name}/eng_arg.*
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
%cmake \
	-DENABLE_INTERNAL_VOLK:BOOL=OFF \
	-DENABLE_EXAMPLES:BOOL=ON \
	-DENABLE_GNURADIO_RUNTIME:BOOL=ON \
	-DENABLE_GNURADIO_FFT:BOOL=ON \
	-DENABLE_GR_BLOCKS:BOOL=ON \
	-DENABLE_GR_QTGUI:BOOL=ON \
	-DENABLE_GR_NETWORK:BOOL=ON \
	-DGR_PYTHON_DIR=%{python_sitelib} \
	-G Ninja
%ninja_build

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
%ninja_install -C build

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
--set-key=Name \
--set-value='Gnu Radio Companion' \
--dir=%{buildroot}%{_datadir}/applications ./grc/scripts/freedesktop/%{name}-grc.desktop

############################
# metainfo
install -dm 0755 %{buildroot}%{_datadir}/metainfo/
install -pm 0644 grc/scripts/freedesktop/org.gnuradio.grc.metainfo.xml %{buildroot}%{_datadir}/metainfo/

############################
# We don't need these:
find %{buildroot} -name "*.la" -delete
#rm -f %{buildroot}%{_libexecdir}/%{name}/grc_setup_freedesktop


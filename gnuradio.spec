%define major		0
%define libuhd		%mklibname %{name}-uhd %{major}
%define devuhd		%mklibname %{name}-uhd -d
%define libdigital	%mklibname %{name}-digital %{major}
%define devdigital	%mklibname %{name}-digital -d
%define libvolk		%mklibname %{name}-volk %{major}
%define devvolk		%mklibname %{name}-volk -d
%define libatsc		%mklibname %{name}-atsc %{major}
%define devatsc		%mklibname %{name}-atsc -d
%define libaudio	%mklibname %{name}-audio %{major}
%define devaudio	%mklibname %{name}-audio -d
%define libruntime	%mklibname %{name}-runtime %{major}
%define devruntime	%mklibname %{name}-runtime -d
%define libvocoder	%mklibname %{name}-vocoder %{major}
%define devvocoder	%mklibname %{name}-vocoder -d
%define libnoaa		%mklibname %{name}-noaa %{major}
%define devnoaa		%mklibname %{name}-noaa -d
%define libpager	%mklibname %{name}-pager %{major}
%define devpager	%mklibname %{name}-pager -d
%define libqtgui	%mklibname %{name}-qtgui %{major}
%define devqtgui	%mklibname %{name}-qtgui -d
%define libtrellis	%mklibname %{name}-trellis %{major}
%define devtrellis	%mklibname %{name}-trellis -d
%define libvideo_sdl	%mklibname %{name}-video-sdl %{major}
%define devvideo_sdl	%mklibname %{name}-video-sdl -d
%define libfcd		%mklibname %{name}-fcd %{major}
%define devfcd		%mklibname %{name}-fcd -d
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
%define libwxgui	%mklibname %{name}-wxgui %{major}
%define devwxgui	%mklibname %{name}-wxgui -d
%define libchannels	%mklibname %{name}-channels %{major}
%define devchannels	%mklibname %{name}-channels -d
%define libfec		%mklibname %{name}-fec %{major}
%define devfec		%mklibname %{name}-fec -d
%define libpmt		%mklibname %{name}-pmt %{major}
%define devpmt		%mklibname %{name}-pmt -d

# The following retained only for obsoletes
%define libcore		%mklibname %{name}-core %{major}
%define devcore		%mklibname %{name}-core -d
%define libgruel	%mklibname gruel %{major}
%define devgruel	%mklibname gruel -d

%bcond_with ice

#######################################################
Name:		gnuradio
Version:	3.7.3
Release:	2
Summary:	Software defined radio framework
Group:		Communications
License:	GPLv3+
URL:		http://www.gnuradio.org
Source0:	http://gnuradio.org/releases/gnuradio/%{name}-%{version}.tar.gz

# Create tarball from git with:
# $ ./make-tarball gnuradio http://gnuradio.org/git/gnuradio.git
# See note in make-tarball script
Source1:	make-tarball

Patch0:		gnuradio-3.7.1-mga-cmakelists.patch

BuildRequires:	cmake
BuildRequires:	sdcc
BuildRequires:	fftw-devel
BuildRequires:	cppunit-devel
BuildRequires:	wxPython
BuildRequires:	xmlto
BuildRequires:	graphviz
BuildRequires:	boost-devel
BuildRequires:	python-devel
BuildRequires:	swig
BuildRequires:	doxygen
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(guile-2.0)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	portaudio-devel
BuildRequires:	libtool
BuildRequires:	gsl-devel
BuildRequires:	python-qt4-devel
BuildRequires:	libqwtplot3d-devel
BuildRequires:	python-cheetah
BuildRequires:	xdg-utils
BuildRequires:	python-lxml
BuildRequires:	pygtk2.0-libglade
BuildRequires:	orc-devel
BuildRequires:	uhd-devel
BuildRequires:	python-numpy
BuildRequires:	qwt-devel
%if %{with ice}
BuildRequires:	python-ice-devel
BuildRequires:	ice-devel
%endif

Requires(pre):	shadow-utils

Requires:	%{name}-companion = %{EVRD}
Requires:	%{name}-doc = %{EVRD}
Requires:	%{name}-examples = %{EVRD}
Requires:	%{name}-noaa = %{EVRD}
Requires:	%{name}-pager = %{EVRD}
Requires:	%{name}-utils = %{EVRD}
Requires:	%{libatsc} = %{EVRD}
Requires:	%{libruntime} = %{EVRD}
Requires:	%{libnoaa} = %{EVRD}
Requires:	%{libpager} = %{EVRD}
Requires:	%{libqtgui} = %{EVRD}
Requires:	%{libtrellis} = %{EVRD}
Requires:	%{libvideo_sdl} = %{EVRD}
Requires:	%{libuhd} = %{EVRD}
Requires:	%{libdigital} = %{EVRD}
Requires:	%{libvolk} = %{EVRD}
Requires:	%{libaudio} = %{EVRD}
Requires:	%{libvocoder} = %{EVRD}
Requires:	%{libfcd} = %{EVRD}
Requires:	%{libwavelet} = %{EVRD}
Requires:	%{libfft} = %{EVRD}
Requires:	%{libfilter} = %{EVRD}
Requires:	%{libanalog} = %{EVRD}
Requires:	%{libblocks} = %{EVRD}
Requires:	%{libwxgui} = %{EVRD}
Requires:	%{libchannels} = %{EVRD}
Requires:	%{libfec} = %{EVRD}
Requires:	%{libpmt} = %{EVRD}

Requires:	python-%{name}-atsc = %{EVRD}
Requires:	python-%{name}-runtime = %{EVRD}
Requires:	python-%{name}-qtgui = %{EVRD}
Requires:	python-%{name}-trellis = %{EVRD}
Requires:	python-%{name}-video-sdl = %{EVRD}
Requires:	python-%{name}-wxgui = %{EVRD}
Requires:	python-%{name}-digital = %{EVRD}
Requires:	python-%{name}-vocoder = %{EVRD}
Requires:	python-%{name}-audio = %{EVRD}
Requires:	python-%{name}-uhd = %{EVRD}
Requires:	python-%{name}-fcd = %{EVRD}
Requires:	python-%{name}-wavelet = %{EVRD}
Requires:	python-%{name}-fft = %{EVRD}
Requires:	python-%{name}-filter = %{EVRD}
Requires:	python-%{name}-modtool = %{EVRD}
Requires:	python-%{name}-channels = %{EVRD}
Requires:	python-%{name}-fec = %{EVRD}
Requires:	python-%{name}-pmt = %{EVRD}
Requires:	python-%{name}-blocks = %{EVRD}
Requires:	python-%{name}-analog = %{EVRD}

Provides:	%{name} = %{EVRD}

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
Group:		Communications
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
Group:		Communications

%description examples
This package provides examples of GNU Radio usage using Python.

%files examples
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/grc

#######################################################
#######################################################
#
# Lib and devel packages
#
#######################################################
#######################################################

############################
%package -n %{libuhd}
Summary:	Uhd
Group:		System/Libraries
Obsoletes:	%{_lib}%{name}-usrp0 < 3.5.1
Obsoletes:	%{_lib}%{name}-usrp2_0 < 3.5.1
Obsoletes:	usrp < 3.5.1

%description -n %{libuhd}
This is the GNU Radio UHD package.
It is the interface to the UHD library to connect to and send and receive data
between the Ettus Research, LLC product line.

%files -n %{libuhd}
%{_libdir}/lib%{name}-uhd*.so.%{major}*

############################
%package -n %{devuhd}
Summary:	Uhd devel files
Group:		Development/Other
Requires:	%{libuhd} = %{EVRD}
Obsoletes:	%{_lib}%{name}-usrp2-devel < 3.5.1
Obsoletes:	%{_lib}%{name}-usrp-devel < 3.5.1
Requires:	%{devruntime} = %{EVRD}

%description -n %{devuhd}
This package contains header files needed by developers.

%files -n %{devuhd}
%{_includedir}/%{name}/uhd/*.h
%{_libdir}/pkgconfig/%{name}-uhd.pc
%{_libdir}/lib%{name}-uhd*.so

############################
%package -n %{libdigital}
Summary:	GNU Radio digital modulation blocks
Group:		System/Libraries

%description -n %{libdigital}
This is the gr-digital package.
It contains all of the digital modulation blocks, utilities, and examples.

%files -n %{libdigital}
%{_libdir}/lib%{name}-digital*.so.%{major}*

############################
%package -n %{devdigital}
Summary:	Digital
Group:		Development/Other
Requires:	%{libdigital} = %{EVRD}

%description -n %{devdigital}
This package contains header files needed by developers.

%files -n %{devdigital}
%{_includedir}/%{name}/digital/*.h
%{_libdir}/pkgconfig/%{name}-digital.pc
%{_libdir}/lib%{name}-digital*.so

############################
%package -n %{libvolk}
Summary:	GNU Radio Volk
Group:		System/Libraries

%description -n %{libvolk}
VOLK stands for Vector-Optimized Library of Kernels.
It is a library that was introduced into GNU Radio in December 2010.

%files -n %{libvolk}
%{_libdir}/libvolk.so.%{major}*
%{_libdir}/cmake/volk/VolkConfig.cmake

############################
%package -n %{devvolk}
Summary:	GNU Radio Volk devel files
Group:		Development/Other
Requires:	%{libvolk} = %{EVRD}

%description -n %{devvolk}
This package contains header files needed by developers.

%files -n %{devvolk}
%{_includedir}/volk/*
%{_libdir}/pkgconfig/volk.pc
%{_libdir}/libvolk.so

############################
%package -n %{libatsc}
Summary:	The GNU Radio blocks for ATSC decoding
Group:		System/Libraries

%description -n %{libatsc}
This pacage provides ATSC (HDTV) transmitter and receiver blocks.
Code related to the Advanced Television Standards Committee HDTV
implementation.

%files -n %{libatsc}
%{_libdir}/lib%{name}-atsc*.so.%{major}*

############################
%package -n %{devatsc}
Summary:	The GNU Radio blocks for ATSC decoding
Group:		Development/Other
Requires:	%{libatsc} = %{EVRD}

%description -n %{devatsc}
This package contains header files needed by developers.

%files -n %{devatsc}
%{_includedir}/%{name}/atsc/*.h
%{_includedir}/%{name}/atsc/CMakeLists.txt
%{_libdir}/pkgconfig/%{name}-atsc.pc
%{_libdir}/lib%{name}-atsc*.so


############################
%package -n %{libaudio}
Summary:	GNU Radio audio interfaces
Group:		System/Libraries
Obsoletes:	%{name}-sounder < 3.5.1
Obsoletes:	%{_lib}%{name}-audio-alsa0 < 3.5.1
Obsoletes:	%{_lib}%{name}-audio-jack0 < 3.5.1
Obsoletes:	%{_lib}%{name}-audio-portaudio0 < 3.5.1

%description -n %{libaudio}
This package includes all of the supported audio interfaces.

%files -n %{libaudio}
%{_libdir}/lib%{name}-audio*.so.%{major}*
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio-*.conf

############################
%package -n %{devaudio}
Summary:	GNU Radio audio interfaces - devel files
Group:		Development/Other
Requires:	%{libaudio} = %{EVRD}
Obsoletes:	%{_lib}%{name}-audio-alsa-devel < 3.5.1
Obsoletes:	%{_lib}%{name}-audio-jack-devel < 3.5.1
Obsoletes:	%{_lib}%{name}-audio-portaudio-devel < 3.5.1
Requires:	%{devruntime} = %{EVRD}

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
# Obsoletes with no new corresponding package added here
Obsoletes:	%{name}-gpio < 3.5.1
Obsoletes:	%{name}-radar-mono < 3.5.1
Obsoletes:	%{name}-radio-astronomy < 3.5.1
Obsoletes:	%{_lib}%{name}-msdd6000_0 < 3.5.1
Obsoletes:	%{libcore} < %{version}-%{release}
Obsoletes:	%{libgruel} < %{version}-%{release}
Obsoletes:	%{devgruel} < %{version}-%{release}
Obsoletes:	%{devcore} < %{version}-%{release}
Obsoletes:	%{devgruel} < %{version}-%{release}

%description -n %{libruntime}
This package contains the GNU Radio runtime libraries.

%files -n %{libruntime}
%{_libdir}/lib%{name}-runtime*.so.%{major}*

############################
%package -n %{devruntime}
Summary:	The GNU Radio runtime devel files
Group:		Development/Other
Requires:	%{libruntime} = %{EVRD}
Provides:	%{devruntime} = %{EVRD}
Obsoletes:	%{_lib}%{name}-msdd6000-devel  < 3.5.1

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
#libgnuradio-vocoder

%package -n %{libvocoder}
Summary:	GNU Radio C++ vocoder blocks
Group:		System/Libraries
Obsoletes:	%{_lib}%{name}-cvsd-vocoder0 < 3.5.1
Obsoletes:	%{_lib}%{name}-gsm-fr-vocoder0 < 3.5.1

%description -n %{libvocoder}
This is the gr-vocoder package.
It contains all available vocoders in GNU Radio.

%files -n %{libvocoder}
%{_libdir}/lib%{name}-vocoder*.so.%{major}*

############################
%package -n %{devvocoder}
Summary:	GNU Radio vocoder devel files
Group:		Development/Other
Requires:	%{libvocoder} = %{EVRD}
Obsoletes:	%{_lib}%{name}-cvsd-vocoder-devel < 3.5.1
Obsoletes:	%{_lib}%{name}-gsm-fr-vocoder-devel < 3.5.1

%description -n %{devvocoder}
This package contains header files needed by developers.

%files -n %{devvocoder}
%{_includedir}/%{name}/vocoder/*.h
%{_libdir}/pkgconfig/%{name}-vocoder.pc
%{_libdir}/lib%{name}-vocoder*.so

############################
#libgnuradio-noaa0

%package -n %{libnoaa}
Summary:	GNU Radio C++ block implementing the NOAA
Group:		System/Libraries

%description -n %{libnoaa}
This package provides a NOAA POES HRPT receiver/demodulator block
for GNU Radio.

%files -n %{libnoaa}
%{_libdir}/lib%{name}-noaa*.so.%{major}*

############################
%package -n %{devnoaa}
Summary:	GNU Radio C++ block implementing the NOAA
Group:		Development/Other
Requires:	%{libnoaa} = %{EVRD}

%description -n %{devnoaa}
This package contains header files needed by developers.

%files -n %{devnoaa}
%{_includedir}/%{name}/noaa/*.h
%{_libdir}/lib%{name}-noaa*.so
%{_libdir}/pkgconfig/%{name}-noaa.pc

############################
#libgnuradio-pager0

%package -n %{libpager}
Summary:	GNU Radio C++ block implementing the FLEX one-way pager protocol
Group:		System/Libraries

%description -n %{libpager}
This package provides an implementation of the FLEX one-way pager protocol
for GNU Radio.

%files -n %{libpager}
%{_libdir}/lib%{name}-pager*.so.%{major}*

############################
%package -n %{devpager}
Summary:	GNU Radio C++ block implementing the FLEX one-way pager protocol
Group:		Development/Other
Requires:	%{libpager} = %{EVRD}

%description -n %{devpager}
This package contains header files needed by developers.

%files -n %{devpager}
%{_includedir}/%{name}/pager/*.h
%{_libdir}/pkgconfig/%{name}-pager.pc
%{_libdir}/lib%{name}-pager*.so

############################
%package -n %{libqtgui}
Summary:	GNU Radio C++ blocks for QT-based GUI applications
Group:		System/Libraries

%description -n %{libqtgui}
This package contains the C++ library for using GNU Radio inside
QT-based GUI applications.

%files -n %{libqtgui}
%{_libdir}/lib%{name}-qtgui*.so.%{major}*
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-qtgui.conf

############################
%package -n %{devqtgui}
Summary:	GNU Radio C++ blocks for QT-based GUI applications
Group:		Development/Other
Requires:	%{libqtgui} = %{EVRD}

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
%{_libdir}/lib%{name}-trellis*.so.%{major}*

############################
%package -n %{devtrellis}
Summary:	GNU Radio C++ block implementing trellis-coded modulation
Group:		Development/Other
Requires:	%{libtrellis} = %{EVRD}

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
%{_libdir}/lib%{name}-video-sdl*.so.%{major}*

############################
%package -n %{devvideo_sdl}
Summary:	GNU Radio C++ block implementing video-sdl-coded modulation
Group:		Development/Other
Requires:	%{libvideo_sdl} = %{EVRD}

%description -n %{devvideo_sdl}
This package provides an interface to the SDL rendering library
for GNU Radio.

This package contains header files needed by developers.

%files -n %{devvideo_sdl}
%{_includedir}/%{name}/video_sdl/*.h
%{_libdir}/pkgconfig/%{name}-video-sdl.pc
%{_libdir}/lib%{name}-video-sdl*.so

############################
%package -n %{libfcd}
Summary:	Fun Cube Dongle libs
Group:		System/Libraries

%description -n %{libfcd}
Fun Cube Dongle library files

%files -n %{libfcd}
%{_libdir}/lib%{name}-fcd*.so.%{major}*

############################
%package -n %{devfcd}
Summary:	Fcd
Group:		System/Libraries
Requires:	%{libfcd} = %{EVRD}

%description -n %{devfcd}
This package contains header files needed by developers.

%files -n %{devfcd}

%{_includedir}/%{name}/fcd/*.h
%{_libdir}/pkgconfig/%{name}-fcd.pc
%{_libdir}/lib%{name}-fcd*.so

############################
%package -n %{libwavelet}
Summary:	GnuRadio Wavelet
Group:		System/Libraries

%description -n %{libwavelet}
GnuRadio Wavelet module.

%files -n %{libwavelet}
%{_libdir}/lib%{name}-wavelet*.so.%{major}*

############################
%package -n %{devwavelet}
Summary:	GnuRadio Wavelet development files
Group:		System/Libraries
Requires:	%{libwavelet} = %{EVRD}

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
%{_libdir}/lib%{name}-fft*.so.%{major}*

############################
%package -n %{devfft}
Summary:	GnuRadio fft development files
Group:		System/Libraries
Requires:	%{libfft} = %{EVRD}

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
%{_libdir}/lib%{name}-filter*.so.%{major}*

############################
%package -n %{devfilter}
Summary:	GnuRadio filter development files
Group:		System/Libraries
Requires:	%{libfilter} = %{EVRD}

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
%{_libdir}/lib%{name}-analog*.so.%{major}*

############################
%package -n %{devanalog}
Summary:	GnuRadio analog development files
Group:		System/Libraries
Requires:	%{libanalog} = %{EVRD}

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
%{_libdir}/lib%{name}-blocks*.so.%{major}*

############################
%package -n %{devblocks}
Summary:	GnuRadio blocks development files
Group:		System/Libraries
Requires:	%{libblocks} = %{EVRD}

%description -n %{devblocks}
This package contains header files needed by developers.

%files -n %{devblocks}
%{_includedir}/%{name}/blocks/*.h
%{_libdir}/lib%{name}-blocks*.so
%{_libdir}/pkgconfig/%{name}-blocks.pc

############################
%package -n %{libwxgui}
Summary:	GnuRadio wxgui
Group:		System/Libraries

%description -n %{libwxgui}
GnuRadio wxgui module.

%files -n %{libwxgui}
%{_libdir}/lib%{name}-wxgui*.so.%{major}*

############################
%package -n %{devwxgui}
Summary:	GnuRadio wxgui development files
Group:		System/Libraries
Requires:	%{libwxgui} = %{EVRD}

%description -n %{devwxgui}
This package contains header files needed by developers.

%files -n %{devwxgui}
%{_includedir}/%{name}/wxgui/*.h
%{_libdir}/lib%{name}-wxgui*.so
%{_libdir}/pkgconfig/gr-wxgui.pc

############################
%package -n %{libchannels}
Summary:	GnuRadio channels
Group:		System/Libraries

%description -n %{libchannels}
GnuRadio channels module.

%files -n %{libchannels}
%{_libdir}/lib%{name}-channels*.so.%{major}*

############################
%package -n %{devchannels}
Summary:	GnuRadio channels development files
Group:		System/Libraries
Requires:	%{libchannels} = %{EVRD}

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
%{_libdir}/lib%{name}-fec*.so.%{major}*

############################
%package -n %{devfec}
Summary:	GnuRadio fec development files
Group:		System/Libraries
Requires:	%{libfec} = %{EVRD}

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
%{_libdir}/lib%{name}-pmt*.so.%{major}*

############################
%package -n %{devpmt}
Summary:	GnuRadio pmt development files
Group:		System/Libraries
Requires:	%{libpmt} = %{EVRD}

%description -n %{devpmt}
This package contains header files needed by developers.

%files -n %{devpmt}
%{_libdir}/lib%{name}-pmt*.so
%{_includedir}/pmt/*.h

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
Requires:	python-numpy
Requires:	python-lxml
Requires:	pygtk2.0
Requires:	python-cheetah
Requires:	wxPython
Requires:	python-scipy
Requires:	python-opengl
# Explicit require on PyQt4 Resolves: rhbz#781494
Requires:	PyQt4
Obsoletes:	python-%{name}-msdd6000 < 3.5.1
Obsoletes:	python-%{name}-gruel < %{version}-%{release}
Obsoletes:	python-%{name}-core < %{version}-%{release}

%description -n python-%{name}-runtime
This package provides the modules that enable one to use gnuradio from
Python scripts.

%files -n python-%{name}-runtime
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/%{name}-runtime.conf
%dir %{py_platsitedir}/%{name}
%{py_platsitedir}/%{name}/gr
%{py_platsitedir}/%{name}/gru
%{py_platsitedir}/%{name}/__init__.*
%{py_platsitedir}/%{name}/eng_notation.*
%{py_platsitedir}/%{name}/eng_option.*
%{py_platsitedir}/%{name}/gr_unittest.*
%{py_platsitedir}/%{name}/gr_xmlrunner.*

%package -n python-%{name}-digital
Summary:	Python bindings for GNU Radio digital
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}

%description -n python-%{name}-digital
This package contains Python bindings for GNU Radio Digital.

%files -n python-%{name}-digital
%{py_platsitedir}/%{name}/digital/*

############################
%package -n python-%{name}-vocoder
Summary:	Python bindings for GNU Radio vocoder
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}
Obsoletes:	python-%{name}-cvsd-vocoder < 3.5.1
Obsoletes:	python-%{name}-gsm-fr-vocoder < 3.5.1

%description -n python-%{name}-vocoder
This package contains Python bindings for GNU Radio ATSC decoding.

%files -n python-%{name}-vocoder
%{py_platsitedir}/%{name}/vocoder/*

############################
%package -n python-%{name}-atsc
Summary:	Python bindings for GNU Radio ATSC decoding
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}

%description -n python-%{name}-atsc
This package contains Python bindings for GNU Radio ATSC decoding.
Code related to the Advanced Television Standards Committee HDTV
implementation.

%files -n python-%{name}-atsc
%{py_platsitedir}/%{name}/atsc/*

############################
%package -n python-%{name}-audio
Summary:	GNU Radio Python Audio Driver
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}
Obsoletes:	python-%{name}-audio-alsa < 3.5.1
Obsoletes:	python-%{name}-audio-jack < 3.5.1
Obsoletes:	python-%{name}-audio-portaudio < 3.5.1

%description -n python-%{name}-audio
This package provides the Python interface to the GNU Radio driver for the
audio system.

%files -n python-%{name}-audio
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio.conf
%{py_platsitedir}/%{name}/audio/*

############################
%package -n python-%{name}-qtgui
Summary:	GNU Radio Graphical Interface Routines based on QT
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}

%description -n python-%{name}-qtgui
This package provides the Python wrappers around the GNU Radio QT GUI
C++ blocks.

%files -n python-%{name}-qtgui
%{py_platsitedir}/%{name}/qtgui

############################
%package -n python-%{name}-trellis
Summary:	GNU Radio Trellis-Coded Modulation library
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}

%description -n python-%{name}-trellis
This package provides an implementation of trellis-coded modulation for
GNU Radio.

%files -n python-%{name}-trellis
%{py_platsitedir}/%{name}/trellis/*

############################
%package -n python-%{name}-uhd
Summary:	Python bindings for GNU Radio uhd driver
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}
Obsoletes:	python-%{name}-usrp < 3.5.1
Obsoletes:	python-%{name}-usrp2 < 3.5.1

%description -n python-%{name}-uhd
This package provides the Python interface to the GNU Radio uhd driver
and daughterboard drivers.

%files -n python-%{name}-uhd
%{py_platsitedir}/%{name}/uhd

############################
%package -n python-%{name}-video-sdl
Summary:	GNU Radio SDL Interface Library
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}

%description -n python-%{name}-video-sdl
This package provides an interface to the SDL rendering library for GNU Radio.

%files -n python-%{name}-video-sdl
%{py_platsitedir}/%{name}/video_sdl/*

############################
%package -n python-%{name}-wxgui
Summary:	GNU Radio GUI Routines based on wxPython
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}

%description -n python-%{name}-wxgui
This package provides high level GUI construction classes based upon the
wxPython bindings for wxWidgets.

%files -n python-%{name}-wxgui
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-wxgui.conf
%{py_platsitedir}/%{name}/wxgui

############################
%package -n python-%{name}-channels
Summary:	GNU Radio channels
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}

%description -n python-%{name}-channels
GNU Radio channels

%files -n python-%{name}-channels
%{py_platsitedir}/%{name}/channels

############################
%package -n python-%{name}-fec
Summary:	GNU Radio fec
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}

%description -n python-%{name}-fec
GNU Radio fec

%files -n python-%{name}-fec
%{py_platsitedir}/%{name}/fec

############################
%package -n python-%{name}-pmt
Summary:	GNU Radio pmt
Group:		Development/Python
Requires:	python-%{name}-runtime = %{EVRD}
Requires:	python-numpy
Requires:	python-opengl

%description -n python-%{name}-pmt
GNU Radio pmt

%files -n python-%{name}-pmt
%{py_platsitedir}/pmt/*

############################
%package -n python-%{name}-fcd
Summary:	GNU Radio Fun Cube Dongle
Group:		Development/Python

%description -n python-%{name}-fcd
GNU Radio Fun Cube Dongle

%files -n python-%{name}-fcd
%{py_platsitedir}/%{name}/fcd

############################
%package -n python-%{name}-wavelet
Summary:	GNU Radio wavelet
Group:		Development/Python

%description -n python-%{name}-wavelet
GNU Radio wavelet

%files -n python-%{name}-wavelet
%{py_platsitedir}/%{name}/wavelet

############################
%package -n python-%{name}-fft
Summary:	GNU Radio fft
Group:		Development/Python

%description -n python-%{name}-fft
GNU Radio fft

%files -n python-%{name}-fft
%{py_platsitedir}/%{name}/fft
%{py_platsitedir}/%{name}/plot_fft_base.*

############################
%package -n python-%{name}-filter
Summary:	GNU Radio filter
Group:		Development/Python

%description -n python-%{name}-filter
GNU Radio filter

%files -n python-%{name}-filter
%{py_platsitedir}/%{name}/filter
%{py_platsitedir}/%{name}/pyqt_filter.*

############################
%package -n python-%{name}-analog
Summary:	GNU Radio analog
Group:		Development/Python

%description -n python-%{name}-analog
GNU Radio analog

%files -n python-%{name}-analog
%{py_platsitedir}/%{name}/analog

############################
%package -n python-%{name}-blocks
Summary:	GNU Radio blocks
Group:		Development/Python

%description -n python-%{name}-blocks
GNU Radio blocks

%files -n python-%{name}-blocks
%{py_platsitedir}/%{name}/blocks

############################
%package -n python-%{name}-modtool
Summary:	GNU Radio modtool
Group:		Development/Python

%description -n python-%{name}-modtool
GNU Radio modtool

%files -n python-%{name}-modtool
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/modtool.conf
%{py_platsitedir}/%{name}/modtool
%{py_platsitedir}/volk_modtool/*

############################
%if %{with ice}
%package -n python-%{name}-ctrlport
Summary:	GNU Radio ctrlport
Group:		Development/Python

%description -n python-%{name}-ctrlport
GNU Radio ctrlport

%files -n python-%{name}-ctrlport
%{_sysconfdir}/%{name}/ctrlport.conf.example
%{py_platsitedir}/%{name}/ctrlport
%{py_platsitedir}/frontend_ice.*
%{py_platsitedir}/%{name}_ice.*
%endif

#######################################################
#######################################################
#
# Software packages and others
#
#######################################################
#######################################################

%package companion
Summary:	The GNU Radio Companion
Group:		Communications
Requires:	python-%{name}-runtime = %{EVRD}
Requires:	python-gnuradio-pmt = %{EVRD}
Suggests:	%{name}-examples = %{EVRD}
Requires:	python-cheetah
Requires:	pygtk2.0
Requires:	python-lxml
Obsoletes:	grc < 3.5.1

%description companion
GRC is a graphical flowgraph editor for the GNU Software Radio.

%files companion
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/grc.conf
%{_bindir}/%{name}-companion
%{_datadir}/applications/%{name}-grc.desktop
%{_datadir}/mime/application/*.xml
%{_iconsdir}/hicolor/*/apps/%{name}-grc.png
%{_datadir}/%{name}/grc
%{py_platsitedir}/%{name}/grc
%{py_platsitedir}/grc_%{name}


############################
%package  noaa
Summary:	GNU Radio NOAA POES HRPT receiver
Group:		Communications
Requires:	python-%{name}-runtime = %{EVRD}

%description noaa
This package provides and implements an NOAA POES HRPT receiver.

%files noaa
%{py_platsitedir}/%{name}/noaa

############################
%package pager
Summary:	GNU Radio FLEX Pager Decoder
Group:		Communications
Requires:	python-%{name}-uhd = %{EVRD}

%description pager
This package provides a decoder for the FLEX paging protocol for GNU Radio.

%files pager
%{_bindir}/usrp_flex*
%{py_platsitedir}/%{name}/pager

############################
%package utils
Summary:	GNU Radio Utilities
Group:		Communications
Requires:	python-%{name}-wxgui = %{EVRD}
Requires:	python-matplotlib
Requires:	python-scipy
Requires:	python-qt4
#Requires:	python-qwt

%description utils
This package provides commonly used utilities for GNU Radio.

%files utils
%{py_platsitedir}/%{name}/plot_psd_base.*
%{py_platsitedir}/%{name}/plot_data.*
%{py_platsitedir}/%{name}/pyqt_plot.*
%{_bindir}/%{name}-config-info

## Where do these live?
%{_bindir}/gr_filter_design
%{_bindir}/gr_plot_*
%{_bindir}/uhd_*
%{_bindir}/gr_read_file_metadata
%{_bindir}/grcc
%{_bindir}/gr_modtool
%{_bindir}/gr_constellation_plot
%{_bindir}/gr_psd_plot_b
%{_bindir}/gr_psd_plot_c
%{_bindir}/gr_psd_plot_f
%{_bindir}/gr_psd_plot_i
%{_bindir}/gr_psd_plot_s
%{_bindir}/gr_spectrogram_plot_b
%{_bindir}/gr_spectrogram_plot_c
%{_bindir}/gr_spectrogram_plot_f
%{_bindir}/gr_spectrogram_plot_i
%{_bindir}/gr_spectrogram_plot_s
%{_bindir}/gr_time_plot_b
%{_bindir}/gr_time_plot_c
%{_bindir}/gr_time_plot_f
%{_bindir}/gr_time_plot_i
%{_bindir}/gr_time_plot_s
%{_bindir}/gr_time_raster_b
%{_bindir}/gr_time_raster_f
%{_bindir}/volk_modtool
%{_bindir}/volk_profile
%{_bindir}/volk-config-info
%if %{with ice}
%{_bindir}/gr-ctrlport-curses
%{_bindir}/gr-ctrlport-cursesc
%{_bindir}/gr-ctrlport-curseso
%{_bindir}/gr-ctrlport-monitor
%{_bindir}/gr-ctrlport-monitorc
%{_bindir}/gr-ctrlport-monitoro
%{_bindir}/gr-perf-monitorx
%{_bindir}/gr-perf-monitorxc
%{_bindir}/gr-perf-monitorxo
%endif
%{_libdir}/cmake/%{name}

#######################################################
#######################################################
%prep
%setup -q
%autopatch -p1

%build
%cmake
%make

%check
## TODO Some tests fail only in i586 build.
# qa_qtgui test failure is a known issue and is skipped.
# Test failures do not halt builds, so check the log.
cd build
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
ctest -V -E qa_qtgui ||:

%install
%makeinstall_std -C build

#icons
for i in 32 48 64 128 256; do
	install -Dpm0644 %{buildroot}%{_datadir}/%{name}/grc/freedesktop/grc-icon-${i}.png \
		%{buildroot}/%{_iconsdir}/hicolor/${i}x${i}/apps/%{name}-grc.png
done

############################
# Desktop files
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/mime/application
mv %{buildroot}%{_datadir}/%{name}/grc/freedesktop/%{name}-grc.xml %{buildroot}%{_datadir}/mime/application/

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
rm -f %{buildroot}/usr/libexec/%{name}/grc_setup_freedesktop
rm -rf %{buildroot}/%{_datadir}/%{name}/grc/freedesktop

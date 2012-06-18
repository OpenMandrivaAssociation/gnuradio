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
%define libcore		%mklibname %{name}-core %{major}
%define devcore		%mklibname %{name}-core -d
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
%define libgruel	%mklibname gruel %{major}
%define devgruel	%mklibname gruel -d
%define libfcd		%mklibname %{name}-fcd %{major}
%define devfcd		%mklibname %{name}-fcd -d
%define libwave		%mklibname %{name}-wavelet %{major}
%define devwave		%mklibname %{name}-wavelet -d
%define devfft		%mklibname fft -d
%define libfft		%mklibname fft

Name:		gnuradio
Version:	3.6.1
Release:	1
Summary:	Software defined radio framework
Group:		Development/Other 
License:	GPLv3+
URL:		http://www.gnuradio.org
Source0:	%{name}-%{version}.tar.gz
# Create tarball from git with:
# $ ./make-tarball gnuradio http://gnuradio.org/git/gnuradio.git
# See note in make-tarball script
# Unlike the release tarballs the created tarball will be Cmake enabled.
Source1:	make-tarball
Patch0:		gnuradio-3.5.1-mga-fix_install_paths_in_CMakeLists.patch
Patch2:		gnuradio-3.6.1-fix-linkage.patch

BuildRequires:	cmake
BuildRequires:	sdcc
BuildRequires:	fftw-devel
BuildRequires:	cppunit-devel
BuildRequires:	wxPython
BuildRequires:	xmlto
BuildRequires:	texlive-graphics
BuildRequires:	graphviz
BuildRequires:	boost-devel
BuildRequires:	python-devel
BuildRequires:	swig
BuildRequires:	doxygen
BuildRequires:	libusb-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(guile-2.0)
BuildRequires:	portaudio-devel
BuildRequires:	libtool
BuildRequires:	gsl-devel
BuildRequires:	python-qt4-devel
#BuildRequires:	python-qwt
BuildRequires:	libqwtplot3d-devel
BuildRequires:	python-cheetah
BuildRequires:	xdg-utils
BuildRequires:	python-lxml
BuildRequires:	pygtk2.0-libglade
BuildRequires:	liborc-devel
BuildRequires:	uhd-devel
BuildRequires:	python-numpy
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	%{_lib}qwt-devel
BuildRequires:	desktop-file-utils

Requires(pre):	shadow-utils

Requires:	gnuradio-companion
Requires:	gnuradio-doc
Requires:	gnuradio-examples
Requires:	gnuradio-noaa
Requires:	gnuradio-pager
Requires:	gnuradio-utils
Requires:	%{libatsc}
Requires:	%{libcore}
Requires:	%{libnoaa}
Requires:	%{libpager}
Requires:	%{libqtgui}
Requires:	%{libtrellis}
Requires:	%{libvideo_sdl}
Requires:	%{libuhd}
Requires:	%{libdigital}
Requires:	%{libvolk}
Requires:	%{libaudio}
Requires:	%{libvocoder}
Requires:	%{libgruel}
Requires:	%{libfcd}
Requires:	python-gnuradio-atsc
Requires:	python-gnuradio-core
Requires:	python-gnuradio-qtgui
Requires:	python-gnuradio-trellis
Requires:	python-gnuradio-video-sdl
Requires:	python-gnuradio-wxgui
Requires:	python-gnuradio-digital
Requires:	python-gnuradio-gruel
Requires:	python-gnuradio-vocoder
Requires:	python-gnuradio-audio
Requires:	python-gnuradio-uhd
Requires:	python-gnuradio-fcd

Obsoletes:	%{name} < %{version}-%{release}
Provides:	%{name} = %{version}-%{release}

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
Group:		Development/Other
BuildArch:	noarch

%description doc
This package contains the documentation for the GNU Radio software
defined radio system.

%files doc
%doc AUTHORS
%doc %{_docdir}/*
%{_datadir}/applications/%{name}-doc.desktop

############################
%package examples
Summary:	GNU Radio Example Programs
Group:		Development/Other
BuildArch:	noarch

%description examples
This package provides examples of GNU Radio usage using Python.

%files examples
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/grc

############################
############################
#
# Lib and devel packages
#
############################
############################

############################
%package -n %{libuhd}
Summary:	uhd
Group:		System/Libraries
Obsoletes:	%{_lib}gnuradio-usrp0 < 3.5.1
Obsoletes:	%{_lib}gnuradio-usrp2_0 < 3.5.1
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
Requires:	%{libuhd} = %{version}-%{release}
Obsoletes:	%{_lib}gnuradio-usrp2-devel < 3.5.1
Obsoletes:	%{_lib}gnuradio-usrp-devel < 3.5.1
Requires:	%{devcore} = %{version}-%{release}


%description -n %{devuhd}
This package contains header files needed by developers.

%files -n %{devuhd}
# %{_includedir}/%{name}/gr_uhd_*.h
%{_libdir}/pkgconfig/%{name}-uhd.pc
%{_libdir}/lib%{name}-uhd*.so


########################################

%package -n %{libfft}
Summary:	fft package for %{name}
Group:		System/Libraries
Provides:	%{name}-fft

%description -n %{libfft}
This is the GNU Radio FFT package. 

%files -n %{libfft}
%{_libdir}/lib%{name}-fft*.so.%{major}*



%package -n %{devfft}
Summary:	FFT devel files
Group:		Development/Other
Requires:	%{libfft} = %{version}-%{release}
Requires:	%{devcore} = %{version}-%{release}


%description -n %{devfft}
This package contains header files ans libs needed for
developers.

%files -n %{devfft}
%{_includedir}/%{name}/fft/*.h
%{_libdir}/pkgconfig/%{name}-fft.pc
%{_libdir}/lib%{name}-fft*.so


%package -n python-%{name}-fft
Summary:	Python bindings for GNU Radio FFT
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-fft
This package contains Python bindings for GNU Radio wavelet.

%files -n python-%{name}-fft
%{python_sitearch}/gnuradio/fft/*


############################
#libgnuradio-digital

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
Summary:	digital
Group:		Development/Other
Requires:	%{libdigital} = %{version}-%{release}

%description -n %{devdigital}
This package contains header files needed by developers.

%files -n %{devdigital}
%{_includedir}/%{name}/digital_*.h
%{_libdir}/pkgconfig/%{name}-digital.pc
%{_libdir}/lib%{name}-digital*.so


############################
#libgnuradio-volk

%package -n %{libvolk}
Summary:	GNU Radio Volk
Group:		System/Libraries

%description -n %{libvolk}
VOLK stands for Vector-Optimized Library of Kernels. 
It is a library that was introduced into GNU Radio in December 2010. 

%files -n %{libvolk}
%{_libdir}/libvolk.so.%{major}*
# not sure where to put this:
%{_bindir}/volk_profile


############################
%package -n %{devvolk}
Summary:	GNU Radio Volk devel files
Group:		Development/Other
Requires:	%{libvolk} = %{version}-%{release}

%description -n %{devvolk}
This package contains header files needed by developers.

%files -n %{devvolk}
%{_includedir}/volk/*
%{_libdir}/pkgconfig/volk.pc
%{_libdir}/libvolk.so


############################
#libgnuradio-atsc0

%package -n %{libatsc}
Summary:	The GNU Radio blocks for ATSC decoding
Group:		System/Libraries

%description -n %{libatsc}
This pacage provides ATSC (HDTV) transmitter and receiver blocks.

%files -n %{libatsc}
%{_libdir}/lib%{name}-atsc*.so.%{major}*


############################
%package -n %{devatsc}
Summary:	The GNU Radio blocks for ATSC decoding
Group:		Development/Other
Requires:	%{libatsc} = %{version}-%{release}

%description -n %{devatsc}
This package contains header files needed by developers.

%files -n %{devatsc}
%{_includedir}/%{name}/atsc_*.h
%{_includedir}/%{name}/atsci_*.h
%{_includedir}/%{name}/convolutional_interleaver.h
%{_includedir}/%{name}/create_atsci_*.h
%{_includedir}/%{name}/fpll_btloop_coupling.h
%{_includedir}/%{name}/interleaver_fifo.h
%{_libdir}/pkgconfig/%{name}-atsc.pc
%{_libdir}/lib%{name}-atsc*.so


############################
%package -n %{libaudio}
Summary:	GNU Radio audio interfaces
Group:		System/Libraries
Requires:	libportaudio2
Obsoletes:	gnuradio-sounder < 3.5.1
Obsoletes:	%{_lib}gnuradio-audio-alsa0 < 3.5.1
Obsoletes:	%{_lib}gnuradio-audio-jack0 < 3.5.1
Obsoletes:	%{_lib}gnuradio-audio-portaudio0 < 3.5.1


%description -n %{libaudio}
This package includes all of the supported audio interfaces.

%files -n %{libaudio}
%{_libdir}/lib%{name}-audio*.so.%{major}*
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio-*.conf


############################
%package -n %{devaudio}
Summary:	GNU Radio audio interfaces - devel files
Group:		Development/Other
Requires:	%{libaudio} = %{version}-%{release}
Obsoletes:	%{_lib}gnuradio-audio-alsa-devel < 3.5.1
Obsoletes:	%{_lib}gnuradio-audio-jack-devel < 3.5.1
Obsoletes:	%{_lib}gnuradio-audio-portaudio-devel < 3.5.1
Requires:	%{devcore} = %{version}-%{release}

%description -n %{devaudio}
This package contains header files needed by developers.

%files -n %{devaudio}
#% {_includedir}/%{name}/gr_audio_*.h
%{_libdir}/pkgconfig/%{name}-audio.pc
%{_libdir}/lib%{name}-audio*.so


############################
#libgnuradio-core0

%package -n %{libcore}
Summary:	The GNU Radio Core Library
Group:		System/Libraries
# Obsoletes with no new corresponding package added here 
Obsoletes:	gnuradio-gpio < 3.5.1
Obsoletes:	gnuradio-radar-mono < 3.5.1
Obsoletes:	gnuradio-radio-astronomy < 3.5.1
Obsoletes:	%{_lib}gnuradio-msdd6000_0 < 3.5.1

%description -n %{libcore}
This package contains the core GNU Radio libraries.

%files -n %{libcore}
%{_libdir}/lib%{name}-core*.so.%{major}*


############################
%package -n %{devcore}
Summary:	The GNU Radio Core devel files
Group:		Development/Other
Requires:	%{libcore} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}
# Obsoletes (devel) with no new corresponding package added here 
Obsoletes:	%{_lib}gnuradio-msdd6000-devel  < 3.5.1

%description -n %{devcore}
This package contains header files needed by developers.

%files -n %{devcore}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/gr_*.h
%{_includedir}/%{name}/gri_*.h

%{_includedir}/%{name}/ccomplex_*.h
%{_includedir}/%{name}/complex_*.h
%{_includedir}/%{name}/fcomplex*.h
%{_includedir}/%{name}/float_dotprod*.h
%{_includedir}/%{name}/gnuradio_swig_bug_workaround.h
%{_includedir}/%{name}/i2c*.h
%{_includedir}/%{name}/malloc16.h
%{_includedir}/%{name}/microtune_*.h
%{_includedir}/%{name}/swig
%{_includedir}/%{name}/ppio*.h
%{_includedir}/%{name}/qa_filter.h
%{_includedir}/%{name}/random.h
%{_includedir}/%{name}/rs.h
%{_includedir}/%{name}/sdr_1000.h
%{_includedir}/%{name}/short_dotprod*.h
%{_includedir}/%{name}/sse_debug.h
%{_includedir}/%{name}/viterbi.h
%{_libdir}/pkgconfig/%{name}-core.pc
%{_libdir}/lib%{name}-core*.so

############################
#libgnuradio-vocoder

%package -n %{libvocoder}
Summary:	GNU Radio C++ vocoder blocks
Group:		System/Libraries
Obsoletes:	%{_lib}gnuradio-cvsd-vocoder0 < 3.5.1
Obsoletes:	%{_lib}gnuradio-gsm-fr-vocoder0 < 3.5.1

%description -n %{libvocoder}
This is the gr-vocoder package.
It contains all available vocoders in GNU Radio.

%files -n %{libvocoder}
%{_libdir}/lib%{name}-vocoder*.so.%{major}*


############################
%package -n %{devvocoder}
Summary:	GNU Radio vocoder devel files
Group:		Development/Other
Requires:	%{libvocoder} = %{version}-%{release}
Obsoletes:	%{_lib}gnuradio-cvsd-vocoder-devel < 3.5.1
Obsoletes:	%{_lib}gnuradio-gsm-fr-vocoder-devel < 3.5.1

%description -n %{devvocoder}
This package contains header files needed by developers.

%files -n %{devvocoder}
%{_includedir}/%{name}/vocoder_*.h
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
Requires:	%{libnoaa} = %{version}-%{release}

%description -n %{devnoaa}
This package contains header files needed by developers.

%files -n %{devnoaa}
%{_includedir}/%{name}/noaa_*.h
%{_libdir}/lib%{name}-noaa*.so
%{_libdir}/pkgconfig/%{name}-noaa.pc

####################
#libwave

%package -n %{libwave}
Summary:	GNU Radio C++ block implementing the NOAA
Group:		System/Libraries

%description -n %{libwave}
This package provides a NOAA POES HRPT receiver/demodulator block
for GNU Radio.
 
%files -n %{libwave}
%{_libdir}/lib%{name}-wavelet*.so.%{major}*


############################
%package -n %{devwave}
Summary:	GNU Radio C++ block implementing the NOAA
Group:		Development/Other
Requires:	%{libwave} = %{version}-%{release}

%description -n %{devwave}
This package contains header files needed by developers.

%files -n %{devwave}
%{_includedir}/%{name}/wavelet_*
%{_libdir}/lib%{name}-wavelet-%{version}.so
%{_libdir}/lib%{name}-wavelet.so
%{_libdir}/pkgconfig/%{name}-wavelet.pc

%package -n python-%{name}-wavelet
Summary:	Python bindings for GNU Radio wavelet
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-wavelet
This package contains Python bindings for GNU Radio wavelet.

%files -n python-%{name}-wavelet
%{python_sitearch}/gnuradio/wavelet/*


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
Requires:	%{libpager} = %{version}-%{release}

%description -n %{devpager}
This package contains header files needed by developers.

%files -n %{devpager}
%{_includedir}/%{name}/pager*.h
%{_libdir}/pkgconfig/%{name}-pager.pc
%{_libdir}/lib%{name}-pager*.so


############################
#libgnuradio-qtgui0

%package -n %{libqtgui}
Summary:	GNU Radio C++ blocks fro QT-based GUI applications
Group:		System/Libraries

%description -n %{libqtgui}
This package contains the C++ library for using GNU Radio inside
QT-based GUI applications.

%files -n %{libqtgui}
%{_libdir}/lib%{name}-qtgui*.so.%{major}*


############################
%package -n %{devqtgui}
Summary:	GNU Radio C++ blocks for QT-based GUI applications
Group:		Development/Other
Requires:	%{libqtgui} = %{version}-%{release}

%description -n %{devqtgui}
This package contains the C++ library for using GNU Radio inside
QT-based GUI applications.
This package contains header files needed by developers.

%files -n %{devqtgui}
%{_includedir}/%{name}/qtgui*.h
%{_includedir}/%{name}/ConstellationDisplayPlot.h
%{_includedir}/%{name}/FrequencyDisplayPlot.h
%{_includedir}/%{name}/SpectrumGUIClass.h
%{_includedir}/%{name}/TimeDomainDisplayPlot.h
%{_includedir}/%{name}/WaterfallDisplayPlot.h
%{_includedir}/%{name}/plot_waterfall.h
%{_includedir}/%{name}/spectrumUpdateEvents.h
%{_includedir}/%{name}/spectrumdisplayform.h
%{_includedir}/%{name}/waterfallGlobalData.h
%{_includedir}/%{name}/timedisplayform.h
%{_libdir}/pkgconfig/%{name}-qtgui.pc
%{_libdir}/lib%{name}-qtgui*.so

############################
#libgnuradio-trellis0

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
Requires:	%{libtrellis} = %{version}-%{release}

%description -n %{devtrellis}
This package contains header files needed by developers.

%files -n %{devtrellis}
%{_includedir}/%{name}/trellis*.h
%{_includedir}/%{name}/quicksort_index.h
%{_includedir}/%{name}/interleaver.h
%{_includedir}/%{name}/fsm.h
%{_includedir}/%{name}/base.h
%{_includedir}/%{name}/siso_type.h
%{_includedir}/%{name}/calc_metric.h
%{_includedir}/%{name}/core_algorithms.h
%{_libdir}/pkgconfig/%{name}-trellis.pc
%{_libdir}/lib%{name}-trellis*.so

############################
#libgnuradio-video-sdl0

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
Requires:	%{libvideo_sdl} = %{version}-%{release}

%description -n %{devvideo_sdl}
This package provides an interface to the SDL rendering library
for GNU Radio.

This package contains header files needed by developers.

%files -n %{devvideo_sdl}
%{_includedir}/%{name}/video_sdl*.h
%{_libdir}/pkgconfig/%{name}-video-sdl.pc
%{_libdir}/lib%{name}-video-sdl*.so


############################
#libgruel0

%package -n %{libgruel}
Summary:	GNU Radio Utility Etcetera Library
Group:		System/Libraries

%description -n %{libgruel}
This package implements a variety of low-level utility routines for
GNU Radio.

%files -n %{libgruel}
%{_libdir}/libgruel*.so.%{major}*


############################
%package -n %{devgruel}
Summary:	GNU Radio Utility Etcetera Library
Group:		Development/Other
Requires:	%{libgruel} = %{version}-%{release}

%description -n %{devgruel}
This package implements a variety of low-level utility routines for
GNU Radio.

This package contains header files needed by developers.

%files -n %{devgruel}
%{_includedir}/gruel/*
%{_libdir}/pkgconfig/gruel.pc
%{_libdir}/libgruel*.so

############################
#libfcd

%package -n %{libfcd}
Summary:	Fun Cube Dongle libs
Group:		System/Libraries

%description -n %{libfcd}
Fun Cube Dongle library files

%files -n %{libfcd}
%{_libdir}/lib%{name}-fcd*.so.%{major}*

############################
%package -n %{devfcd}
Summary:	fcd
Group:		System/Libraries
Requires:	%{libfcd} = %{version}-%{release}

%description -n %{devfcd}
This package contains header files needed by developers.

%files -n %{devfcd}

%{_includedir}/%{name}/fcd_api.h
%{_includedir}/%{name}/fcd_source_c.h
%{_libdir}/pkgconfig/%{name}-fcd.pc
%{_libdir}/lib%{name}-fcd*.so

############################
############################
#
# Python packages
#
############################
############################


%package -n python-%{name}-digital
Summary:	Python bindings for GNU Radio digital
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-digital
This package contains Python bindings for GNU Radio Digital.

%files -n python-%{name}-digital
%{python_sitearch}/%{name}/digital/*


############################
%package -n python-%{name}-gruel
Summary:	Python bindings for GNU Radio gruel
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-gruel
This package contains Python bindings for GNU Radio gruel.

%files -n python-%{name}-gruel
%{python_sitearch}/gruel/*


############################
%package -n python-%{name}-vocoder
Summary:	Python bindings for GNU Radio vocoder
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}
Obsoletes:	python-gnuradio-cvsd-vocoder < 3.5.1
Obsoletes:	python-gnuradio-gsm-fr-vocoder < 3.5.1

%description -n python-%{name}-vocoder
This package contains Python bindings for GNU Radio ATSC decoding.

%files -n python-%{name}-vocoder
%{python_sitearch}/%{name}/vocoder/*


############################
%package -n python-%{name}-atsc
Summary:	Python bindings for GNU Radio ATSC decoding
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-atsc
This package contains Python bindings for GNU Radio ATSC decoding.

%files -n python-%{name}-atsc
%{python_sitearch}/%{name}/_atsc.*
%{python_sitearch}/%{name}/atsc.*


############################
%package -n python-%{name}-audio
Summary:	GNU Radio Python Audio Driver
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}
Obsoletes:	python-gnuradio-audio-alsa < 3.5.1
Obsoletes:	python-gnuradio-audio-jack < 3.5.1
Obsoletes:	python-gnuradio-audio-portaudio < 3.5.1

%description -n python-%{name}-audio
This package provides the Python interface to the GNU Radio driver for the
audio system.

%files -n python-%{name}-audio
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio.conf
%{python_sitearch}/%{name}/audio/*


############################
%package -n python-%{name}-core
Summary:	Python bindings for GNU Radio core library
Group:		Development/Python
Requires:	python-numpy
Requires:	python-lxml
Requires:	pygtk2.0
Requires:	python-cheetah
Requires:	wxPython
Requires:	python-scipy
# Explicit require on PyQt4 Resolves: rhbz#781494
Requires:	PyQt4
# Obsoletes (python) with no new corresponding package added here
Obsoletes:	python-gnuradio-msdd6000 < 3.5.1

%description -n python-%{name}-core
This package provides the modules that enable one to use gnuradio from
Python scripts.

%files -n python-%{name}-core
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gnuradio-core.conf
%dir %{python_sitearch}/%{name}
%{python_sitearch}/%{name}/blks2
%{python_sitearch}/%{name}/blks2impl
%{python_sitearch}/%{name}/gr
%{python_sitearch}/%{name}/gru
%{python_sitearch}/%{name}/gruimpl
%{python_sitearch}/%{name}/__init__.*
%{python_sitearch}/%{name}/eng_notation.*
%{python_sitearch}/%{name}/eng_option.*
%{python_sitearch}/%{name}/gr_unittest.*
%{python_sitearch}/%{name}/optfir.*
%{python_sitearch}/%{name}/window.*


############################
%package -n python-%{name}-qtgui
Summary:	GNU Radio Graphical Interface Routines based on QT
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-qtgui
This package provides the Python wrappers around the GNU Radio QT GUI
C++ blocks.

%files -n python-%{name}-qtgui
%{python_sitearch}/%{name}/qtgui


############################
%package -n python-%{name}-trellis
Summary:	GNU Radio Trellis-Coded Modulation library
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-trellis
This package provides an implementation of trellis-coded modulation for
GNU Radio.

%files -n python-%{name}-trellis
%{python_sitearch}/%{name}/_trellis.*
%{python_sitearch}/%{name}/trellis.*


############################
%package -n python-%{name}-uhd
Summary:	Python bindings for GNU Radio uhd driver
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}
Obsoletes:	python-gnuradio-usrp < 3.5.1
Obsoletes:	python-gnuradio-usrp2 < 3.5.1

%description -n python-%{name}-uhd
This package provides the Python interface to the GNU Radio uhd driver
and daughterboard drivers.

%files -n python-%{name}-uhd
%{python_sitearch}/%{name}/uhd
%{_bindir}/uhd_*


############################
%package -n python-%{name}-video-sdl
Summary:	GNU Radio SDL Interface Library
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-video-sdl
This package provides an interface to the SDL rendering library for GNU Radio.

%files -n python-%{name}-video-sdl
%{python_sitearch}/%{name}/_video_sdl.*
%{python_sitearch}/%{name}/video_sdl.*


############################
%package -n python-%{name}-wxgui
Summary:	GNU Radio Graphical Interface Routines based on wxPython
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}
Requires:	python-numpy
Requires:	python-opengl

%description -n python-%{name}-wxgui
This package provides high level GUI construction classes based upon the wxPython bindings 
for wxWidgets.

%files -n python-%{name}-wxgui
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-wxgui.conf
%{python_sitearch}/%{name}/wxgui

############################
%package -n python-%{name}-fcd
Summary:	GNU Radio Fun Cube Dongle
Group:		Development/Python

%description -n python-%{name}-fcd
GNU Radio Fun Cube Dongle

%files -n python-%{name}-fcd
%{python_sitearch}/%{name}/fcd


############################
############################
#
# Software packages and others
#
############################
############################

%package companion
Summary:	The GNU Radio Companion
Group:		Development/Other
Requires:	python-%{name}-core = %{version}-%{release}
Requires:	python-cheetah
Requires:	pygtk2.0
Requires:	python-lxml
Obsoletes:	grc < 3.5.1

%description companion
GRC is a graphical flowgraph editor for the GNU Software Radio.

%files companion
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/grc.conf
%{_bindir}/gnuradio-companion
%{_datadir}/applications/%{name}-grc.desktop
%{_datadir}/mime/application/*.xml
%{_iconsdir}/hicolor/*/apps/gnuradio-grc.png
%{_datadir}/%{name}/grc
%{python_sitearch}/%{name}/grc
%{python_sitearch}/grc_%{name}


############################
%package  noaa
Summary:	GNU Radio NOAA POES HRPT receiver
Group:		Development/Other
Requires:	python-%{name}-core = %{version}-%{release}

%description noaa
This package provides and implements an NOAA POES HRPT receiver.

%files noaa
#%{_bindir}/usrp_rx_hrpt.py
#%{_bindir}/file_rx_hrpt.py
#%{_bindir}/hrpt_decode.py
#%{_bindir}/hrpt_demod.py
#%{_bindir}/usrp_rx_hrpt_nogui.py
%{python_sitearch}/%{name}/noaa


############################
%package pager
Summary:	GNU Radio FLEX Pager Decoder
Group:		Development/Other
Requires:	python-%{name}-uhd = %{version}-%{release}

%description pager
This package provides a decoder for the FLEX paging protocol for GNU Radio.

%files pager
%{_bindir}/usrp_flex*
%{python_sitearch}/%{name}/pager


############################
%package utils
Summary:	GNU Radio Utilities
Group:		Development/Other
Requires:	python-%{name}-wxgui = %{version}-%{release}
Requires:	python-matplotlib
Requires:	python-scipy
Requires:	python-qt4
Requires:	python-qwt

%description utils
This package provides commonly used utilities for GNU Radio.

%files utils
%{_bindir}/gr_filter_design
%{_bindir}/gr_plot*
%{python_sitearch}/%{name}/plot_data.*
%{python_sitearch}/%{name}/plot_fft*.py*
%{python_sitearch}/%{name}/plot_psd*.py*
%{python_sitearch}/%{name}/pyqt_filter.*
%{python_sitearch}/%{name}/pyqt_plot.*
%{_bindir}/gnuradio-config-info
# This should really be in a devel package
%{_libdir}/pkgconfig/gr-wxgui.pc
# Not sure if this lives here
%{python_sitearch}/%{name}/gr_xmlrunner.*

############################
############################
%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .gnuradio-3.5.1-mga-fix_install_paths_in_CMakeLists.patch
%patch2 -p1 -b .gnuradio-3.6.1-linkage.patch

%build
%cmake
make

# TODO
# At present 1 test fails (qtgui) when run during build, either in iurt or local system.
# All tests pass when run in build dir manually on local system.
#%%check
#cd build
#make test

%install
%makeinstall_std -C build

#icons
for i in 32 48 64 128 256; do
	install -Dpm0644 %{buildroot}%{_datadir}/%{name}/grc/freedesktop/grc-icon-${i}.png \
		%{buildroot}/%{_iconsdir}/hicolor/${i}x${i}/apps/gnuradio-grc.png
done

# Desktop files
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/mime/application
mv %{buildroot}%{_datadir}/%{name}/grc/freedesktop/gnuradio-grc.xml %{buildroot}%{_datadir}/mime/application/

cat > gnuradio-doc.desktop << EOF
[Desktop Entry]
Version=1.0
Name=Gnu Radio C++ API Documentation
GenericName=Gnu Radio C++ API Documentation
Exec=xdg-open /usr/share/doc/%{name}-%{version}/html/index.html
Icon=gnuradio-grc
Terminal=false
Type=Application
Categories=System;Documentation;X-Mandriva-Desktop;
X-Desktop-File-Install-Version=0.19
EOF

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{name}-doc.desktop

desktop-file-install \
--add-category='X-Mandriva-Desktop' \
--set-key=Name \
--set-value='Gnu Radio Companion' \
--dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/%{name}/grc/freedesktop/%{name}-grc.desktop

############################

#we don't want these
find %{buildroot} -name "*.la" -exec rm -rf {} \;
rm -rf %{buildroot}%{_bindir}/create-gnuradio-out-of-tree-project
rm -rf %{buildroot}%{_libdir}/%{name}/grc_setup_freedesktop
rm -rf %{buildroot}/%{_datadir}/%{name}/grc/freedesktop	

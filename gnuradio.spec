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
%define libwavelet	%mklibname %{name}-wavelet %{major}
%define devwavelet	%mklibname %{name}-wavelet -d
%define libfft		%mklibname %{name}-fft %{major}
%define devfft		%mklibname %{name}-fft -d
%define libfilter	%mklibname %{name}-filter %{major}
%define devfilter	%mklibname %{name}-filter -d

Summary:	Software defined radio framework
Name:		gnuradio
Version:	3.6.2
Release:	5
License:	GPLv3+
Group:		Communications
Url:		http://www.gnuradio.org
Source0:	%{name}-%{version}.tar.gz
# Create tarball from git with:
# $ ./make-tarball gnuradio http://gnuradio.org/git/gnuradio.git
# See note in make-tarball script
Source1:	make-tarball
Source100:      gnuradio.rpmlintrc

Patch0:		gnuradio-3.6.2-mga-fix_install_paths_in_CMakeLists.patch
Patch2:		gnuradio-3.6.1-fix-linkage.patch

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	pygtk2.0-libglade
BuildRequires:	python-cheetah
BuildRequires:	python-lxml
BuildRequires:	python-numpy
BuildRequires:	sdcc
BuildRequires:	swig
BuildRequires:	wxPython
BuildRequires:	xdg-utils
BuildRequires:	xmlto
BuildRequires:	boost-devel
BuildRequires:	libqwtplot3d-devel
BuildRequires:	python-qt4-devel
BuildRequires:	qwt-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(guile-2.0)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(uhd)
## TODO
#BuildRequires:	sphinx

Requires(pre):	shadow-utils

Requires:	%{name}-companion
Requires:	%{name}-doc
Requires:	%{name}-examples
Requires:	%{name}-noaa
Requires:	%{name}-pager
Requires:	%{name}-utils
Requires:	python-%{name}-atsc
Requires:	python-%{name}-core
Requires:	python-%{name}-qtgui
Requires:	python-%{name}-trellis
Requires:	python-%{name}-video-sdl
Requires:	python-%{name}-wxgui
Requires:	python-%{name}-digital
Requires:	python-%{name}-gruel
Requires:	python-%{name}-vocoder
Requires:	python-%{name}-audio
Requires:	python-%{name}-uhd
Requires:	python-%{name}-fcd
Requires:	python-%{name}-wavelet
Requires:	python-%{name}-fft
Requires:	python-%{name}-filter

%description
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual wave forms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

This is a virtual package that installs the entire GNU Radio software set.

%files

#----------------------------------------------------------------------------

%package doc
Summary:	Software Defined Radio
Group:		Communications
BuildArch:	noarch

%description doc
This package contains the documentation for the GNU Radio software
defined radio system.

%files doc
%doc AUTHORS
%doc %{_docdir}/*
%{_datadir}/applications/%{name}-doc.desktop

#----------------------------------------------------------------------------

%package examples
Summary:	GNU Radio Example Programs
Group:		Communications

%description examples
This package provides examples of GNU Radio usage using Python.

%files examples
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/grc

#----------------------------------------------------------------------------

%package -n %{libuhd}
Summary:	GNU Radio UHD package
Group:		System/Libraries

%description -n %{libuhd}
This is the GNU Radio UHD package.

It is the interface to the UHD library to connect to and send and receive data
between the Ettus Research, LLC product line.

%files -n %{libuhd}
%{_libdir}/lib%{name}-uhd*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devuhd}
Summary:	Uhd devel files
Group:		Communications
Requires:	%{libuhd} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devuhd}
This package contains header files needed by developers.

%files -n %{devuhd}
%{_libdir}/pkgconfig/%{name}-uhd.pc
%{_libdir}/lib%{name}-uhd*.so

#----------------------------------------------------------------------------

%package -n %{libdigital}
Summary:	GNU Radio digital modulation blocks
Group:		System/Libraries

%description -n %{libdigital}
This is the gr-digital package.

It contains all of the digital modulation blocks, utilities, and examples.

%files -n %{libdigital}
%{_libdir}/lib%{name}-digital*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devdigital}
Summary:	GNU Radio digital modulation blocks development files
Group:		Communications
Requires:	%{libdigital} = %{EVRD}

%description -n %{devdigital}
This package contains header files needed by developers.

%files -n %{devdigital}
%{_includedir}/%{name}/digital_*.h
%{_libdir}/pkgconfig/%{name}-digital.pc
%{_libdir}/lib%{name}-digital*.so

#----------------------------------------------------------------------------

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

#----------------------------------------------------------------------------

%package -n %{devvolk}
Summary:	GNU Radio Volk devel files
Group:		Communications
Requires:	%{libvolk} = %{EVRD}

%description -n %{devvolk}
This package contains header files needed by developers.

%files -n %{devvolk}
%{_includedir}/volk/*
%{_libdir}/pkgconfig/volk.pc
%{_libdir}/libvolk.so

#----------------------------------------------------------------------------

%package -n %{libatsc}
Summary:	The GNU Radio blocks for ATSC decoding
Group:		System/Libraries

%description -n %{libatsc}
This pacage provides ATSC (HDTV) transmitter and receiver blocks.
Code related to the Advanced Television Standards Committee HDTV
implementation.

%files -n %{libatsc}
%{_libdir}/lib%{name}-atsc*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devatsc}
Summary:	The GNU Radio blocks for ATSC decoding
Group:		Communications
Requires:	%{libatsc} = %{EVRD}

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

#----------------------------------------------------------------------------

%package -n %{libaudio}
Summary:	GNU Radio audio interfaces
Group:		System/Libraries

%description -n %{libaudio}
This package includes all of the supported audio interfaces.

%files -n %{libaudio}
%{_libdir}/lib%{name}-audio*.so.%{major}*
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio-*.conf

#----------------------------------------------------------------------------

%package -n %{devaudio}
Summary:	GNU Radio audio interfaces - devel files
Group:		Communications
Requires:	%{libaudio} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devaudio}
This package contains header files needed by developers.

%files -n %{devaudio}
%{_libdir}/pkgconfig/%{name}-audio.pc
%{_libdir}/lib%{name}-audio*.so


#----------------------------------------------------------------------------

%package -n %{libcore}
Summary:	The GNU Radio Core Library
Group:		System/Libraries

%description -n %{libcore}
This package contains the core GNU Radio libraries.

%files -n %{libcore}
%{_libdir}/lib%{name}-core*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devcore}
Summary:	The GNU Radio Core devel files
Group:		Communications
Requires:	%{libcore} = %{EVRD}

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
%{_includedir}/%{name}/%{name}_swig_bug_workaround.h
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

#----------------------------------------------------------------------------

%package -n %{libvocoder}
Summary:	GNU Radio C++ vocoder blocks
Group:		System/Libraries

%description -n %{libvocoder}
This is the gr-vocoder package.
It contains all available vocoders in GNU Radio.

%files -n %{libvocoder}
%{_libdir}/lib%{name}-vocoder*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devvocoder}
Summary:	GNU Radio vocoder devel files
Group:		Communications
Requires:	%{libvocoder} = %{EVRD}

%description -n %{devvocoder}
This package contains header files needed by developers.

%files -n %{devvocoder}
%{_includedir}/%{name}/vocoder_*.h
%{_libdir}/pkgconfig/%{name}-vocoder.pc
%{_libdir}/lib%{name}-vocoder*.so

#----------------------------------------------------------------------------

%package -n %{libnoaa}
Summary:	GNU Radio C++ block implementing the NOAA
Group:		System/Libraries

%description -n %{libnoaa}
This package provides a NOAA POES HRPT receiver/demodulator block
for GNU Radio.

%files -n %{libnoaa}
%{_libdir}/lib%{name}-noaa*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devnoaa}
Summary:	GNU Radio C++ block implementing the NOAA
Group:		Communications
Requires:	%{libnoaa} = %{EVRD}

%description -n %{devnoaa}
This package contains header files needed by developers.

%files -n %{devnoaa}
%{_includedir}/%{name}/noaa_*.h
%{_libdir}/lib%{name}-noaa*.so
%{_libdir}/pkgconfig/%{name}-noaa.pc

#----------------------------------------------------------------------------

%package -n %{libpager}
Summary:	GNU Radio C++ block implementing the FLEX one-way pager protocol
Group:		System/Libraries

%description -n %{libpager}
This package provides an implementation of the FLEX one-way pager protocol
for GNU Radio.

%files -n %{libpager}
%{_libdir}/lib%{name}-pager*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devpager}
Summary:	GNU Radio C++ block implementing the FLEX one-way pager protocol
Group:		Communications
Requires:	%{libpager} = %{EVRD}

%description -n %{devpager}
This package contains header files needed by developers.

%files -n %{devpager}
%{_includedir}/%{name}/pager*.h
%{_libdir}/pkgconfig/%{name}-pager.pc
%{_libdir}/lib%{name}-pager*.so

#----------------------------------------------------------------------------

%package -n %{libqtgui}
Summary:	GNU Radio C++ blocks fro QT-based GUI applications
Group:		System/Libraries

%description -n %{libqtgui}
This package contains the C++ library for using GNU Radio inside
QT-based GUI applications.

%files -n %{libqtgui}
%{_libdir}/lib%{name}-qtgui*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devqtgui}
Summary:	GNU Radio C++ blocks for QT-based GUI applications
Group:		Communications
Requires:	%{libqtgui} = %{EVRD}

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

#----------------------------------------------------------------------------

%package -n  %{libtrellis}
Summary:	GNU Radio C++ block implementing trellis-coded modulation
Group:		System/Libraries

%description -n %{libtrellis}
This package provides an implementation of tellis-coded modulation
for GNU Radio.

%files -n %{libtrellis}
%{_libdir}/lib%{name}-trellis*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devtrellis}
Summary:	GNU Radio C++ block implementing trellis-coded modulation
Group:		Communications
Requires:	%{libtrellis} = %{EVRD}

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

#----------------------------------------------------------------------------

%package -n %{libvideo_sdl}
Summary:	GNU Radio C++ block implementing video-sdl-coded modulation
Group:		System/Libraries

%description -n %{libvideo_sdl}
This package provides an interface to the SDL rendering library
for GNU Radio.

%files -n %{libvideo_sdl}
%{_libdir}/lib%{name}-video-sdl*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devvideo_sdl}
Summary:	GNU Radio C++ block implementing video-sdl-coded modulation
Group:		Communications
Requires:	%{libvideo_sdl} = %{EVRD}

%description -n %{devvideo_sdl}
This package provides an interface to the SDL rendering library
for GNU Radio.

This package contains header files needed by developers.

%files -n %{devvideo_sdl}
%{_includedir}/%{name}/video_sdl*.h
%{_libdir}/pkgconfig/%{name}-video-sdl.pc
%{_libdir}/lib%{name}-video-sdl*.so

#----------------------------------------------------------------------------

%package -n %{libgruel}
Summary:	GNU Radio Utility Etcetera Library
Group:		System/Libraries

%description -n %{libgruel}
This package implements a variety of low-level utility routines for
GNU Radio.

%files -n %{libgruel}
%{_libdir}/libgruel*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devgruel}
Summary:	GNU Radio Utility Etcetera Library
Group:		Communications
Requires:	%{libgruel} = %{EVRD}

%description -n %{devgruel}
This package implements a variety of low-level utility routines for
GNU Radio.

This package contains header files needed by developers.

%files -n %{devgruel}
%{_includedir}/gruel/*
%{_libdir}/pkgconfig/gruel.pc
%{_libdir}/libgruel*.so

#----------------------------------------------------------------------------

%package -n %{libfcd}
Summary:	Fun Cube Dongle libs
Group:		System/Libraries

%description -n %{libfcd}
Fun Cube Dongle library files.

%files -n %{libfcd}
%{_libdir}/lib%{name}-fcd*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devfcd}
Summary:	Fun Cube Dongle development files
Group:		System/Libraries
Requires:	%{libfcd} = %{EVRD}

%description -n %{devfcd}
This package contains header files needed by developers.

%files -n %{devfcd}
%{_includedir}/%{name}/fcd_api.h
%{_includedir}/%{name}/fcd_source_c.h
%{_libdir}/pkgconfig/%{name}-fcd.pc
%{_libdir}/lib%{name}-fcd*.so

#----------------------------------------------------------------------------

%package -n %{libwavelet}
Summary:	GnuRadio Wavelet
Group:		System/Libraries

%description -n %{libwavelet}
GnuRadio Wavelet module.

%files -n %{libwavelet}
%{_libdir}/lib%{name}-wavelet*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devwavelet}
Summary:	GnuRadio Wavelet development files
Group:		System/Libraries
Requires:	%{libwavelet} = %{EVRD}

%description -n %{devwavelet}
This package contains header files needed by developers.

%files -n %{devwavelet}
%{_includedir}/%{name}/wavelet_*.h
%{_libdir}/lib%{name}-wavelet*.so
%{_libdir}/pkgconfig/%{name}-wavelet.pc

#----------------------------------------------------------------------------

%package -n %{libfft}
Summary:	GnuRadio fft
Group:		System/Libraries

%description -n %{libfft}
GnuRadio fft module.

%files -n %{libfft}
%{_libdir}/lib%{name}-fft*.so.%{major}*

#----------------------------------------------------------------------------

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

#----------------------------------------------------------------------------

%package -n %{libfilter}
Summary:	GnuRadio filters
Group:		System/Libraries

%description -n %{libfilter}
GnuRadio filter module.

%files -n %{libfilter}
%{_libdir}/lib%{name}-filter*.so.%{major}*

#----------------------------------------------------------------------------

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

#----------------------------------------------------------------------------

%package -n python-%{name}-digital
Summary:	Python bindings for GNU Radio digital
Group:		Development/Python
Requires:	python-%{name}-core = %{EVRD}

%description -n python-%{name}-digital
This package contains Python bindings for GNU Radio Digital.

%files -n python-%{name}-digital
%{python_sitearch}/%{name}/digital/*

#----------------------------------------------------------------------------

%package -n python-%{name}-gruel
Summary:	Python bindings for GNU Radio gruel
Group:		Development/Python
Requires:	python-%{name}-core = %{EVRD}

%description -n python-%{name}-gruel
This package contains Python bindings for GNU Radio gruel.

%files -n python-%{name}-gruel
%{python_sitearch}/gruel/*

#----------------------------------------------------------------------------

%package -n python-%{name}-vocoder
Summary:	Python bindings for GNU Radio vocoder
Group:		Development/Python
Requires:	python-%{name}-core = %{EVRD}

%description -n python-%{name}-vocoder
This package contains Python bindings for GNU Radio ATSC decoding.

%files -n python-%{name}-vocoder
%{python_sitearch}/%{name}/vocoder/*

#----------------------------------------------------------------------------

%package -n python-%{name}-atsc
Summary:	Python bindings for GNU Radio ATSC decoding
Group:		Development/Python
Requires:	python-%{name}-core = %{EVRD}

%description -n python-%{name}-atsc
This package contains Python bindings for GNU Radio ATSC decoding.
Code related to the Advanced Television Standards Committee HDTV
implementation.

%files -n python-%{name}-atsc
%{python_sitearch}/%{name}/_atsc.*
%{python_sitearch}/%{name}/atsc.*

#----------------------------------------------------------------------------

%package -n python-%{name}-audio
Summary:	GNU Radio Python Audio Driver
Group:		Development/Python
Requires:	python-%{name}-core = %{EVRD}

%description -n python-%{name}-audio
This package provides the Python interface to the GNU Radio driver for the
audio system.

%files -n python-%{name}-audio
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio.conf
%{python_sitearch}/%{name}/audio/*

#----------------------------------------------------------------------------

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

%description -n python-%{name}-core
This package provides the modules that enable one to use gnuradio from
Python scripts.

%files -n python-%{name}-core
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/%{name}-core.conf
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

#----------------------------------------------------------------------------

%package -n python-%{name}-qtgui
Summary:	GNU Radio Graphical Interface Routines based on QT
Group:		Development/Python
Requires:	python-%{name}-core = %{EVRD}

%description -n python-%{name}-qtgui
This package provides the Python wrappers around the GNU Radio QT GUI
C++ blocks.

%files -n python-%{name}-qtgui
%{python_sitearch}/%{name}/qtgui

#----------------------------------------------------------------------------

%package -n python-%{name}-trellis
Summary:	GNU Radio Trellis-Coded Modulation library
Group:		Development/Python
Requires:	python-%{name}-core = %{EVRD}

%description -n python-%{name}-trellis
This package provides an implementation of trellis-coded modulation for
GNU Radio.

%files -n python-%{name}-trellis
%{python_sitearch}/%{name}/_trellis.*
%{python_sitearch}/%{name}/trellis.*

#----------------------------------------------------------------------------

%package -n python-%{name}-uhd
Summary:	Python bindings for GNU Radio uhd driver
Group:		Development/Python
Requires:	python-%{name}-core = %{EVRD}

%description -n python-%{name}-uhd
This package provides the Python interface to the GNU Radio uhd driver
and daughterboard drivers.

%files -n python-%{name}-uhd
%{python_sitearch}/%{name}/uhd

#----------------------------------------------------------------------------

%package -n python-%{name}-video-sdl
Summary:	GNU Radio SDL Interface Library
Group:		Development/Python
Requires:	python-%{name}-core = %{EVRD}

%description -n python-%{name}-video-sdl
This package provides an interface to the SDL rendering library for GNU Radio.

%files -n python-%{name}-video-sdl
%{python_sitearch}/%{name}/_video_sdl.*
%{python_sitearch}/%{name}/video_sdl.*

#----------------------------------------------------------------------------

%package -n python-%{name}-wxgui
Summary:	GNU Radio GUI Routines based on wxPython
Group:		Development/Python
Requires:	python-%{name}-core = %{EVRD}
Requires:	python-numpy
Requires:	python-opengl

%description -n python-%{name}-wxgui
This package provides high level GUI
construction classes based upon the wxPython bindings 
for wxWidgets.

%files -n python-%{name}-wxgui
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-wxgui.conf
%{python_sitearch}/%{name}/wxgui

#----------------------------------------------------------------------------

%package -n python-%{name}-fcd
Summary:	GNU Radio Fun Cube Dongle
Group:		Development/Python

%description -n python-%{name}-fcd
GNU Radio Fun Cube Dongle

%files -n python-%{name}-fcd
%{python_sitearch}/%{name}/fcd

#----------------------------------------------------------------------------

%package -n python-%{name}-wavelet
Summary:	GNU Radio wavelet
Group:		Development/Python

%description -n python-%{name}-wavelet
GNU Radio wavelet.

%files -n python-%{name}-wavelet
%{python_sitearch}/%{name}/wavelet

#----------------------------------------------------------------------------

%package -n python-%{name}-fft
Summary:	GNU Radio fft
Group:		Development/Python

%description -n python-%{name}-fft
GNU Radio fft

%files -n python-%{name}-fft
%{python_sitearch}/%{name}/fft
%{python_sitearch}/%{name}/plot_fft_base.*

#----------------------------------------------------------------------------

%package -n python-%{name}-filter
Summary:	GNU Radio filter
Group:		Development/Python

%description -n python-%{name}-filter
GNU Radio filter

%files -n python-%{name}-filter
%{python_sitearch}/%{name}/filter

#----------------------------------------------------------------------------

%package companion
Summary:	The GNU Radio Companion
Group:		Communications
Requires:	python-%{name}-core = %{EVRD}
Requires:	python-cheetah
Requires:	pygtk2.0
Requires:	python-lxml

%description companion
GRC is a graphical flowgraph editor for the GNU Software Radio.

%files companion
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/grc.conf
%{_bindir}/%{name}-companion
%{_datadir}/applications/%{name}-grc.desktop
%{_datadir}/mime/application/*.xml
%{_iconsdir}/hicolor/*/apps/%{name}-grc.png
%{_datadir}/%{name}/grc
%{python_sitearch}/%{name}/grc
%{python_sitearch}/grc_%{name}

#----------------------------------------------------------------------------

%package  noaa
Summary:	GNU Radio NOAA POES HRPT receiver
Group:		Communications
Requires:	python-%{name}-core = %{EVRD}

%description noaa
This package provides and implements an NOAA POES HRPT receiver.

%files noaa
%{python_sitearch}/%{name}/noaa

#----------------------------------------------------------------------------

%package pager
Summary:	GNU Radio FLEX Pager Decoder
Group:		Communications
Requires:	python-%{name}-uhd = %{EVRD}

%description pager
This package provides a decoder for the FLEX paging protocol for GNU Radio.

%files pager
%{_bindir}/usrp_flex*
%{python_sitearch}/%{name}/pager

#----------------------------------------------------------------------------

%package utils
Summary:	GNU Radio Utilities
Group:		Communications
Requires:	python-%{name}-wxgui = %{EVRD}
Requires:	python-matplotlib
Requires:	python-scipy
Requires:	python-qt4

%description utils
This package provides commonly used utilities for GNU Radio.

%files utils
%{python_sitearch}/%{name}/plot_data.*
%{python_sitearch}/%{name}/pyqt_filter.*
%{python_sitearch}/%{name}/pyqt_plot.*
%{_bindir}/%{name}-config-info
# This should really be in a devel package
%{_libdir}/pkgconfig/gr-wxgui.pc

## TODO Where do these live?
%{_bindir}/gr_filter_design
%{_bindir}/gr_plot_*
%{_bindir}/uhd_*
%{python_sitearch}/%{name}/gr_xmlrunner.*
%{python_sitearch}/%{name}/plot_psd_base.*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .gnuradio-3.6.2-mga-fix_install_paths_in_CMakeLists.patch
%patch2 -p1 -b .gnuradio-3.6.1-fix-linkage.patch

%build
%cmake
make

%install
%makeinstall_std -C build

#icons
for i in 32 48 64 128 256; do
	install -Dpm0644 %{buildroot}%{_datadir}/%{name}/grc/freedesktop/grc-icon-${i}.png \
		%{buildroot}/%{_iconsdir}/hicolor/${i}x${i}/apps/%{name}-grc.png
done

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
Categories=System;Documentation;
X-Desktop-File-Install-Version=0.19
EOF

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{name}-doc.desktop

desktop-file-install \
--set-key=Name \
--set-value='Gnu Radio Companion' \
--dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/%{name}/grc/freedesktop/%{name}-grc.desktop

#we don't want these
rm -rf %{buildroot}%{_bindir}/create-%{name}-out-of-tree-project
rm -rf %{buildroot}%{_libdir}/%{name}/grc_setup_freedesktop
rm -rf %{buildroot}/%{_datadir}/%{name}/grc/freedesktop

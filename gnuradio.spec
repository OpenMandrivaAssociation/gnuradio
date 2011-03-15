# TODO:
# - better summaries and descriptions
# - maybe some more?!

Name:           gnuradio
Version:        3.3.0
Release:        %mkrel 12
Summary:        Software defined radio framework
Group:          Networking/Other 
License:        GPLv3+
URL:            http://www.gnuradio.org
Source0:        ftp://ftp.gnu.org/gnu/gnuradio/gnuradio-%{version}.tar.gz
Patch0:		gnuradio-3.3.0-fix_pkgconfig_cflags.patch
Patch1:		gnuradio-3.3.0-usrpgccpatch.patch
BuildRequires:	cppunit-devel
BuildRequires:	doxygen
BuildRequires:	fftw-devel
BuildRequires:	graphviz
BuildRequires:	xdg-utils
BuildRequires:	guile
BuildRequires:	libSDL-devel
BuildRequires:	libboost-devel
BuildRequires:	libgsl-devel
BuildRequires:	libjack-devel
BuildRequires:	libomniorb
BuildRequires:	libportaudio-devel
BuildRequires:	libqwt-devel
BuildRequires:	libusb-devel
BuildRequires:	libwxgtk2.8-devel
BuildRequires:	libqwt-devel
BuildRequires:	libqwtplot3d-devel
BuildRequires:	ltp
BuildRequires:	pygtk2.0-libglade
BuildRequires:	python-devel
BuildRequires:	python-cheetah
BuildRequires:	python-lxml
BuildRequires:	python-numpy
BuildRequires:	python-qt4-devel
BuildRequires:	python-qwt

%if %{mdkversion} >= 201100
BuildRequires:	sdcc2.9
BuildRequires:	libalsa-oss-devel
%else
BuildRequires:	sdcc
BuildRequires:	%{_lib}alsa-oss-devel
%endif

BuildRequires:	swig
BuildRequires:	wxPython
BuildRequires:	xmlto

%description
GNU Radio is a collection of software that when combined with minimal 
hardware, allows the construction of radios where the actual waveforms 
transmitted and received are defined by software. What this means is 
that it turns the digital modulation schemes used in today's high 
performance wireless devices into software problems.

############################
%package -n usrp-doc
Summary:        Universal Software Radio Peripheral
Group:          Networking/Other

%description -n usrp-doc
Gnu Radio Universal Software Radio Peripheral documentation.

%files -n usrp-doc
%defattr(-,root,root,-)
%doc usrp-docs/*

############################
%package doc
Summary:	Software Defined Radio
Group:		Networking/Other

%description doc
This package contains the documentation for the GNU Radio software
defined radio system.

%files doc
%defattr(-,root,root,-)
%doc ChangeLog NEWS AUTHORS
%doc gnuradio-docs/*

############################
%package examples
Summary:	GNU Radio Example Programs
Group:		Networking/Other

%description examples
This package provides examples of GNU Radio usage using Python.

%files examples
%defattr(-,root,root,-)
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/grc

############################
%package -n usrp-firmware
Summary:	Control applications and firmware for the USRP
Group:		Networking/Other

%description -n usrp-firmware
The Universal Software Radio Peripheral (USRP) is an USB-connected,
low-cost and open board. It features four high-speed analog-to-digital
and digital-to-analog converters, an FPGA and a microcontroller. It's
ideal for capturing or transmitting various signals, usually in combination
with GNU Radio. The design schemas are available under a free license.

This package contains the basic FPGA bitstrings for normal USRP
operation.

%files -n usrp-firmware
%defattr(-,root,root)
%{_datadir}/usrp

############################
############################
#
# Lib and devel packages
#
############################
############################

%define major	0

##############
#libusrp0
%define	libusrp		%mklibname usrp	%{major}
%define devusrp		%mklibname usrp -d

%package -n %{libusrp}
Summary:	Client side library for the USRP(1) hardware
Group:		System/Libraries

%description -n %{libusrp}
The Universal Software Radio Peripheral (USRP) is an USB-connected,
low-cost and open board. It features four high-speed analog-to-digital
and digital-to-analog converters, an FPGA and a microcontroller. It's
ideal for capturing or transmitting various signals, usually in
combination with GNU Radio. The design schemas are available under a
free license.

This package contains the client-side library, providing an easy interface
for communicating with the USRP.

%files -n %{libusrp}
%defattr(-,root,root)
%{_libdir}/libusrp*.so.%{major}*

##############
%package -n %{devusrp}
Summary:	Client side library for the USRP(1) hardware
Group:		Development/Other
Requires:	%{libusrp} = %{version}-%{release}
Obsoletes:	usrp-devel < %{version}-%{release}
Provides:	usrp-devel = %{version}-%{release}

%description -n %{devusrp}
The Universal Software Radio Peripheral (USRP) is an USB-connected,
low-cost and open board. It features four high-speed analog-to-digital
and digital-to-analog converters, an FPGA and a microcontroller. It's
ideal for capturing or transmitting various signals, usually in
combination with GNU Radio. The design schemas are available under a
free license.

This package contains the client-side library, providing an easy interface
for communicating with the USRP.

This package contains header files needed by developers.

%files -n %{devusrp}
%defattr(-,root,root)
%{_includedir}/usrp
%{_libdir}/pkgconfig/usrp.pc
%{_libdir}/libusrp.so

############################
#libusrp2_0
%define libusrp2	%mklibname usrp 2 %{major}
%define devusrp2	%mklibname usrp 2 -d

%package -n %{libusrp2}
Summary:	Client side library for the USRP2 hardware
Group:		System/Libraries

%description -n %{libusrp2}
The Universal Software Radio Peripheral 2 (USRP2) is a GbE-connected,
low-cost and open board. It features two high-speed analog-to-digital
and digital-to-analog converters, an FPGA and a microcontroller. It's
ideal for capturing or transmitting various signals, usually in
combination with GNU Radio. The design schemas are available under a
free license.

This package contains the client-side C++ library, providing the low-
level (non-GNU Radio) hardware interface.

%files -n %{libusrp2}
%defattr(-,root,root)
%{_libdir}/libusrp2*.so.%{major}*

##############
%package -n %{devusrp2}
Summary:	Client side library for the USRPhardware 2
Group:		Development/Other
Requires:	%{libusrp2} = %{version}-%{release}
Provides:	usrp2-devel = %{version}-%{release}

%description -n %{devusrp2}
The Universal Software Radio Peripheral 2 (USRP2) is a GbE-connected,
low-cost and open board. It features two high-speed analog-to-digital
and digital-to-analog converters, an FPGA and a microcontroller. It's
ideal for capturing or transmitting various signals, usually in
combination with GNU Radio. The design schemas are available under a
free license.

This package contains the client-side C++ library, providing the low-
level (non-GNU Radio) hardware interface.

This package contains header files needed by developers.

%files -n %{devusrp2}
%defattr(-,root,root)
%{_includedir}/usrp2
%{_libdir}/pkgconfig/usrp2.pc
%{_libdir}/libusrp2.so

############################
#libgnuradio-atsc0
%define libatsc		%mklibname %{name}-atsc %{major}
%define devatsc		%mklibname %{name}-atsc -d

%package -n %{libatsc}
Summary:	The GNU Radio blocks for ATSC decoding
Group:		System/Libraries

%description -n %{libatsc}
This pacage provides ATSC (HDTV) transmitter and receiver blocks.

%files -n %{libatsc}
%defattr(-,root,root)
%{_libdir}/lib%{name}-atsc*.so.%{major}*

##############
%package -n %{devatsc}
Summary:	The GNU Radio blocks for ATSC decoding
Group:		Development/Other
Requires:	%{libatsc} = %{version}-%{release}

%description -n %{devatsc}
This package provides ATSC (HDTV) transmitter and receiver blocks.

This package contains header files needed by developers.

%files -n %{devatsc}
%defattr(-,root,root)
%{_includedir}/%{name}/atsc_*.h
%{_includedir}/%{name}/atsci_*.h
%{_includedir}/%{name}/create_atsci_*.h
%{_includedir}/%{name}/qa_atsci*.h
%{_libdir}/pkgconfig/%{name}-atsc.pc
%{_libdir}/lib%{name}-atsc.so

##############
#libgnuradio-audio-alsa0
%define libalsa		%mklibname %{name}-audio-alsa %{major}
%define devalsa		%mklibname %{name}-audio-alsa -d

%package -n %{libalsa}
Summary:	GNU Radio C++ block for ALSA sound system
Group:		System/Libraries

%description -n %{libalsa}
This package contains the ALSA sound system driver for GNU Radio.

%files -n %{libalsa}
%defattr(-,root,root)
%{_libdir}/lib%{name}-audio-alsa*.so.%{major}*

##############
%package -n %{devalsa}
Summary:	GNU Radio C++ block for ALSA sound system
Group:		Development/Other
Requires:	%{libalsa} = %{version}-%{release}

%description -n %{devalsa}
This package contains the ALSA sound system driver for GNU Radio.

This package contains header files needed by developers.

%files -n %{devalsa}
%defattr(-,root,root)
%{_includedir}/%{name}/audio_alsa*.h
%{_libdir}/pkgconfig/%{name}-audio-alsa.pc
%{_libdir}/lib%{name}-audio-alsa.so

############################
#libgnuradio-audio-jack0
%define libjack		%mklibname %{name}-audio-jack %{major}
%define devjack		%mklibname %{name}-audio-jack -d

%package -n %{libjack}
Summary:	GNU Radio C++ block for JACK sound system
Group:		System/Libraries

%description -n %{libjack}
This package contains the JACK sound system driver for GNU Radio.

%files -n %{libjack}
%defattr(-,root,root)
%{_libdir}/lib%{name}-audio-jack*.so.%{major}*

##############
%package -n %{devjack}
Summary:	GNU Radio C++ block for JACK sound system
Group:		Development/Other
Requires:	%{libjack} = %{version}-%{release}

%description -n %{devjack}
This package contains the JACK sound system driver for GNU Radio.

This package contains header files needed by developers.

%files -n %{devjack}
%defattr(-,root,root)
%{_includedir}/%{name}/audio_jack*.h
%{_libdir}/pkgconfig/%{name}-audio-jack.pc
%{_libdir}/lib%{name}-audio-jack.so

############################
#libgnuradio-audio-portaudio0
%define libportaudio	%mklibname %{name}-audio-portaudio %{major}
%define devportaudio	%mklibname %{name}-audio-portaudio -d

%package -n %{libportaudio}
Summary: 	GNU Radio C++ block for PORTAUDIO sound system
Group:		System/Libraries

%description -n %{libportaudio}
This package contains the PORTAUDIO sound system driver for GNU Radio.

%files -n %{libportaudio}
%defattr(-,root,root)
%{_libdir}/lib%{name}-audio-portaudio*.so.%{major}*

##############
%package -n %{devportaudio}
Summary: 	GNU Radio C++ block for PORTAUDIO sound system
Group:		Development/Other
Requires:	%{libportaudio} = %{version}-%{release}

%description -n %{devportaudio}
This package contains the PORTAUDIO sound system driver for GNU Radio.

This package contains header files needed by developers.

%files -n %{devportaudio}
%defattr(-,root,root)
%{_includedir}/%{name}/audio_portaudio*.h
%{_libdir}/pkgconfig/%{name}-audio-portaudio.pc
%{_libdir}/lib%{name}-audio-portaudio.so

############################
#libgnuradio-core0
%define libcore		%mklibname %{name}-core %{major}
%define devcore		%mklibname %{name}-core -d

%package -n %{libcore}
Summary:	The GNU Sofware Radio Core Library
Group:		System/Libraries

%description -n %{libcore}
This package contains the core GNU Radio libraries.

%files -n %{libcore}
%defattr(-,root,root)
%{_libdir}/lib%{name}-core*.so.%{major}*

##############
%package -n %{devcore}
Summary:	The GNU Software Radio Core Library
Group:		Development/Other
Requires:	%{libcore} = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devcore}
This package contains the core GNU Radio libraries.

This package contains header files needed by developers.

%files -n %{devcore}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/ccomplex_*.h
%{_includedir}/%{name}/complex_*.h
%{_includedir}/%{name}/fcomplex*.h
%{_includedir}/%{name}/float_dotprod*.h
%{_includedir}/%{name}/gnuradio_swig_bug_workaround.h
%{_includedir}/%{name}/gr_*.h
%{_includedir}/%{name}/gri_*.h
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
%{_libdir}/pkgconfig/%{name}-core.pc
%{_libdir}/lib%{name}-core.so
#
# Not sure for these files, may be in a wrong package
#
%{_includedir}/%{name}/base.h
%{_includedir}/%{name}/convolutional_interleaver.h
%{_includedir}/%{name}/fpll_btloop_coupling.h
%{_includedir}/%{name}/fsm.h
%{_includedir}/%{name}/interleaver.h
%{_includedir}/%{name}/interleaver_fifo.h
%{_includedir}/%{name}/qa_convolutional_interleaver.h
%{_includedir}/%{name}/qa_interleaver_fifo.h
%{_includedir}/%{name}/quicksort_index.h

############################
#libgnuradio-cvsd-vocoder0
%define libcvsd_vocoder	%mklibname %{name}-cvsd-vocoder %{major}
%define devcvsd_vocoder	%mklibname %{name}-cvsd-vocoder -d

%package -n %{libcvsd_vocoder}
Summary:	GNU Radio C++ block implementing the CVSD vocoder
Group:		System/Libraries

%description -n %{libcvsd_vocoder}
This package provides an implementation of a CVSD vocoder for GNU Radio.

%files -n %{libcvsd_vocoder}
%defattr(-,root,root)
%{_libdir}/lib%{name}-cvsd-vocoder*.so.%{major}*

##############
%package -n %{devcvsd_vocoder}
Summary:	GNU Radio C++ block implementing the CVSD vocoder
Group:		Development/Other
Requires:	%{libcvsd_vocoder} = %{version}-%{release}

%description -n %{devcvsd_vocoder}
This package provides an implementation of a CVSD vocoder for GNU Radio.

This package contains header files needed by developers.

%files -n %{devcvsd_vocoder}
%defattr(-,root,root)
%{_includedir}/%{name}/cvsd_*.h
%{_libdir}/pkgconfig/%{name}-cvsd-vocoder.pc
%{_libdir}/lib%{name}-cvsd-vocoder.so

############################
#libgnuradio-gsm-fr-vocoder0
%define libgsm_fr_vocoder	%mklibname %{name}-gsm-fr-vocoder %{major}
%define devgsm_fr_vocoder	%mklibname %{name}-gsm-fr-vocoder -d

%package -n %{libgsm_fr_vocoder}
Summary:	GNU Radio C++ block implementing the GSM full rate vocoder
Group:		System/Libraries

%description -n %{libgsm_fr_vocoder}
This package provides an implementation of a GSM-FR vocoder for GNU Radio.

%files -n %{libgsm_fr_vocoder}
%defattr(-,root,root)
%{_libdir}/lib%{name}-gsm-fr-vocoder*.so.%{major}*

##############
%package -n %{devgsm_fr_vocoder}
Summary:	GNU Radio C++ block implementing the GSM full rate vocoder
Group:		Development/Other
Requires:	%{libgsm_fr_vocoder} = %{version}-%{release}

%description -n %{devgsm_fr_vocoder}
This package provides an implementation of a GSM-FR vocoder for GNU Radio.

This package contains header files needed by developers.

%files -n %{devgsm_fr_vocoder}
%defattr(-,root,root)
%{_includedir}/%{name}/gsm_fr_*.h
%{_libdir}/pkgconfig/%{name}-gsm-fr-vocoder.pc
%{_libdir}/lib%{name}-gsm-fr-vocoder.so

############################
#libgnuradio-msdd6000_0
%define libmsdd6000	%mklibname %{name}-msdd 6000 %{major}
%define devmsdd6000	%mklibname %{name}-msdd 6000 -d

%package -n %{libmsdd6000}
Summary:	GNU Radio blocks for the Softronics MSDD 6000
Group:		System/Libraries

%description -n %{libmsdd6000}
This package provides an interface block between the Softronics MSDD6000
and GNU Radio.

%files -n %{libmsdd6000}
%defattr(-,root,root)
%{_libdir}/lib%{name}-msdd6000-*.so.%{major}*
%{_libdir}/lib%{name}-msdd6000_rs*.so.%{major}*

##############
%package -n %{devmsdd6000}
Summary:	GNU Radio blocks for the Softronics MSDD 6000
Group:		Development/Other
Requires:	%{libmsdd6000} = %{version}-%{release}

%description -n %{devmsdd6000}
This package provides an interface block between the Softronics MSDD6000
and GNU Radio.

This package contains header files needed by developers.

%files -n %{devmsdd6000}
%defattr(-,root,root)
%{_includedir}/%{name}/msdd6000.h
%{_includedir}/%{name}/msdd6000_rs.h
%{_includedir}/%{name}/msdd_*.h
%{_libdir}/lib%{name}-msdd6000.so
%{_libdir}/lib%{name}-msdd6000_rs.so
%{_libdir}/pkgconfig/%{name}-msdd6000.pc

############################
#libgnuradio-noaa0
%define libnoaa		%mklibname %{name}-noaa %{major}
%define devnoaa		%mklibname %{name}-noaa -d

%package -n %{libnoaa}
Summary:	GNU Radio C++ block implementing the NOAA
Group:		System/Libraries

%description -n %{libnoaa}
This package provides a NOAA POES HRPT receiver/demodulator block
for GNU Radio.
 
%files -n %{libnoaa}
%defattr(-,root,root)
%{_libdir}/lib%{name}-noaa*.so.%{major}*

##############
%package -n %{devnoaa}
Summary:	GNU Radio C++ block implementing the NOAA
Group:		Development/Other
Requires:	%{libnoaa} = %{version}-%{release}

%description -n %{devnoaa}
This package provides a NOAA POES HRPT receiver/demodulator block
for GNU Radio.

This package contains header files needed by developers.

%files -n %{devnoaa}
%defattr(-,root,root)
%{_includedir}/%{name}/noaa_*.h
%{_libdir}/lib%{name}-noaa.so

############################
#libgnuradio-pager0
%define libpager	%mklibname %{name}-pager %{major}
%define devpager	%mklibname %{name}-pager -d

%package -n %{libpager}
Summary:	GNU Radio C++ block implementing the FLEX one-way pager protocol
Group:		System/Libraries

%description -n %{libpager}
This package provides an implementation of the FLEX one-way pager protocol
for GNU Radio.

%files -n %{libpager}
%defattr(-,root,root)
%{_libdir}/lib%{name}-pager*.so.%{major}*

##############
%package -n %{devpager}
Summary:	GNU Radio C++ block implementing the FLEX one-way pager protocol
Group:		Development/Other
Requires:	%{libpager} = %{version}-%{release}

%description -n %{devpager}
This package provides an implementation of the FLEX one-way pager protocol
for GNU Radio.

This package contains header files needed by developers.

%files -n %{devpager}
%defattr(-,root,root)
%{_includedir}/%{name}/pager*.h
%{_libdir}/pkgconfig/%{name}-pager.pc
%{_libdir}/lib%{name}-pager.so

############################
#libgnuradio-qtgui0
%define libqtgui	%mklibname %{name}-qtgui %{major}
%define devqtgui	%mklibname %{name}-qtgui -d

%package -n %{libqtgui}
Summary:	GNU Radio C++ blocks fro QT-based GUI applications
Group:		System/Libraries

%description -n %{libqtgui}
This package contains the C++ library for using GNU Radio inside
QT-based GUI applications.

%files -n %{libqtgui}
%defattr(-,root,root)
%{_libdir}/lib%{name}-qtgui*.so.%{major}*

##############
%package -n %{devqtgui}
Summary:	GNU Radio C++ blocks fro QT-based GUI applications
Group:		Development/Other
Requires:	%{libqtgui} = %{version}-%{release}

%description -n %{devqtgui}
This package contains the C++ library for using GNU Radio inside
QT-based GUI applications.

This package contains header files needed by developers.

%files -n %{devqtgui}
%defattr(-,root,root)
%{_includedir}/%{name}/ConstellationDisplayPlot.h
%{_includedir}/%{name}/FrequencyDisplayPlot.h
%{_includedir}/%{name}/SpectrumGUIClass.h
%{_includedir}/%{name}/TimeDomainDisplayPlot.h
%{_includedir}/%{name}/Waterfall3DDisplayPlot.h
%{_includedir}/%{name}/WaterfallDisplayPlot.h
%{_includedir}/%{name}/highResTimeFunctions.h
%{_includedir}/%{name}/plot_waterfall.h
%{_includedir}/%{name}/qtgui*.h
%{_includedir}/%{name}/spectrumUpdateEvents.h
%{_includedir}/%{name}/spectrumdisplayform.h
%{_includedir}/%{name}/waterfallGlobalData.h
%{_libdir}/lib%{name}-qtgui.so

############################
#libgnuradio-trellis0
%define libtrellis	%mklibname %{name}-trellis %{major}
%define devtrellis	%mklibname %{name}-trellis -d

%package -n  %{libtrellis}
Summary:	GNU Radio C++ block implementing trellis-coded modulation
Group:		System/Libraries

%description -n %{libtrellis}
This package provides an implementation of tellis-coded modulation
for GNU Radio.

%files -n %{libtrellis}
%defattr(-,root,root)
%{_libdir}/lib%{name}-trellis*.so.%{major}*

##############
%package -n %{devtrellis}
Summary:	GNU Radio C++ block implementing trellis-coded modulation
Group:		Development/Other
Requires:	%{libtrellis} = %{version}-%{release}

%description -n %{devtrellis}
This package provides an implementation of trellis-coded modulation
for GNU Radio.

This package contains header files needed by developers.

%files -n %{devtrellis}
%defattr(-,root,root)
%{_includedir}/%{name}/trellis*.h
%{_libdir}/pkgconfig/%{name}-trellis.pc
%{_libdir}/lib%{name}-trellis.so

############################
#libgnuradio-usrp0
%define libgnu_usrp	%mklibname %{name}-usrp %{major}
%define devgnu_usrp	%mklibname %{name}-usrp -d

%package -n %{libgnu_usrp}
Summary:	GNU Radio C++ blocks for USRP(1) hardware
Group:		System/Libraries

%description -n %{libgnu_usrp}
This package contains the C++ API blocks for the Universal Software Radio
Peripheral.

%files -n %{libgnu_usrp}
%defattr(-,root,root)
%{_libdir}/lib%{name}-usrp*.so.%{major}*

##############
%package -n %{devgnu_usrp}
Summary:	GNU Radio C++ blocks for USRP(1) hardware
Group:		Development/Other
Requires:	%{libgnu_usrp} = %{version}-%{release}

%description -n %{devgnu_usrp}
This package contains the C++ API blocks for the Universal Software Radio
Peripheral.

This package contains header files needed by developers.

%files -n %{devgnu_usrp}
%defattr(-,root,root)
%{_includedir}/%{name}/usrp_*.h
%{_libdir}/pkgconfig/%{name}-usrp.pc
%{_libdir}/lib%{name}-usrp.so

############################
#libgnuradio-usrp2_0
%define libgnu_usrp2	%mklibname %{name}-usrp 2 %{major}
%define devgnu_usrp2	%mklibname %{name}-usrp 2 -d

%package -n %{libgnu_usrp2}
Summary:	GNU Radio C++ blocks for USRP2 hardware
Group:		System/Libraries

%description -n %{libgnu_usrp2}
This package contains the C++ API blocks for the Universal Software Radio
Peripheral 2.

%files -n %{libgnu_usrp2}
%defattr(-,root,root)
%{_libdir}/lib%{name}-usrp2*.so.%{major}*

##############
%package -n %{devgnu_usrp2}
Summary:	GNU Radio C++ blocks for USRP2 hardware
Group:		Development/Other
Requires:	%{libgnu_usrp2} = %{version}-%{release}

%description -n %{devgnu_usrp2}
This package contains the C++ API blocks for the Universal Software Radio
Peripheral 2.

This package contains header files needed by developers.

%files -n %{devgnu_usrp2}
%defattr(-,root,root)
%{_includedir}/%{name}/usrp2_*.h
%{_libdir}/pkgconfig/%{name}-usrp2.pc
%{_libdir}/lib%{name}-usrp2.so

############################
#libgnuradio-video-sdl0
%define libvideo_sdl	%mklibname %{name}-video-sdl %{major}
%define devvideo_sdl	%mklibname %{name}-video-sdl -d

%package -n %{libvideo_sdl}
Summary:	GNU Radio C++ block implementing video-sdl-coded modulation
Group:		System/Libraries

%description -n %{libvideo_sdl}
This package provides an interface to the SDL rendering library
for GNU Radio.

%files -n %{libvideo_sdl}
%defattr(-,root,root)
%{_libdir}/lib%{name}-video-sdl*.so.%{major}*

##############
%package -n %{devvideo_sdl}
Summary:	GNU Radio C++ block implementing video-sdl-coded modulation
Group:		Development/Other
Requires:	%{libvideo_sdl} = %{version}-%{release}

%description -n %{devvideo_sdl}
This package provides an interface to the SDL rendering library
for GNU Radio.

This package contains header files needed by developers.

%files -n %{devvideo_sdl}
%defattr(-,root,root)
%{_includedir}/%{name}/video_sdl*.h
%{_libdir}/pkgconfig/%{name}-video-sdl.pc
%{_libdir}/lib%{name}-video-sdl.so

############################
#libgruel0
%define libgruel	%mklibname gruel %{major}
%define devgruel	%mklibname gruel -d

%package -n %{libgruel}
Summary:	GNU Radio Utility Etcetera Library
Group:		System/Libraries

%description -n %{libgruel}
This package implements a variety of low-level utility routines for
GNU Radio.

%files -n %{libgruel}
%defattr(-,root,root)
%{_libdir}/libgruel*.so.%{major}*

##############
%package -n %{devgruel}
Summary:	GNU Radio Utility Etcetera Library
Group:		Development/Other
Requires:	%{libgruel} = %{version}-%{release}

%description -n %{devgruel}
This package implements a variety of low-level utility routines for
GNU Radio.

This package contains header files needed by developers.

%files -n %{devgruel}
%defattr(-,root,root)
%{_includedir}/gruel
%{_libdir}/pkgconfig/gruel.pc
%{_libdir}/libgruel.so

############################

############################
############################
#
# Python packages
#
############################
############################

%package -n python-%{name}-atsc
Summary:	Python bindings for GNU Radio ATSC decoding
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-atsc
This package contains Python bindings for GNU Radio ATSC decoding.

%files -n python-%{name}-atsc
%defattr(-,root,root)
%{python_sitearch}/%{name}/_atsc.*
%{python_sitearch}/%{name}/atsc.*

############################
%package -n python-%{name}-audio-alsa
Summary:	Python bindings for GNU Radio ALSA audio driver
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-audio-alsa
This package provides the Python wrappers around the GNU Radio ALSA audio
driver.

%files -n python-%{name}-audio-alsa
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio-alsa.conf
%{python_sitearch}/%{name}/_audio_alsa.*
%{python_sitearch}/%{name}/audio_alsa.*

############################
%package -n python-%{name}-audio-jack
Summary:	GNU Radio Python JACK Audio Driver
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-audio-jack
This package provides the Python interface to the GNU Radio driver for the
JACK audio system.

%files -n python-%{name}-audio-jack
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio-jack.conf
%{python_sitearch}/%{name}/_audio_jack.*
%{python_sitearch}/%{name}/audio_jack.*

############################
%package -n python-%{name}-audio-portaudio
Summary:	GNU Radio Python PortAudio Driver
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-audio-portaudio
This package provides the Python interface to the GNU Radio driver for the
PortAudio audio system.

%files -n python-%{name}-audio-portaudio
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-audio-portaudio.conf
%{python_sitearch}/%{name}/_audio_portaudio.*
%{python_sitearch}/%{name}/audio_portaudio.*

############################
%package -n python-%{name}-core
Summary:	Python bindings for GNU Radio core library
Group:		Development/Python
Requires:	python-numpy

%description -n python-%{name}-core
This package provides the modules that enable one to use gnuradio from
Python scripts.

%files -n python-%{name}-core
%defattr(-,root,root)
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gnuradio-core.conf
%dir %{python_sitearch}/%{name}
%{python_sitearch}/%{name}/blks2
%{python_sitearch}/%{name}/blks2impl
%{python_sitearch}/%{name}/gr
%{python_sitearch}/%{name}/gru
%{python_sitearch}/%{name}/gruimpl
%dir %{python_sitearch}/%{name}/vocoder
%{python_sitearch}/%{name}/vocoder/__init__.*
%{python_sitearch}/%{name}/__init__.*
%{python_sitearch}/%{name}/audio.*
%{python_sitearch}/%{name}/eng_notation.*
%{python_sitearch}/%{name}/eng_option.*
%{python_sitearch}/%{name}/gr_unittest.*
%{python_sitearch}/%{name}/modulation_utils*.*
%{python_sitearch}/%{name}/ofdm_packet_utils.*
%{python_sitearch}/%{name}/optfir.*
%{python_sitearch}/%{name}/packet_utils.*
%{python_sitearch}/%{name}/usrp_options.*
%{python_sitearch}/%{name}/window.*

############################
%package -n python-%{name}-cvsd-vocoder
Summary:	GNU Radio CVSD Vocoder
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-cvsd-vocoder
This package provides an implementation of a CVSD vocoder for GNU Radio.

%files -n python-%{name}-cvsd-vocoder
%defattr(-,root,root)
%{python_sitearch}/%{name}/vocoder/_cvsd_vocoder.*
%{python_sitearch}/%{name}/vocoder/cvsd_vocoder.*

############################
%package -n python-%{name}-gsm-fr-vocoder
Summary:	GNU Radio GSM Full-Rate Vocoder
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-gsm-fr-vocoder
This package provides an implementation of a full-rate GSM vocoder for
GNU Radio.

%files -n python-%{name}-gsm-fr-vocoder
%defattr(-,root,root)
%{python_sitearch}/%{name}/vocoder/_gsm_full_rate.*
%{python_sitearch}/%{name}/vocoder/gsm_full_rate.*

############################
%package -n python-%{name}-msdd6000
Summary:	Python bindings for Softronics MSDD 6000 GNU Radio blocks
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-msdd6000
This package provides Python bindings for Softronics MSDD 6000 GNU Radio blocks.

%files -n python-%{name}-msdd6000
%defattr(-,root,root)
%{python_sitearch}/%{name}/_msdd.*
%{python_sitearch}/%{name}/msdd.*
%{python_sitearch}/%{name}/_msdd_rs.*
%{python_sitearch}/%{name}/msdd_rs.*

############################
%package -n python-%{name}-qtgui
Summary:	GNU Radio Graphical Interface Routines based on QT
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-qtgui
This package provides the Python wrappers around the GNU Radio QT GUI
C++ blocks.

%files -n python-%{name}-qtgui
%defattr(-,root,root)
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
%defattr(-,root,root)
%{python_sitearch}/%{name}/_trellis.*
%{python_sitearch}/%{name}/trellis.*

############################
%package -n python-%{name}-usrp
Summary:	Python bindings for GNU Radio USRP driver
Group:		Development/Python
Requires:       python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-usrp
This package provides the Python interface to the GNU Radio USRP driver
and daughterboard drivers.

%files -n python-%{name}-usrp
%defattr(-,root,root)
%{python_sitearch}/%{name}/usrp

############################
%package -n python-%{name}-usrp2
Summary:	Python bindings for GNU Radio USRP driver
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n	python-%{name}-usrp2
This package provides the Python interface to the GNU Radio USRP driver
and daughterboard drivers. 

%files -n python-%{name}-usrp2  
%defattr(-,root,root)
%{python_sitearch}/%{name}/_usrp2.*
%{python_sitearch}/%{name}/usrp2.*

############################
%package -n python-%{name}-video-sdl
Summary:	GNU Radio SDL Interface Library
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-%{name}-video-sdl
This package provides an interface to the SDL rendering library for GNU Radio.

%files -n python-%{name}-video-sdl
%defattr(-,root,root)
%{python_sitearch}/%{name}/_video_sdl.*
%{python_sitearch}/%{name}/video_sdl.*

############################
%package -n python-usrp
Summary:	Python bindings for the USRP library
Group:		Development/Python
Requires:	python-%{name}-core = %{version}-%{release}

%description -n python-usrp
This package provides auxiliary routines in Python for manipulating the USRP hardware. 

%files -n python-usrp
%defattr(-,root,root)
%{python_sitearch}/usrpm

############################
%package -n python-%{name}-wxgui
Summary:	GNU Radio Graphical Interface Routines based on wxPython
Group:		Networking/Other
Requires:	python-%{name}-core = %{version}-%{release}
Requires:	python-numpy
Requires:	python-opengl

%description -n python-%{name}-wxgui
This package provides high level GUI construction classes based upon the wxPython bindings 
for wxWidgets.

%files -n python-%{name}-wxgui
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/gr-wxgui.conf
%{python_sitearch}/%{name}/wxgui
%exclude %{python_sitearch}/%{name}/wxgui/ra_*.*
#
# This should really be in a devel package
%{_libdir}/pkgconfig/gr-wxgui.pc

############################
############################
#
# Software packages and others
#
############################
############################

%package companion
Summary:	The GNU Radio Companion
Group:		Networking/Other
Requires:	python-%{name}-core = %{version}-%{release}
Requires:	python-cheetah
Requires:	pygtk2.0
Requires:	python-lxml
Obsoletes:	%{name} < %{version}-%{release}
Provides:	%{name} = %{version}-%{release}

%description companion
GRC is a graphical flowgraph editor for the GNU Software Radio.

%files companion
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/grc.conf
%{_bindir}/gnuradio-companion
%{_bindir}/usrp*_probe
%{_datadir}/applications/*.desktop
%{_datadir}/mime/application/*.xml
%{_iconsdir}/hicolor/*/apps/gnuradio-grc.png
%{_datadir}/%{name}/grc
%{python_sitearch}/%{name}/grc
%{python_sitearch}/grc_%{name}

############################
%package gpio
Summary:	GNU Radio Streaming Digital Application
Group:		Networking/Other
Requires:	python-%{name}-usrp = %{name}-%{version}
Requires:	usrp-firmware = %{version}-%{release}

%description gpio
This package provides streaming digital GPIO capabilities for GNU Radio 

%files gpio
%defattr(-,root,root)
%{_bindir}/gpio*
%{python_sitearch}/%{name}/gpio

############################
%package  noaa
Summary:	GNU Radio NOAA POES HRPT receiver
Group:		Networking/Other
Requires:	python-%{name}-core = %{version}-%{release}

%description noaa
This package provides and implements an NOAA POES HRPT receiver.

%files noaa
%defattr(-,root,root)
%{_bindir}/usrp_rx_hrpt.py
%{_bindir}/file_rx_hrpt.py
%{_bindir}/file_rx_lrit.py
%{_bindir}/hrpt_decode.py
%{_bindir}/hrpt_demod.py
%{_bindir}/usrp_rx_hrpt_nogui.py
%{_bindir}/usrp_rx_lrit.py
%{python_sitearch}/%{name}/noaa

############################
%package pager
Summary:	GNU Radio FLEX Pager Decoder
Group:		Networking/Other
Requires:	python-%{name}-usrp = %{name}-%{version}

%description pager
This package provides a decoder for the FLEX paging protocol for GNU Radio.

%files pager
%defattr(-,root,root)
%{_bindir}/usrp_flex*
%{python_sitearch}/%{name}/pager

############################
%package radar-mono
Summary:	GNU Radio Monostatic Radar Application
Group:		Networking/Other
Requires:	python-%{name}-usrp = %{name}-%{version}
Requires:	usrp-firmware = %{version}-%{release}

%description radar-mono
This package provides a monostatic radar application for GNU Radio.

%files radar-mono
%defattr(-,root,root)
%{_bindir}/usrp_radar_mono.*
%{python_sitearch}/%{name}/radar_mono.*

############################
%package radio-astronomy
Summary:	GNU Radio Radio Astronomy Applications
Group:		Networking/Other
Requires:	python-%{name}-usrp = %{name}-%{version}
Requires:	python-%{name}-wxgui = %{name}-%{version}

%description radio-astronomy
This package provides radio astronomy applications for GNU Radio.

%files radio-astronomy
%defattr(-,root,root)
%{_bindir}/usrp_*_receiver.*
%{python_sitearch}/%{name}/_ra.*
%{python_sitearch}/%{name}/ra.*
%{python_sitearch}/%{name}/local_calibrator.*
%{python_sitearch}/%{name}/wxgui/ra_*.*

############################
%package sounder
Summary:	GNU Radio Channel Sounder Application
Group:		Networking/Other
Requires:       python-%{name}-usrp = %{name}-%{version}
Requires:	usrp-firmware = %{version}-%{release}

%description sounder
This package provides an RF channel sounder application for GNU Radio.

%files sounder
%defattr(-,root,root)
%{_bindir}/usrp_sounder.*
%{python_sitearch}/%{name}/sounder.*

############################
%package utils
Summary:	GNU Radio Utilities
Group:		Networking/Other
Requires:	python-%{name}-usrp = %{version}-%{release}
Requires:	python-%{name}-usrp2 = %{version}-%{release}
Requires:	python-%{name}-wxgui = %{version}-%{release}
Requires:	python-matplotlib
Requires:	python-scipy
Requires:	python-qt4
Requires:	python-qwt
Obsoletes:	usrp < %{version}-%{release}
Provides:	usrp = %{version}-%{release}

%description utils
This package provides commonly used utilities for GNU Radio.

%files utils
%defattr(-,root,root)
%{_bindir}/find_usrps
%{_bindir}/gr_filter_design.py
%{_bindir}/gr_plot_*.py
%{_bindir}/lsusrp
%{_bindir}/usrp_fft.py
%{_bindir}/usrp_oscope.py
%{_bindir}/usrp_print_db.py
%{_bindir}/usrp_rx_cfile.py
%{_bindir}/usrp_rx_nogui.py
%{_bindir}/usrp_siggen.py
%{_bindir}/usrp_siggen_gui.py
%{_bindir}/usrp_test_counting.py
%{_bindir}/usrp_test_loopback.py
%{_bindir}/usrp2_fft.py
%{_bindir}/usrp2_rx_cfile.py
%{python_sitearch}/%{name}/plot_data.*
%{python_sitearch}/%{name}/pyqt_filter.*
%{python_sitearch}/%{name}/pyqt_plot.*
###
%{_bindir}/usrper
%{_bindir}/gnuradio-config-info
%{_bindir}/usrp2_burn_mac_addr
%{_bindir}/usrp2_socket_opener
%{_bindir}/usrp_cal_dc_offset

############################

%prep
%setup -q
%patch0 -p0 -b .cflags
%if %mdkversion >= 201100
%patch1 -p0
%endif

# force regeneration of cached moc output files
find . -name "*_moc.cc" -exec rm {} \;

%build
%configure2_5x \
	--enable-doxygen \
	--enable-latex-doc \
	--disable-gr-audio-oss \
	--enable-grc \
	--enable-usrp \
	--enable-gnuradio-core \
	--enable-gnuradio-examples \
	--with-qwt-incdir=%{_includedir} \
	--with-qwtplot3d-incdir=%{_includedir}

%make LIBS="-lpython%{py_ver} -lpthread"

%install
rm -rf %{buildroot}
%makeinstall_std

#move docs to a better location
mv %{buildroot}%{_docdir}/%{name}-%{version} gnuradio-docs
mv %{buildroot}%{_docdir}/usrp-%{version} usrp-docs

#icons
for i in 32 48 64 128 256; do
	install -Dpm0644 %{buildroot}%{_datadir}/%{name}/grc/freedesktop/grc-icon-${i}.png \
		%{buildroot}/%{_iconsdir}/hicolor/${i}x${i}/apps/gnuradio-grc.png
done

#desktop files
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/mime/application
mv %{buildroot}%{_datadir}/%{name}/grc/freedesktop/*.desktop %{buildroot}%{_datadir}/applications/
mv %{buildroot}%{_datadir}/%{name}/grc/freedesktop/gnuradio-grc.xml %{buildroot}%{_datadir}/mime/application/

#we don't want these
find %{buildroot} -name "*.la" -exec rm -rf {} \;
rm -rf %{buildroot}%{_bindir}/create-gnuradio-out-of-tree-project
rm -rf %{buildroot}%{_bindir}/grc_setup_freedesktop
rm -rf %{buildroot}/%{_datadir}/%{name}/grc/freedesktop	

%clean
rm -rf %{buildroot}

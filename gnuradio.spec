Name:           gnuradio
Version:        3.3.0
Release:        %mkrel 1
Summary:        Software defined radio framework
Group:          Networking/Other 
License:        GPLv3
URL:            http://www.gnuradio.org
Source0:        ftp://ftp.gnu.org/gnu/gnuradio/gnuradio-%{version}.tar.gz
BuildRequires:  fftw-devel
BuildRequires:  cppunit-devel
BuildRequires:  fftw-devel
BuildRequires: 	libboost-devel
#BuildRequires:	libwxPythonGTK2.8
BuildRequires: 	libwxgtk2.8-devel
BuildRequires: 	%{mklibname alsa-oss}-devel
BuildRequires: 	libSDL-devel
BuildRequires: 	libportaudio-devel
BuildRequires: 	libjack-devel
BuildRequires:	swig
BuildRequires:	doxygen
BuildRequires:  libusb-devel
BuildRequires:  xmlto
BuildRequires:  graphviz
BuildRequires:	wxPython
BuildRequires:	sdcc
BuildRequires:	libomniorb
BuildRequires:	ltp
BuildRequires:  libgsl-devel
BuildRequires:  libqwt-devel
BuildRequires:  python-cheetah
BuildRequires:  python-lxml
BuildRequires:  guile
Requires:	libgsl-devel

%description
GNU Radio is a collection of software that when combined with minimal 
hardware, allows the construction of radios where the actual waveforms 
transmitted and received are defined by software. What this means is 
that it turns the digital modulation schemes used in today's high 
performance wireless devices into software problems.

%package devel
Summary:        GNU Radio
Group:          Networking/Other 
Requires:       %{name} = %{version}-%{release}

%description devel
GNU Radio Headers

%package doc
Summary:        GNU Radio
Group:          Networking/Other 
Requires:       %{name} = %{version}-%{release}

%description doc
GNU Radio Documentation

%package usrp
Summary:        Universal Software Radio Peripheral
Group:          Networking/Other 
Requires:       %{name} = %{version}-%{release}

%description usrp
GNU Radio USRP files

%prep
%setup -q

%build
./bootstrap
#%configure2_5x --enable-all-components  --enable-doxygen  --enable-latex-doc  --disable-gr-qtgui  --enable-gr-audio-oss --disable-gr-audio-osx --disable-comedi --disable-gr-comedi --disable-gr-gcell --disable-gcell --disable-gr-audio-windows --disable-usrp --disable-gr-usrp --disable-usrp2 --disable-gr-usrp2 --disable-gr-gpio --disable-gr-radar-mono --disable-gr-sounder --disable-gr-utils --disable-usrp2-firmware --disable-gr-audio-jack
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%configure2_5x --enable-libgc --disable-gr-audio-jack
%make


%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog README README.hacking NEWS
%{python_sitelib}/gnuradio
%{python_sitelib}/usrpm
%{_bindir}/usrp*
#%{_bindir}/*
%{_libdir}/libgnuradio-core*
%{_libdir}/libusrp.*
%{_libdir}/libusrp2.*
%{_libdir}/libgnuradio-*
%{_libdir}/libgruel*
%{_libdir}/libusrp-*
%{_libdir}/libusrp2-*
#%{_libdir}/libgromnithread*
#%{_libdir}/libgr_audio_alsa*
%{_libdir}/pkgconfig/*.pc  
%{_libdir}/python2.6/site-packages/grc_gnuradio/*  
%{_datadir}/usrp
%{_datadir}/gnuradio/examples/*
%{_datadir}/gnuradio/grc/blocks/
%{_datadir}/gnuradio/grc/freedesktop
%{_datadir}/gnuradio/*
%{_sysconfdir}/gnuradio
%config(noreplace)%{_sysconfdir}/gnuradio/conf.d/gr-audio-alsa.conf
%config(noreplace)%{_sysconfdir}/gnuradio/conf.d/gnuradio-core.conf
%config(noreplace)%{_sysconfdir}/gnuradio/conf.d/gr-wxgui.conf

%files devel
%defattr(-,root,root,-)
%{_includedir}/gnuradio
%{_includedir}/usrp*
%{_includedir}/gruel/*

%files doc
%defattr(-,root,root,-)
%{_docdir}/usrp-%{version}/*
%{_docdir}/%{name}-%{version}/html/*
%{_docdir}/%{name}-%{version}/xml/*
%{_docdir}/%{name}-%{version}/README*

%files usrp
%defattr(-,root,root,-)



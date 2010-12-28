# TODO:
# - better summaries and descriptions
# - libify gnuradio
# - maybe some more?!

Name:           gnuradio
Version:        3.3.0
Release:        %mkrel 7
Summary:        Software defined radio framework
Group:          Networking/Other 
License:        GPLv3
URL:            http://www.gnuradio.org
Source0:        ftp://ftp.gnu.org/gnu/gnuradio/gnuradio-%{version}.tar.gz
Patch1:		usrpgccpatch.diff
BuildRequires:	cppunit-devel
BuildRequires:	doxygen
BuildRequires:	fftw-devel
BuildRequires:	graphviz
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
Requires:	python-numpy
Requires:	wxPython
Requires:	python-scipy
Requires:	portaudio

%description
GNU Radio is a collection of software that when combined with minimal 
hardware, allows the construction of radios where the actual waveforms 
transmitted and received are defined by software. What this means is 
that it turns the digital modulation schemes used in today's high 
performance wireless devices into software problems.

%package devel
Summary:	GNU Radio
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
GNU Radio Headers.

%package doc
Summary:	GNU Radio
Group:		Networking/Other
Requires:	%{name} = %{version}-%{release}

%description doc
GNU Radio Documentation.

%package examples
Summary:	GNU Radio
Group:		Networking/Other
Requires:	%{name} = %{version}-%{release}

%description examples
GNU Radio examples.

%package -n usrp
Summary:	Universal Software Radio Peripheral
Group:		Networking/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-usrp
Provides:	%{name}-usrp

%description -n usrp
Gnu Radio Universal Software Radio Peripheral software.

%package -n usrp-devel
Summary:	Universal Software Radio Peripheral
Group:		Development/Other
Requires:	usrp = %{version}-%{release}

%description -n usrp-devel
Gnu Radio Universal Software Radio Peripheral development files and headers.

%package -n usrp-doc
Summary:        Universal Software Radio Peripheral
Group:          Networking/Other
Requires:	usrp = %{version}-%{release}

%description -n usrp-doc
Gnu Radio Universal Software Radio Peripheral documentation.

%prep
%setup -q
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
	--enable-usrp \
	--enable-gnuradio-core \
	--enable-gnuradio-examples \
	--with-pythondir=%{py_puresitedir} \
	--with-qwt-incdir=%{_includedir} \
	--with-qwtplot3d-incdir=%{_includedir}

%make LIBS="-lpython%{py_ver} -lpthread"

%install
rm -rf %{buildroot}
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -exec rm -rf {} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitearch}/grc_gnuradio
%{python_sitearch}/%{name}
%exclude %{python_sitearch}/%{name}/_usrp2.so
%exclude %{python_sitearch}/%{name}/usrp*  
%dir %{_sysconfdir}/%{name} 
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace)%{_sysconfdir}/%{name}/conf.d/*.conf
%{_bindir}/%{name}*
%{_bindir}/*.py
%exclude %{_bindir}/usrp*.py
%{_bindir}/create-gnuradio-out-of-tree-project
%{_bindir}/grc_setup_freedesktop
%{_libdir}/libgnuradio*.so.*
%{_libdir}/libgruel*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_includedir}/gruel
%{_libdir}/libgnuradio*.so
%{_libdir}/libgruel.so
%{_libdir}/pkgconfig/gnuradio*.pc
%{_libdir}/pkgconfig/gr-wxgui.pc
%{_libdir}/pkgconfig/gruel.pc

%files doc
%defattr(-,root,root,-)
%doc ChangeLog README README.hacking NEWS AUTHORS
%{_docdir}/%{name}-%{version}

%files -n usrp-doc
%defattr(-,root,root,-)
%{_docdir}/usrp-%{version}

%files examples
%defattr(-,root,root,-)
%{_datadir}/%{name}

%files -n usrp
%defattr(-,root,root,-)
%{_bindir}/usrp*
%{_bindir}/gpio*
%{_bindir}/find_usrps
%{_bindir}/lsusrp
%{_datadir}/usrp
%{_libdir}/libusrp*.so.*
%{python_sitearch}/usrpm
%{python_sitearch}/%{name}/_usrp2.so
%{python_sitearch}/%{name}/usrp*

%files -n usrp-devel
%defattr(-,root,root,-)
%{_libdir}/libusrp*.so
%{_includedir}/usrp*
%{_libdir}/pkgconfig/usrp*.pc

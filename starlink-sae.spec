Summary:	SAE - Starlink Applications Environment special files
Summary(pl):	SAE - pliki specjalne dla ¶rodowiska aplikacji Starlink
Name:		starlink-sae
Version:	1.0_4.218
Release:	1
License:	GPL
Group:		Development
#Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/sae/sae.tar.Z
Source0:	sae.tar.Z
# Source0-md5:	d76376d6dc79076e7e0ec7d0960842dd
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_SAE.html
BuildRequires:	starlink-htx
Requires:	starlink-htx
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
The SAE package brings together some include files, a facility error
file and a shell script needed for development of software in the
Starlink environment, and for building the USSC.

%description -l pl
Pakiet SAE (Starlink Applications Environment - ¶rodowisko aplikacji
Starlink) dostarcza kilka plików nag³ówkowych, plik definiuj±cy kody
b³êdów oraz skrypt pow³oki potrzebny do tworzenia oprogramowania w
¶rodowisku Startlink oraz do budowania USSC.

%package devel
Summary:	Development files for SAE environment
Summary(pl):	Pliki programistyczne ¶rodowiska SAE
Group:		Development
Requires:	%{name} = %{version}

%description devel
Development files for SAE environment.

%description devel -l pl
Pliki programistyczne ¶rodowiska SAE.

%prep
%setup -q -c

%build
SYSTEM=ix86_Linux \
./mk build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sae.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%{stardir}/help/fac*

%files devel
%attr(755,root,root) %{stardir}/bin/star_dev
%{stardir}/include/*

Summary:	Load the NVIDIA kernel module and create NVIDIA character device files
Summary(pl.UTF-8):	Ładowanie modułu jądra NVIDIA i tworzenie plików urządzeń znakowych NVIDIA
Name:		nvidia-modprobe
Version:	510.54
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://download.nvidia.com/XFree86/nvidia-modprobe/%{name}-%{version}.tar.bz2
# Source0-md5:	b7a2671f6b6beb5557859cd0e2faedb4
URL:		https://download.nvidia.com/XFree86/nvidia-modprobe/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The nvidia-modprobe utility is used by user-space NVIDIA driver
components to make sure the NVIDIA kernel module is loaded and that
the NVIDIA character device files are present.

%description -l pl.UTF-8
Narzędzie nvidia-modprobe jest używane przez komponenty sterownika
NVIDIA działające w przestrzeni użytkownika w celu zapewnienia, że
moduł jądra NVIDIA jest załadowany oraz pliki urządzeń znakowych
NVIDIA są utworzone.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
%{__make} \
	CC="%{__cc}" \
	DO_STRIP= \
	MANPAGE_GZIP=0 \
	NV_VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	MANPAGE_GZIP=0 \
	NV_VERBOSE=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/nvidia-modprobe
%{_mandir}/man1/nvidia-modprobe.1*

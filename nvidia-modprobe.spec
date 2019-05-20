Summary:	Load the NVIDIA kernel module and create NVIDIA character device files
Name:		nvidia-modprobe
Version:	430.14
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://download.nvidia.com/XFree86/nvidia-modprobe/%{name}-%{version}.tar.bz2
# Source0-md5:	153de667b62f463f8793c76c2b57f649
URL:		https://download.nvidia.com/XFree86/nvidia-modprobe/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The nvidia-modprobe utility is used by user-space NVIDIA driver
components to make sure the NVIDIA kernel module is loaded and that
the NVIDIA character device files are present.

%prep
%setup -q

%build
%{__make} \
	NV_VERBOSE=1 \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	NV_VERBOSE=1 \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/nvidia-modprobe
%{_mandir}/man1/nvidia-modprobe.1*

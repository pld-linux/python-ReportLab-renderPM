# TODO: real description
%define		_snap	20070412
Summary:	Bitmap renderer module for the ReportLab Toolkit
Summary(pl.UTF-8):	Moduł do renderowania bitmap dla toolkitu ReportLab
Name:		python-ReportLab-renderPM
Version:	1.03
Release:	1
License:	distributable
Group:		Libraries/Python
Source0:	http://www.reportlab.org/daily/renderPM-%{version}-daily-unix.tgz
# Source0-md5:	c8651574c4ebe2a5abecc2659a35f1bb
URL:		http://www.reportlab.org/
BuildRequires:	python-devel >= 1:2.4
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bitmap renderer module for the ReportLab Toolkit.

%description -l pl.UTF-8
Moduł do renderowania bitmap dla toolkitu ReportLab.

%prep
%setup -q -n renderPM-%{version}-%{_snap}

%build
cd renderPM
CFLAGS="%{rpmcflags}"; export CFLAGS
%py_build

%install
rm -rf $RPM_BUILD_ROOT
cd renderPM
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so

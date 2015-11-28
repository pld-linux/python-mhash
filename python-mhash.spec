Summary:	Python interface for mhash library
Summary(pl.UTF-8):	Interfejs Pythona do biblioteki mhash
Name:		python-mhash
Version:	1.4
Release:	4
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/mhash/%{name}-%{version}.tar.bz2
# Source0-md5:	fb2a9ebae95c995eb8dea58eca1b46ed
URL:		http://mhash.sourceforge.net/
BuildRequires:	mhash-devel >= 0.9.2
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	mhash >= 0.9.2
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python mhash module provides an interface for the mhash library.
The mhash library provides an easy way to access strong hashes such as
MD5, SHA1 and other algorithms.

%description -l pl.UTF-8
Moduł Pythona mhash dostarcza interfejs do biblioteki mhash.
Biblioteka mhash daje łatwy dostęp do silnych algorytmów mieszających,
takich jak MD5, SHA1 i inne.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{py_sitedir}/*.so

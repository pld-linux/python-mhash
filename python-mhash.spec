%include	/usr/lib/rpm/macros.python
Summary:	Python interface for mhash library
Summary(pl):	Interfejs Pythona do biblioteki mhash
Name:		python-mhash
Version:	1.2
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/mhash/%{name}-%{version}.tar.gz
# Source0-md5:	b82467ec28cec6ca3258c06cc0ee3e88
URL:		http://mhash.sourceforge.net/
BuildRequires:	mhash-devel
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python mhash module provides an interface for the mhash library.
The mhash library provides an easy way to access strong hashes such as
MD5, SHA1 and other algorithms.

%description -l pl
Modu³ Pythona mhash dostarcza interfejs do biblioteki mhash.
Biblioteka mhash daje ³atwy dostêp do silnych algorytmów mieszaj±cych,
takich jak MD5, SHA1 i inne.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{py_sitedir}/*.so

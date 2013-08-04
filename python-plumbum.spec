%global pypi_name plumbum
%global with_python3 1

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Shell combinators library

License:        MIT
URL:            https://github.com/tomerfiliba/plumbum
Source0:        http://pypi.python.org/packages/source/p/plumbum/plumbum-%{version}.tar.gz
# https://github.com/tomerfiliba/plumbum/pull/55
Patch0:         plumbum-1.1.0-fix-print-for-p3.patch
Patch1:         plumbum-1.1.0-add-__path__-to-LocalModule.patch

BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-six

%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif # if with_python3

%description
Ever wished the wrist-handiness of shell scripts be put into a real programming
language? Say hello to Plumbum Shell Combinators. Plumbum (Latin for lead,
which was used to create pipes back in the day) is a small yet feature-rich
library for shell script-like programs in Python. The motto of the library is
"Never write shell scripts again", and thus it attempts to mimic the shell
syntax ("shell combinators") where it makes sense, while keeping it all
pythonic and cross-platform.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Shell combinators library
Requires:       python3-six

%description -n python3-%{pypi_name}
Ever wished the wrist-handiness of shell scripts be put into a real programming
language? Say hello to Plumbum Shell Combinators. Plumbum (Latin for lead,
which was used to create pipes back in the day) is a small yet feature-rich
library for shell script-like programs in Python. The motto of the library is
"Never write shell scripts again", and thus it attempts to mimic the shell
syntax ("shell combinators") where it makes sense, while keeping it all
pythonic and cross-platform.
%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%patch0 -p1
%patch1 -p1

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc LICENSE README.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc LICENSE README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3


%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.0-2
- Patch the Python 3.3 module subclass error.

* Fri Feb 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.0-1
- Update to 1.1.0.

* Fri Feb 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.1-2
- Introduce python3 subpackage.

* Mon Nov 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.1-1
- Update to 1.0.1.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.0-1
- Initial package.

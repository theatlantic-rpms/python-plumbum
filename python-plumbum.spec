%global pypi_name plumbum

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Shell combinators library

License:        MIT
URL:            https://github.com/tomerfiliba/plumbum
Source0:        http://pypi.python.org/packages/source/p/plumbum/plumbum-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-six

%description
Ever wished the wrist-handiness of shell scripts be put into a real programming
language? Say hello to Plumbum Shell Combinators. Plumbum (Latin for lead,
which was used to create pipes back in the day) is a small yet feature-rich
library for shell script-like programs in Python. The motto of the library is
"Never write shell scripts again", and thus it attempts to mimic the shell
syntax ("shell combinators") where it makes sense, while keeping it all
pythonic and cross-platform.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc LICENSE README.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Mon Nov 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.1-1
- Update to 1.0.1.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.0-1
- Initial package.

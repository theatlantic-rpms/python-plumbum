%global pypi_name plumbum
%global with_python3 1

Name:           python-%{pypi_name}
Version:        1.6.6
Release:        1%{?dist}
Summary:        Shell combinators library

License:        MIT
URL:            https://github.com/tomerfiliba/plumbum
Source0:        http://pypi.python.org/packages/source/p/plumbum/plumbum-%{version}.tar.gz

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
* Fri Jun 15 2018 Frankie Dintino <fdintino@theatlantic.com> - 1.6.6-1
- Update to 1.6.6 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.6.0-1
- Update to 1.6.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Slavek Kabrda <bkabrda@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

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

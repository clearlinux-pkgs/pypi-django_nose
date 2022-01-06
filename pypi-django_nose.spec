#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-django_nose
Version  : 1.4.7
Release  : 1
URL      : https://files.pythonhosted.org/packages/4c/d6/a340da9854cf0a2b54e23cf9147911b1e15a831911428983dd0158572ce9/django-nose-1.4.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/4c/d6/a340da9854cf0a2b54e23cf9147911b1e15a831911428983dd0158572ce9/django-nose-1.4.7.tar.gz
Summary  : Makes your Django tests simple and snappy
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-django_nose-license = %{version}-%{release}
Requires: pypi-django_nose-python = %{version}-%{release}
Requires: pypi-django_nose-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(check_manifest)
BuildRequires : pypi(coverage)
BuildRequires : pypi(dj_database_url)
BuildRequires : pypi(django)
BuildRequires : pypi(flake8)
BuildRequires : pypi(flake8_docstrings)
BuildRequires : pypi(ipdb)
BuildRequires : pypi(ipdbplugin)
BuildRequires : pypi(ipython)
BuildRequires : pypi(nose)
BuildRequires : pypi(pyroma)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(tox)
BuildRequires : pypi(twine)
BuildRequires : pypi(wheel)

%description
===========
        django-nose
        ===========

%package license
Summary: license components for the pypi-django_nose package.
Group: Default

%description license
license components for the pypi-django_nose package.


%package python
Summary: python components for the pypi-django_nose package.
Group: Default
Requires: pypi-django_nose-python3 = %{version}-%{release}

%description python
python components for the pypi-django_nose package.


%package python3
Summary: python3 components for the pypi-django_nose package.
Group: Default
Requires: python3-core
Provides: pypi(django_nose)
Requires: pypi(nose)

%description python3
python3 components for the pypi-django_nose package.


%prep
%setup -q -n django-nose-1.4.7
cd %{_builddir}/django-nose-1.4.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641511009
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-django_nose
cp %{_builddir}/django-nose-1.4.7/LICENSE %{buildroot}/usr/share/package-licenses/pypi-django_nose/abeb4d52f5efe6fc97782177199726a557c65aa8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-django_nose/abeb4d52f5efe6fc97782177199726a557c65aa8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

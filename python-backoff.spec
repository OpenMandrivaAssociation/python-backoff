%define module backoff

Summary: Python library providing function decorators for configurable backoff and retry
Name:		python-%{module}
Version:	2.2.1
Release:	2
Group:		Development/Python
License:	MIT
URL:		https://github.com/litl/backoff
Source0:	%{url}/archive/v%{version}/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(poetry-core)

%description
This module provides function decorators which can be used to wrap
a function such that it will be retried until some condition is met.
It is meant to be of use when accessing unreliable resources with the
potential for intermittent failures i.e. network resources and external
APIs. Somewhat more generally, it may also be of use for dynamically
polling resources for externally generated content.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc CHANGELOG.md README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}.dist-info/

%define module backoff
%define oname python_backoff

Name:		python-backoff
Version:	2.3.1
Release:	1
Summary:	Python library providing function decorators for configurable backoff and retry
Group:		Development/Python
License:	MIT
# New maintained fork
URL:		https://github.com/python-backoff/backoff
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

# Upstream renamed the module from backoff to python-backoff, we have to
# provide an upgrade path and a route for other modules to be able to locate
# the renamed module.
Provides:	python%{pyver}dist(backoff) = %{version}

%description
This module provides function decorators which can be used to wrap
a function such that it will be retried until some condition is met.
It is meant to be of use when accessing unreliable resources with the
potential for intermittent failures i.e. network resources and external
APIs. Somewhat more generally, it may also be of use for dynamically
polling resources for externally generated content.

%files
%license LICENSE
%doc CHANGELOG.md README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{oname}-%{version}.dist-info

%define		_module		exif
Summary:	EXIF/IPTC module for Gallery
Summary(pl):	Modu³ do odczytu EXIF/IPTC dla Gallery
Name:		gallery-module-%{_module}
Version:	1.0.6
Release:	0.1
License:	GPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/gallery/g2-module-%{_module}-%{version}.tar.gz
# Source0-md5:	94c70c26238b9812c7df7083159c53b8
URL:		http://codex.gallery2.org/index.php/Gallery2:Modules:exif
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	gallery >= 2.1.0
Requires:	php-exif
Provides:	external-gallery-module
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/gallery/modules/%{_module}

%description
Makes block available to themes for display of EXIF/IPTC metadata from
image files. Configure fields to display in site admin. Site admin can
also configure whether EXIF description or IPTC keywords are imported
into Gallery fields for newly added items.

%description -l pl
Ten modu³ udostêpnia motywom blok do wy¶wietlania metadanych EXIF/IPTC
z plików zdjêæ. Wy¶wietlane pola mo¿na konfigurowaæ w panelu
administracyjnym. Tam te¿ mo¿na ustawiæ, czy opis EXIF lub s³owa
kluczowe IPTC maj± byæ importowane do pól galerii dla nowo dodawanych
elementów.

%prep
%setup -q -n modules

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cd %{_module}
cp -R * $RPM_BUILD_ROOT%{_appdir}

# Cleanups:
rm -rf $RPM_BUILD_ROOT%{_appdir}/{MANIFEST,test/}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_module}/test
%{_appdir}

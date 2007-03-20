%define		_module		exif
Summary:	EXIF/IPTC module for Gallery
Summary(pl.UTF-8):	Moduł do odczytu EXIF/IPTC dla Gallery
Name:		gallery-module-%{_module}
Version:	1.1.0
Release:	0.1
License:	GPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/gallery/g2-module-%{_module}-%{version}.tar.gz
# Source0-md5:	8ca34069e8b34499ef109bd14224f27b
URL:		http://codex.gallery2.org/index.php/Gallery2:Modules:exif
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	gallery >= 2.1.0
Requires:	php(exif)
Provides:	external-gallery-module
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/gallery/modules/%{_module}

%description
Makes block available to themes for display of EXIF/IPTC metadata from
image files. Configure fields to display in site admin. Site admin can
also configure whether EXIF description or IPTC keywords are imported
into Gallery fields for newly added items.

%description -l pl.UTF-8
Ten moduł udostępnia motywom blok do wyświetlania metadanych EXIF/IPTC
z plików zdjęć. Wyświetlane pola można konfigurować w panelu
administracyjnym. Tam też można ustawić, czy opis EXIF lub słowa
kluczowe IPTC mają być importowane do pól galerii dla nowo dodawanych
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

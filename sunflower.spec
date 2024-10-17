Name:           sunflower
Version:        0.2.59
Release:        1
Summary:        Graphic twin panel file manager
Group:          System/X11
License:        GPL-3.0
URL:            https://code.google.com/p/sunflower-fm/
Source0:        http://sunflower-fm.googlecode.com/files/sunflower-0.2-59.tgz
Source1:        sunflower.sh
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  desktop-file-utils
Requires:       pygtk2.0
Requires:       python-notify
Requires:       vte

%description
Is a small and highly customizable twin-panel file manager for Linux with
support for plugins.

%prep
%setup -q -n Sunflower

%build
rm -f translations/*/LC_MESSAGES/sunflower.po
rm -f translations/sunflower.pot

%install
%__install -D -m 644 %{_builddir}/Sunflower/images/sunflower.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

%__install -d -m 755 %{buildroot}%{_datadir}/sunflower/
cp -r %{_builddir}/Sunflower/* %{buildroot}%{_datadir}/sunflower/

%__install -D -m 755 %{_builddir}/Sunflower/Sunflower.py %{buildroot}%{_datadir}/sunflower/Sunflower.py
%__install -D -m 755 %{SOURCE1} %{buildroot}%{_bindir}/sunflower
mkdir -p %{buildroot}%{_datadir}/applications/
mv %{buildroot}%{_datadir}/sunflower/Sunflower.desktop %{buildroot}%{_datadir}/applications/Sunflower.desktop
ln -s %{_datadir}/sunflower/images/sunflower.png %{buildroot}%{_datadir}/pixmaps/sunflower.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/sunflower
%{_datadir}/applications/Sunflower.desktop
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/sunflower

%changelog
* Thu Jun 13 2013 Huaren Zhong <huaren.zhong@gmail.com> - 0.1a.56
- Rebuild for Fedora
* Sun Feb  5 2012 nekolayer@yandex.ru
- initial package

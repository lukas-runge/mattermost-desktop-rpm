%global debug_package %{nil}
%global __strip /bin/true
%global __provides_exclude_from ^/opt/Mattermost/.*$
%global __requires_exclude_from ^/opt/Mattermost/.*$

Name:           mattermost-desktop
Version:        6.3.1
Release:        1%{?dist}
Summary:        Mattermost Desktop client (repackaged upstream build)
License:        Apache-2.0
URL:            https://github.com/mattermost/desktop
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}-linux-x86_64.rpm
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}-linux-aarch64.rpm
ExclusiveArch:  x86_64 aarch64
BuildRequires:  cpio

# Same runtime dependencies as the upstream RPM; automatic detection is off for /opt/Mattermost.
Requires:       at-spi2-core
Requires:       gtk3
Requires:       libnotify
Requires:       libuuid
Requires:       libXScrnSaver
Requires:       libXtst
Requires:       nss
Requires:       xdg-utils

%description
Mattermost Desktop, repackaged from the official upstream RPM so it can be
installed and updated through a dnf repository.

%prep
%setup -q -c -T
%ifarch x86_64
rpm2cpio %{SOURCE0} | cpio -idm --quiet
%else
rpm2cpio %{SOURCE1} | cpio -idm --quiet
%endif

%install
mkdir -p %{buildroot}%{_bindir}
cp -a opt usr %{buildroot}/
# Fedora supports unprivileged user namespaces, so the sandbox needs no setuid bit.
chmod 0755 %{buildroot}/opt/Mattermost/chrome-sandbox
ln -s /opt/Mattermost/mattermost-desktop %{buildroot}%{_bindir}/mattermost-desktop

%files
/opt/Mattermost
%{_bindir}/mattermost-desktop
%{_datadir}/applications/mattermost-desktop.desktop
%{_datadir}/icons/hicolor/*/apps/mattermost-desktop.png

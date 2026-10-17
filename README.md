# Mattermost Desktop for Fedora (COPR)

Unofficial dnf repository for the [Mattermost Desktop](https://github.com/mattermost/desktop) client.
The package is the official upstream RPM, repackaged so it can be installed and updated through dnf.
A GitHub Action checks for new upstream releases every 6 hours and COPR rebuilds automatically.

## Install

```bash
sudo dnf copr enable lukas-runge/mattermost-desktop
sudo dnf install mattermost-desktop
```

Updates arrive with the regular `sudo dnf upgrade` (or through Discover / GNOME Software).

Supported: current Fedora releases and rawhide, x86_64 and aarch64.

## How it works

- `mattermost-desktop.spec` unpacks the upstream RPM for the build architecture.
- `.copr/Makefile` downloads the sources when COPR generates the SRPM (`make_srpm` method).
- `.github/workflows/bump.yml` bumps `Version:` when upstream publishes a release; the push triggers the COPR webhook.

This repository is not affiliated with Mattermost, Inc.

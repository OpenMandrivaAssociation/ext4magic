Name: ext4magic
Version: 0.3.2
Release: 1
Source0: https://sourceforge.net/projects/ext4magic/files/ext4magic-%{version}.tar.gz
Summary: Tool to recover deleted files from ext4 filesystems
URL: https://sourceforge.net/projects/ext4magic
Patch0: https://sourceforge.net/projects/ext4magic/files/Patches/workaround.patch
Patch1: https://aur.archlinux.org/cgit/aur.git/plain/01-i_dir_acl.patch?h=ext4magic-patch-extent-free#/01-i_dir_acl.patch
Patch2: https://aur.archlinux.org/cgit/aur.git/plain/02-Fix-undefined-reference-to-makedev.patch?h=ext4magic-patch-extent-free#/02-Fix-undefined-reference-to-makedev.patch
Patch3: https://aur.archlinux.org/cgit/aur.git/plain/03-Fix-segfault-extent-free.patch?h=ext4magic-patch-extent-free#/03-Fix-segfault-extent-free.patch
License: GPL
Group: System
BuildRequires: pkgconfig(ext2fs)
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(e2p)
BuildRequires: pkgconfig(uuid)

%description
Tool to recover deleted files from ext4 filesystems

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%files
%{_bindir}/ext4magic
%{_mandir}/man8/ext4magic.8*

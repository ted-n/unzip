Summary: A utility for unpacking zip files
Name: unzip
Version: 6.0
Release: 7%{?dist}
License: BSD
Group: Applications/Archiving
Source: http://downloads.sourceforge.net/infozip/unzip60.tar.gz
# Not sent to upstream.
Patch1: unzip-6.0-bzip2-configure.patch
# Upstream plans to do this in zip (hopefully also in unzip).
Patch2: unzip-6.0-exec-shield.patch
# Upstream plans to do similar thing.
Patch3: unzip-6.0-close.patch
# Details in rhbz#532380.
# Reported to upstream: http://www.info-zip.org/board/board.pl?m-1259575993/
Patch4: unzip-6.0-attribs-overflow.patch
# Not sent to upstream, as it's Fedora/RHEL specific.
# Modify the configure script not to request the strip of binaries.
Patch5: unzip-6.0-nostrip.patch
Patch6: unzip-6.0-manpage-fix.patch
# for s-jis file to ja_JP.utf8
Patch7: unzip-6.0-japanese_charset.patch
URL: http://www.info-zip.org/UnZip.html
BuildRequires:  bzip2-devel

%description
The unzip utility is used to list, test, or extract files from a zip
archive.  Zip archives are commonly found on MS-DOS systems.  The zip
utility, included in the zip package, creates zip archives.  Zip and
unzip are both compatible with archives created by PKWARE(R)'s PKZIP
for MS-DOS, but the programs' options and default behaviors do differ
in some respects.

Install the unzip package if you need to list, test or extract files from
a zip archive.

%prep
%setup -q -n unzip60
%patch1 -p1 -b .bzip2-configure
%patch2 -p1 -b .exec-shield
%patch3 -p1 -b .close
%patch4 -p1 -b .attribs-overflow
%patch5 -p1 -b .nostrip
%patch6 -p1 -b .manpage-fix
%patch7 -p1 -b .japanese_charset

%build
make -f unix/Makefile CF_NOOPT="-I. -D_FILE_OFFSET_BITS=64 -DNO_LCHMOD -D_MBCS -DNO_WORKING_ISPRINT -DUNIX $RPM_OPT_FLAGS" generic_gcc %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1 INSTALL="cp -p" install

%files
%defattr(-,root,root)
%doc README BUGS LICENSE
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Fri Mar 01 2013 Takashi Nakajima <ted.nakajima@gmail.com> 6.0-7
- Add patch for japanese charset (Shift-JIS)

* Mon Dec 10 2012 Michal Luscon <mluscon@redhat.com> 6.0-7
- Resolves: #884679 - zip files with bzip2 compression 

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

- Fix minor manpage spelling mistake
  Resolves: #675454

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 24 2010 Karel Klic <kklic@redhat.com> - 6.0-3
- Removed BuildRoot tag
- Removed %%clean section
- Removed trailing whitespaces in the spec file

* Mon Nov 30 2009 Karel Klic <kklic@redhat.com> - 6.0-2
- Fixed a buffer overflow (rhbz#532380, unzip-6.0-attribs-overflow.patch)
- Generate debuginfos (rhbz#540220, unzip-6.0-nostrip.patch)

* Mon Nov 16 2009 Karel Klic <kklic@redhat.com> - 6.0-1
- New upstream version
- Compiled using `make generic_gcc` (includes asm)
- Removed unzip542-rpmoptflags.patch, because RPM_OPT_FLAGS
  are provided using command line
- Removed unzip-5.51-link-segv.patch, because the link file
  is not reopened in the current version
- Removed unzip-5.51-link-segv2.patch, the bug was already fixed
  in open_outfile in 5.52
- Removed unzip-5.52-toctou.patch (CAN-2005-2475), the vulnerability
  is fixed in the current version
- Removed unzip-5.52-near-4GB.patch, unzip-5.52-near-4GB2.patch,
  unzip-5.52-4GB3.patch, and unzip-5.52-4GB_types.patch, because
  the current version supports large files
- Removed unzip-5.52-long-filename.patch, the current version
  fixes the vulnerability by checking the length of command line
  arguments in unzip.c
- Removed unzip-5.52-makefile.patch, because we no longer create
  the link manually
- Removed unzip-5.52-open.patch, the current version uses umask.
- Removed unzip-5.52-cve-2008-0888.patch, the current version
  fixes this vulnerability
- Ported unzip-5.52-249057.patch to current version (unzip-6.0-close)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.52-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.52-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 19 2008 Ivana Varekova <varekova@redhat.com> - 5.52-9
- fix crash (double free) on malformed zip archive
  CVE-2008-0888 (#431438)

* Fri Feb  8 2008 Ivana Varekova <varekova@redhat.com> - 5.52-8
- fix output when out of space error appears

* Wed Jan 23 2008 Ivana Varekova <varekova@redhat.com> - 5.52-7
- fix another long file support problem

* Tue Jan 22 2008 Ivana Varekova <varekova@redhat.com> - 5.52-6
- add 4GB patch (#429674)

* Tue Sep  4 2007 Ivana Varekova <varekova@redhat.com> - 5.52-5
- fix open call

* Wed Feb  7 2007 Ivana Varekova <varekova@redhat.com> - 5.52-4
- incorporate the next peckage review comment

* Tue Feb  6 2007 Ivana Varekova <varekova@redhat.com> - 5.52-3
- Resolves: 226516
  Incorporate the package review

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.52-2.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.52-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.52-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Feb  6 2006 Ivana Varekova <varekova@redhat.com> 5.52-2
- fix bug 180078 - unzip -l causing error
- fix CVE-2005-4667 - unzip long file name buffer overflow

* Thu Dec 22 2005 Ivana Varekova <varekova@redhat.com> 5.52-1
- update to 5.52

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Aug  3 2005 Ivana Varekova <varekova@redhat.com> 5.51-12
- fix bug 164928 - TOCTOU issue in unzip

* Mon May  9 2005 Ivana Varekova <varekova@redhat.com> 5.51-11
- fix bug 156959 â€“ invalid file mode on created files

* Mon Mar  7 2005 Ivana Varekova <varekova@redhat.com> 5.51-10
- rebuilt

* Thu Feb 10 2005 Ivana Varekova <varekova@redhat.com> 5.51-9
- fix the other problem with unpacking zipfiles containing symlinks
  (bug #134073)

* Thu Feb 03 2005 Ivana Varekova <varekova@redhat.com> 5.51-8
- fix segfault with unpacking of zipfiles containing dangling symlinks
  (bug #134073)

* Thu Dec 02 2004 Lon Hohberger <lhh@redhat.com> 5.51-6
- Rebuild

* Thu Dec 02 2004 Lon Hohberger <lhh@redhat.com> 5.51-5
- Fix segfault on extraction of symlinks

* Mon Jun 21 2004 Lon Hohberger <lhh@redhat.com> 5.51-4
- Extend max file/archive size to 2^32-8193 (4294959103) bytes

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 08 2004 Lon Hohberger <lhh@redhat.com> 5.51-2
- Rebuild

* Tue Jun 08 2004 Lon Hohberger <lhh@redhat.com> 5.51-1.1
- Update to 5.51; remove dotdot patch.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Nov 17 2003 Lon Hohberger <lhh@redhat.com> 5.50-36
- Rebuild for FC-next

* Fri Aug 01 2003 Lon Hohberger <lhh@redhat.com> 5.50-35
- Rebuild for Severn

* Fri Aug 01 2003 Lon Hohberger <lhh@redhat.com> 5.50-34
- Rebuild for Taroon

* Fri Aug 01 2003 Lon Hohberger <lhh@redhat.com> 5.50-33
- Rebuild for 9 errata

* Fri Aug 01 2003 Lon Hohberger <lhh@redhat.com> 5.50-32
- Rebuild for 8.0 errata

* Fri Aug 01 2003 Lon Hohberger <lhh@redhat.com> 5.50-31
- Rebuild for 7.3 errata

* Wed Jul 30 2003 Lon Hohberger <lhh@redhat.com> 5.50-30
- SECURITY Round 3: Fix up original patch (from 5.50-9) to fix
^V/ exploit, but still allow '-:', which the other patch (5.50-18)
does not allow.  Never allow explicit writing to the root
directory; force users to change there and extract it manually.

* Wed Jul 30 2003 Lon Hohberger <lhh@redhat.com> 5.50-29
- Rebuild for Severn

* Wed Jul 30 2003 Lon Hohberger <lhh@redhat.com> 5.50-28
- Rebuild

* Wed Jul 30 2003 Lon Hohberger <lhh@redhat.com> 5.50-27
- Rebuild for 9

* Wed Jul 30 2003 Lon Hohberger <lhh@redhat.com> 5.50-26
- Rebuild for 8.0

* Tue Jul 22 2003 Lon Hohberger <lhh@redhat.com> 5.50-23
- Rebuild for 7.3

* Mon Jul 21 2003 Lon Hohberger <lhh@redhat.com> 5.50-22
- Rebuild for Severn

* Mon Jul 21 2003 Lon Hohberger <lhh@redhat.com> 5.50-21
- Rebuild

* Mon Jul 21 2003 Lon Hohberger <lhh@redhat.com> 5.50-20
- Rebuild for 9

* Mon Jul 21 2003 Lon Hohberger <lhh@redhat.com> 5.50-19
- Rebuild for 8.0

* Mon Jul 21 2003 Lon Hohberger <lhh@redhat.com> 5.50-18
- SECURITY: Incorporate far cleaner patch from Ben Laurie
<ben@algroup.co.uk> which also fixes ^V/ (quote-slash).
Patch checks post-decode as opposed to inline as previous
patch does.

* Mon Jun 16 2003 Lon Hohberger <lhh@redhat.com> 5.50-17
- Rebuilt per request

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-16
- Rebuilt

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-15
- Rebuilt

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-14
- Rebuilt: Red Hat Linux 9

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-13
- Rebuilt: Red Hat Enterprise Linux 2.1

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-12
- Rebuilt Red Hat Linux 8.0

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-11
- Rebuilt Red Hat Linux 7.3

* Wed Jun 11 2003 Lon Hohberger <lhh@redhat.com> 5.50-10
- Rebuilt

* Wed Jun 11 2003 Lon Hohberger <lhh@redhat.com> 5.50-9
- SECURITY: Scour start of filename for ../ patterns which
include quote and/or control characters.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Tim Powers <timp@redhat.com>
- bump and rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Apr 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.50-3
- Rebuild

* Tue Apr  2 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.50-2
- Make it not strip

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.50-1
- 5.50

* Thu Feb 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.42-3
- Rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 21 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 5.42
- Don't strip binaries explicitly
- build without assembly, it doesn't seem to increase performance
- make it respect RPM_OPT_FLAGS, define _GNU_SOURCE
- use %%{_tmppath}
- "License:" replaces "Copyright:"
- Update URL
- include zipgrep
- COPYING doesn't exist anymore, include LICENSE instead

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 11 2000 BIll Nottingham <notting@redhat.com>
- rebuild in new env.; FHS fixes.

* Tue Apr 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 4.51 (an acceptable license at last...)

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 5.40

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built for 6.0

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- builds on non i386 platforms

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated the version

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

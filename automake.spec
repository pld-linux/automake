Summary:	GNU automake - Makefile configuration tools
Summary(de):	GNU automake - Makefile-Konfigurationstools
Summary(fr):	automake de GNU - Outils de configuration des makefiles
Summary(pl):	GNU Automake - generator plików Makefile
Summary(tr):	Makefile yapýlandýrma araçlarý
Name:		automake
Version:	1.4
Release:	2
Copyright:	GPL
Group:		Development/Building
Group(pl):	Programowanie/Budowanie
Source:		ftp://ftp.cygnus.com/pub/tromey/%{name}-%{version}.tar.gz
Patch0:		automake-info.patch
URL:		http://sourceware.cygnus.com/automake/
Requires:	perl
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch

%description
Automake is an experimental Makefile generator. It was inspired by the
4.4BSD make and include files, but aims to be portable and to conform to the
GNU standards for Makefile variables and targets.

%description -l de
Automake ist ein experimenteller Makefile-Generator, inspiriert durch die
4.4BSD-Make und Include-Dateien, der jedoch auf Portabilität und Konformität
mit den GNU-Standards für Makefile-Variable und Targets abzielt.

%description -l fr
automake est un générateur expérimental de makefiles. Il a été inspiré par
le make de BSD 4.4, mais se veut portable et conforme aux standards GNU pour
les variables et les cibles des makefiles.

%description -l pl
Automake jest eksperymentalnym generatorem plików Makefile'a. Narzêdzie to
jest wzorowane na make i plikach nag³ówków z systemu 4.4BSD. Umo¿liwia ono
generowanie plików Makefile w oderwaniu od platformy systemowej bêd±c
jednoce¶nie zgodnym ze standardami GNU.

%description -l tr
Automake deneysel bir Makefile üreticisidir. 4.4BSD make ve include
dosyalarýndan esinlenilmistir, ama amaç taþýnabilir olmak ve Makefile
deðiþkenleri ve hedefleri için GNU standartlarýna uyum göstermektir.

%prep
%setup -q
%patch0 -p1

%build
./configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

gzip -9nf $RPM_BUILD_ROOT/usr/info/automake*

%post
/sbin/install-info /usr/info/automake.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/info/automake.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) /usr/bin/*
/usr/info/automake*
%attr(-, root, root) /usr/share/*

%changelog
* Wed Jan 26 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4-1d]
- added Group(pl).

* Tue Dec 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3d-3]
- standarized {un}registering info pages (second try .. added
  automake-info.patch).

* Wed Dec 23 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3d-2]
- (waiting for new autoconf): fixed @SHELL@ bug.

* Sat Dec 19 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3d-1]
- updated URL,
- standarized {un}registering info pages.

* Sat Nov 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3b-1]
- changed base Source url,
- cosmetic changes in %post, %preun in {un}registering autoame info page,
- added URL.

* Sat Aug  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-5]
- modified pl translation,
- added -q %setup parameter,
- removed INSTALL and COPING from %doc (copyright statment is in Copyright
  field),
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- fixed %defattr macro,
- added using %%{name} and %%{version} macro in Source.

* Mon Jun 29 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3-4]
- added pl translation,
- build from non root's account,
- added %defattr support.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- updated to 1.3

* Tue Oct 28 1997 Cristian Gafton <gafton@redhat.com>
- added BuildRoot; added aclocal files

* Fri Oct 24 1997 Erik Troan <ewt@redhat.com>
- made it a noarch package

* Thu Oct 16 1997 Michael Fulbright <msf@redhat.com>
- Fixed some tag lines to conform to 5.0 guidelines.

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- updated to 1.2

* Wed Mar 5 1997 msf@redhat.com <Michael Fulbright>
- first version (1.0)

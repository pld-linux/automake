%include	/usr/lib/rpm/macros.perl
Summary:	GNU automake - Makefile configuration tools
Summary(de):	GNU automake - Makefile-Konfigurationstools
Summary(es):	GNU automake - herramientas de configuración de Makefile
Summary(fr):	automake de GNU - Outils de configuration des makefiles
Summary(pl):	GNU Automake - generator plików Makefile
Summary(pt_BR):	GNU automake - ferramentas de configuração de Makefile
Summary(ru):	GNU automake - ÉÎÓÔÒÕÍÅÎÔÙ ÄÌÑ Á×ÔÏÍÁÔÉÞÅÓËÏÊ ÇÅÎÅÒÁÃÉÉ Makefile'Ï×
Summary(tr):	Makefile yapýlandýrma araçlarý
Summary(uk):	GNU automake - ¦ÎÓÔÒÕÍÅÎÔÉ ÄÌÑ Á×ÔÏÍÁÔÉÞÎÏ§ ÇÅÎÅÒÁÃ¦§ Makefile'¦×
Name:		automake
Version:	1.6b
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Building
Source0:	ftp://sourceware.cygnus.com/pub/automake/%{name}-%{version}.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-regex.m4.patch
Patch3:		%{name}-no_versioned_dir.patch
URL:		http://sourceware.cygnus.com/automake/
BuildRequires:	autoconf >= 2.53b
BuildRequires:	rpm-perlprov
Requires(pre):	fileutils
Requires:	perl
Requires:	perl(File::Glob)
Conflicts:	autoconf < 2.52
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		_aclocaldir	%{_datadir}/aclocal

%description
Automake is an experimental Makefile generator. Automake was inspired
by the 4.4BSD make and include files, but aims to be portable and to
conform to the GNU standards for Makefile variables and targets.

%description -l de
Automake ist ein experimenteller Makefile-Generator, inspiriert durch
die 4.4BSD-Make und Include-Dateien, der jedoch auf Portabilität und
Konformität mit den GNU-Standards für Makefile-Variable und Targets
abzielt.

%description -l es
Automake es un creador experimental de Makefiles. Fue inspirado en el
4.4BSD make y incluye archivos, pero visa ser portátil y compatible
con los padrones GNU para variables y dianas de Makefile.

%description -l fr
automake est un générateur expérimental de makefiles. Il a été inspiré
par le make de BSD 4.4, mais se veut portable et conforme aux
standards GNU pour les variables et les cibles des makefiles.

%description -l pl
Automake jest eksperymentalnym generatorem plików Makefile'a.
Narzêdzie to jest wzorowane na make i plikach nag³ówkowych z systemu
4.4BSD. Umo¿liwia ono generowanie plików Makefile w oderwaniu od
platformy systemowej bêd±c jednocze¶nie zgodnym ze standardami GNU.

%description -l pt_BR
Automake é um gerador experimental de Makefiles. Ele foi inspirado
pelo 4.4BSD make e inclui arquivos, mas visa ser portável e compatível
com os padrões GNU para variáveis e alvos de Makefile.

%description -l ru
Automake - ÜÔÏ ÜËÓÐÅÒÉÍÅÎÔÁÌØÎÙÊ ÇÅÎÅÒÁÔÏÒ Makefile'Ï×. éÄÅÑ ÂÙÌÁ
ÎÁ×ÅÑÎÁ ÐÒÏÇÒÁÍÍÏÊ make É ÈÅÄÅÒÁÍÉ ÉÚ 4.4BSD, ÎÏ automake ÐÒÅÔÅÎÄÕÅÔ
ÎÁ ÔÏ, ÞÔÏÂÙ ÂÙÔØ ÐÏÒÔÁÂÅÌØÎÏÊ É ÓÏÏÔ×ÅÔÓÔ×Ï×ÁÔØ ÓÔÁÎÄÁÒÔÁÍ GNU ÎÁ
ÐÅÒÅÍÅÎÎÙÅ É ÃÅÌÉ Makefile'Ï×.

%description -l tr
Automake deneysel bir Makefile üreticisidir. 4.4BSD make ve include
dosyalarýndan esinlenilmistir, ama amaç taþýnabilir olmak ve Makefile
deðiþkenleri ve hedefleri için GNU standartlarýna uyum göstermektir.

%description -l uk
Automake - ÃÅ ÅËÓÐÅÒÉÍÅÎÔÁÌØÎÉÊ ÇÅÎÅÒÁÔÏÒ Makefile'¦×. ¶ÄÅÑ ÂÕÌÁ
ÎÁ×¦ÑÎÁ ÐÒÏÇÒÁÍÏÀ make ÔÁ ÈÅÄÅÒÁÍÉ Ú 4.4BSD, ÁÌÅ automake ÍÁ¤ ÚÁ Ã¦ÌØ
ÍÏÂ¦ÌØÎ¦ÓÔØ ÔÁ ×¦ÄÐÏ×¦ÄÎ¦ÓÔØ ÓÔÁÎÄÁÒÔÁÍ GNU ÎÁ ÚÍ¦ÎÎ¦ Ô¦ Ã¦Ì¦
Makefile'¦×.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgvdatadir=%{_datadir}/automake

install aclocal.1 automake.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/automake*

%{_aclocaldir}
%{_mandir}/man1/*

%dir %{_datadir}/automake
%{_datadir}/automake/am
%{_datadir}/automake/Automake
%{_datadir}/automake/COPYING
%{_datadir}/automake/INSTALL
%{_datadir}/automake/texinfo.tex
%{_datadir}/automake/ansi2knr*
%attr(755,root,root) %{_datadir}/automake/acinstall
%attr(755,root,root) %{_datadir}/automake/compile
%attr(755,root,root) %{_datadir}/automake/config.guess
%attr(755,root,root) %{_datadir}/automake/config.sub
%attr(755,root,root) %{_datadir}/automake/depcomp
%attr(755,root,root) %{_datadir}/automake/elisp-comp
%attr(755,root,root) %{_datadir}/automake/install-sh
%attr(755,root,root) %{_datadir}/automake/mdate-sh
%attr(755,root,root) %{_datadir}/automake/missing
%attr(755,root,root) %{_datadir}/automake/mkinstalldirs
%attr(755,root,root) %{_datadir}/automake/py-compile
%attr(755,root,root) %{_datadir}/automake/ylwrap

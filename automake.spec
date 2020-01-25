#
# Conditional build:
%bcond_with	bootstrap	# without full regeneration

Summary:	GNU automake - Makefile configuration tools
Summary(de.UTF-8):	GNU automake - Makefile-Konfigurationstools
Summary(es.UTF-8):	GNU automake - herramientas de configuración de Makefile
Summary(fr.UTF-8):	automake de GNU - Outils de configuration des makefiles
Summary(ko.UTF-8):	스스로 Makefile을 만들어주는 GNU 도구
Summary(pl.UTF-8):	GNU Automake - generator plików Makefile
Summary(pt_BR.UTF-8):	GNU automake - ferramentas de configuração de Makefile
Summary(ru.UTF-8):	GNU automake - инструменты для автоматической генерации Makefile'ов
Summary(tr.UTF-8):	Makefile yapılandırma araçları
Summary(uk.UTF-8):	GNU automake - інструменти для автоматичної генерації Makefile'ів
Name:		automake
Version:	1.16.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Development/Building
Source0:	http://ftp.gnu.org/gnu/automake/%{name}-%{version}.tar.xz
# Source0-md5:	53f38e7591fa57c3d2cee682be668e5b
Patch0:		%{name}-info.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-no_versioned_dir.patch
Patch3:		%{name}-morearchs.patch
Patch4:		revert-debian-python-hacks.patch
URL:		http://sources.redhat.com/automake/
BuildRequires:	autoconf >= 2.69
%if %{without bootstrap}
BuildRequires:	automake >= 1:1.14
%endif
BuildRequires:	help2man
BuildRequires:	rpm-perlprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.9
BuildRequires:	xz
Requires(pre):	fileutils
Requires:	filesystem >= 3.0-2
Requires:	perl(File::Glob)
%if %(%{__perl} -le 'use threads; print 1' || echo 0)
# required only if perl was built with threads
Requires:	perl(Thread::Queue)
Requires:	perl(threads)
%endif
Conflicts:	autoconf < 2.65
Conflicts:	libtool < 2:1.5-11
Conflicts:	texinfo < 4.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ver_maj		%(echo %{version} | cut -d. -f1-2)
%define		_enable_debug_packages	0

%description
Automake is an experimental Makefile generator. Automake was inspired
by the 4.4BSD make and include files, but aims to be portable and to
conform to the GNU standards for Makefile variables and targets.

%description -l de.UTF-8
Automake ist ein experimenteller Makefile-Generator, inspiriert durch
die 4.4BSD-Make und Include-Dateien, der jedoch auf Portabilität und
Konformität mit den GNU-Standards für Makefile-Variable und Targets
abzielt.

%description -l es.UTF-8
Automake es un creador experimental de Makefiles. Fue inspirado en el
4.4BSD make y incluye archivos, pero visa ser portátil y compatible
con los padrones GNU para variables y dianas de Makefile.

%description -l fr.UTF-8
automake est un générateur expérimental de makefiles. Il a été inspiré
par le make de BSD 4.4, mais se veut portable et conforme aux
standards GNU pour les variables et les cibles des makefiles.

%description -l pl.UTF-8
Automake jest eksperymentalnym generatorem plików Makefile'a.
Narzędzie to jest wzorowane na make i plikach nagłówkowych z systemu
4.4BSD. Umożliwia ono generowanie plików Makefile w oderwaniu od
platformy systemowej będąc jednocześnie zgodnym ze standardami GNU.

%description -l pt_BR.UTF-8
Automake é um gerador experimental de Makefiles. Ele foi inspirado
pelo 4.4BSD make e inclui arquivos, mas visa ser portável e compatível
com os padrões GNU para variáveis e alvos de Makefile.

%description -l ru.UTF-8
Automake - это экспериментальный генератор Makefile'ов. Идея была
навеяна программой make и хедерами из 4.4BSD, но automake претендует
на то, чтобы быть портабельной и соответствовать стандартам GNU на
переменные и цели Makefile'ов.

%description -l tr.UTF-8
Automake deneysel bir Makefile üreticisidir. 4.4BSD make ve include
dosyalarından esinlenilmistir, ama amaç taşınabilir olmak ve Makefile
değişkenleri ve hedefleri için GNU standartlarına uyum göstermektir.

%description -l uk.UTF-8
Automake - це експериментальний генератор Makefile'ів. Ідея була
навіяна програмою make та хедерами з 4.4BSD, але automake має за ціль
мобільність та відповідність стандартам GNU на змінні ті цілі
Makefile'ів.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%if %{without bootstrap}
# prepare temporary copy of m4 dir without amversion.m4 (which causes automake version check)
mkdir m4-tmp
cd m4-tmp
ln -s ../m4/[!a]*.m4 ../m4/a[!m]*.m4 .
%endif

%build
%if %{without bootstrap}
%{__aclocal} -I m4-tmp
%endif
%{__autoconf}
%if %{without bootstrap}
%{__automake}
%endif

%configure \
%if "%{_host_cpu}" != "x32"
	--host=%{_host} \
	--build=%{_host} \
%endif
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgvdatadir=%{_datadir}/automake

cp -a aclocal.1 automake.1 $RPM_BUILD_ROOT%{_mandir}/man1

# not needed when dir/files are handled by package system
%{__rm} $RPM_BUILD_ROOT%{_datadir}/aclocal/README

rm -f $RPM_BUILD_ROOT%{_infodir}/dir*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/aclocal*
%attr(755,root,root) %{_bindir}/automake*
%{_infodir}/automake.info*
%{_infodir}/automake-history.info*
%{_mandir}/man1/aclocal.1*
%{_mandir}/man1/aclocal-%{ver_maj}.1*
%{_mandir}/man1/automake.1*
%{_mandir}/man1/automake-%{ver_maj}.1*

%{_datadir}/aclocal-%{ver_maj}
%dir %{_datadir}/automake
%{_datadir}/automake/am
%{_datadir}/automake/Automake
%{_datadir}/automake/COPYING
%{_datadir}/automake/INSTALL
%{_datadir}/automake/texinfo.tex
%attr(755,root,root) %{_datadir}/automake/ar-lib
%attr(755,root,root) %{_datadir}/automake/compile
%attr(755,root,root) %{_datadir}/automake/config.guess
%attr(755,root,root) %{_datadir}/automake/config.sub
%attr(755,root,root) %{_datadir}/automake/depcomp
%attr(755,root,root) %{_datadir}/automake/install-sh
%attr(755,root,root) %{_datadir}/automake/mdate-sh
%attr(755,root,root) %{_datadir}/automake/missing
%attr(755,root,root) %{_datadir}/automake/mkinstalldirs
%attr(755,root,root) %{_datadir}/automake/py-compile
%attr(755,root,root) %{_datadir}/automake/tap-driver.sh
%attr(755,root,root) %{_datadir}/automake/test-driver
%attr(755,root,root) %{_datadir}/automake/ylwrap

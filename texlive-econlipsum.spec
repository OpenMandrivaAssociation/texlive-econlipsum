Name:		texlive-econlipsum
Version:	58390
Release:	1
Summary:	Generate sentences from economic articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/econlipsum
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/econlipsum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/econlipsum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/econlipsum.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is a blind text generator that ouputs sentences
inferred from abstracts of economic articles. All the
paragraphs are taken with permission from
https://ipsum.mwt.me/.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/econlipsum
%{_texmfdistdir}/tex/latex/econlipsum
%doc %{_texmfdistdir}/doc/latex/econlipsum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

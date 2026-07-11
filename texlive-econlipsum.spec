%global tl_name econlipsum
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8.2
Release:	%{tl_revision}.1
Summary:	Generate sentences from economic articles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/econlipsum
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/econlipsum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/econlipsum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/econlipsum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is a blind text generator that outputs sentences inferred
from abstracts of economic articles. All the paragraphs are taken with
permission from https://ipsum.mwt.me/.


%global tl_name translation-enumitem-de
%global tl_revision 24196

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Enumitem documentation, in German
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/enumitem/de
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-enumitem-de.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-enumitem-de.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a translation of the manual for enumitem.


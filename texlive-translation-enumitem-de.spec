Name:		texlive-translation-enumitem-de
Version:	24196
Release:	2
Summary:	Enumitem documentation, in German
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/enumitem/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-enumitem-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-enumitem-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a translation of the manual for enumitem.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-enumitem-de/enumitem-de.pdf
%doc %{_texmfdistdir}/doc/latex/translation-enumitem-de/enumitem-de.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

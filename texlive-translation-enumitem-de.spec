# revision 24196
# category Package
# catalog-ctan /info/translations/enumitem/de
# catalog-date 2011-10-04 22:25:03 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-translation-enumitem-de
Version:	20111004
Release:	1
Summary:	Enumitem documentation, in German
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/enumitem/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-enumitem-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-enumitem-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a translation of the manual for enumitem.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-enumitem-de/enumitem-de.pdf
%doc %{_texmfdistdir}/doc/latex/translation-enumitem-de/enumitem-de.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

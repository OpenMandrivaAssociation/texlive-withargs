# revision 31906
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-withargs
Version:	20131201
Release:	9
Summary:	TeXLive withargs package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/withargs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/withargs.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive withargs package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/withargs/withargs-dry.sty
%{_texmfdistdir}/tex/latex/withargs/withargs-packagedoc.cls
%{_texmfdistdir}/tex/latex/withargs/withargs.sty
%doc %{_texmfdistdir}/doc/latex/withargs/README
%doc %{_texmfdistdir}/doc/latex/withargs/withargs.pdf
%doc %{_texmfdistdir}/doc/latex/withargs/withargs.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

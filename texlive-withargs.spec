Name:		texlive-withargs
Version:	52641
Release:	2
Summary:	TeXLive withargs package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/withargs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/withargs.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

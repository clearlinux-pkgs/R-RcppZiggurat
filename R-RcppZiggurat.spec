#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RcppZiggurat
Version  : 0.1.5
Release  : 4
URL      : https://cran.r-project.org/src/contrib/RcppZiggurat_0.1.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RcppZiggurat_0.1.5.tar.gz
Summary  : 'Rcpp' Integration of Different "Ziggurat" Normal RNG
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RcppZiggurat-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppGSL
BuildRequires : R-Rcpp
BuildRequires : R-RcppGSL
BuildRequires : buildreq-R
BuildRequires : gsl-dev

%description
numbers, originally proposed by Marsaglia and Tsang (2000,

%package lib
Summary: lib components for the R-RcppZiggurat package.
Group: Libraries

%description lib
lib components for the R-RcppZiggurat package.


%prep
%setup -q -c -n RcppZiggurat
cd %{_builddir}/RcppZiggurat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589570648

%install
export SOURCE_DATE_EPOCH=1589570648
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppZiggurat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppZiggurat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppZiggurat
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RcppZiggurat || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppZiggurat/DESCRIPTION
/usr/lib64/R/library/RcppZiggurat/INDEX
/usr/lib64/R/library/RcppZiggurat/Meta/Rd.rds
/usr/lib64/R/library/RcppZiggurat/Meta/demo.rds
/usr/lib64/R/library/RcppZiggurat/Meta/features.rds
/usr/lib64/R/library/RcppZiggurat/Meta/hsearch.rds
/usr/lib64/R/library/RcppZiggurat/Meta/links.rds
/usr/lib64/R/library/RcppZiggurat/Meta/nsInfo.rds
/usr/lib64/R/library/RcppZiggurat/Meta/package.rds
/usr/lib64/R/library/RcppZiggurat/Meta/vignette.rds
/usr/lib64/R/library/RcppZiggurat/NAMESPACE
/usr/lib64/R/library/RcppZiggurat/NEWS.Rd
/usr/lib64/R/library/RcppZiggurat/R/RcppZiggurat
/usr/lib64/R/library/RcppZiggurat/R/RcppZiggurat.rdb
/usr/lib64/R/library/RcppZiggurat/R/RcppZiggurat.rdx
/usr/lib64/R/library/RcppZiggurat/code/rnorrexp.c
/usr/lib64/R/library/RcppZiggurat/demo/benchmark.R
/usr/lib64/R/library/RcppZiggurat/demo/chisqTest.R
/usr/lib64/R/library/RcppZiggurat/demo/normalTest.R
/usr/lib64/R/library/RcppZiggurat/demo/standardTest.R
/usr/lib64/R/library/RcppZiggurat/doc/RcppZiggurat.R
/usr/lib64/R/library/RcppZiggurat/doc/RcppZiggurat.Rmd
/usr/lib64/R/library/RcppZiggurat/doc/RcppZiggurat.pdf
/usr/lib64/R/library/RcppZiggurat/doc/index.html
/usr/lib64/R/library/RcppZiggurat/help/AnIndex
/usr/lib64/R/library/RcppZiggurat/help/RcppZiggurat.rdb
/usr/lib64/R/library/RcppZiggurat/help/RcppZiggurat.rdx
/usr/lib64/R/library/RcppZiggurat/help/aliases.rds
/usr/lib64/R/library/RcppZiggurat/help/paths.rds
/usr/lib64/R/library/RcppZiggurat/html/00Index.html
/usr/lib64/R/library/RcppZiggurat/html/R.css
/usr/lib64/R/library/RcppZiggurat/include/Zigg.h
/usr/lib64/R/library/RcppZiggurat/include/Ziggurat.h
/usr/lib64/R/library/RcppZiggurat/include/ZigguratGSL.h
/usr/lib64/R/library/RcppZiggurat/include/ZigguratGretl.h
/usr/lib64/R/library/RcppZiggurat/include/ZigguratLZLLV.h
/usr/lib64/R/library/RcppZiggurat/include/ZigguratMT.h
/usr/lib64/R/library/RcppZiggurat/include/ZigguratQL.h
/usr/lib64/R/library/RcppZiggurat/include/ZigguratQL_R.h
/usr/lib64/R/library/RcppZiggurat/include/ZigguratR.h
/usr/lib64/R/library/RcppZiggurat/include/ZigguratV1.h
/usr/lib64/R/library/RcppZiggurat/include/ZigguratV1b.h
/usr/lib64/R/library/RcppZiggurat/include/mt32wrapper.h
/usr/lib64/R/library/RcppZiggurat/tests/zigguratTest.R
/usr/lib64/R/library/RcppZiggurat/tests/zigguratTest.Rout.save
/usr/lib64/R/library/RcppZiggurat/tests/zigguratTestAll.R
/usr/lib64/R/library/RcppZiggurat/tests/zigguratTestAll.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppZiggurat/libs/RcppZiggurat.so
/usr/lib64/R/library/RcppZiggurat/libs/RcppZiggurat.so.avx2

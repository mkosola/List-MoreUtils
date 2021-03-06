# This spec is from Fedora adapted to Mer
Name:           perl-List-MoreUtils
Version:        0.33
Release:        1
Summary:        Provide the stuff missing in List::Util
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/List-MoreUtils/
Source0:        List-MoreUtils-%{version}.tar.gz
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)

%description
List::MoreUtils provides some trivial but commonly needed functionality
on lists that is not going to go into List::Util.

%prep
%setup -q -n List-MoreUtils-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc Changes README LICENSE
%{perl_vendorarch}/List/
%{perl_vendorarch}/auto/List/
%{_mandir}/man3/List::MoreUtils.3pm*

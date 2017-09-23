#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test2-Suite
Version  : 0.000077
Release  : 11
URL      : https://www.cpan.org/authors/id/E/EX/EXODIST/Test2-Suite-0.000077.tar.gz
Source0  : https://www.cpan.org/authors/id/E/EX/EXODIST/Test2-Suite-0.000077.tar.gz
Summary  : 'Distribution with a rich set of tools built upon the Test2 framework.'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Test2-Suite-doc
BuildRequires : perl(Importer)
BuildRequires : perl(Sub::Info)
BuildRequires : perl(Term::Table)

%description
NAME
Test2::Suite - Distribution with a rich set of tools built upon the
Test2 framework.

%package doc
Summary: doc components for the perl-Test2-Suite package.
Group: Documentation

%description doc
doc components for the perl-Test2-Suite package.


%prep
%setup -q -n Test2-Suite-0.000077

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Test2/Bundle.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Bundle/Extended.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Bundle/More.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Bundle/Simple.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Array.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Bag.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Base.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Bool.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Custom.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/DeepRef.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Delta.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Event.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/EventMeta.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Hash.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Meta.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Negatable.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Number.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Object.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/OrderedSubset.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Pattern.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Ref.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Regex.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Scalar.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Set.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/String.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Undef.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Compare/Wildcard.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Event/Times.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Mock.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Plugin.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Plugin/BailOnFail.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Plugin/DieOnFail.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Plugin/ExitSummary.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Plugin/SRand.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Plugin/Times.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Plugin/UTF8.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Require.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Require/AuthorTesting.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Require/EnvVar.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Require/Fork.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Require/Module.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Require/Perl.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Require/RealFork.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Require/Threads.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Suite.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Todo.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Basic.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Class.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/ClassicCompare.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Compare.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Defer.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Encoding.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Event.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Exception.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Exports.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/GenTemp.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Grab.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Mock.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Ref.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Subtest.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Target.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Tools/Warnings.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Util/Grabber.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Util/Ref.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Util/Stash.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Util/Sub.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Util/Table.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Util/Table/Cell.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Util/Table/LineBreak.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Util/Term.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/Util/Times.pm
/usr/lib/perl5/site_perl/5.26.1/Test2/V0.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

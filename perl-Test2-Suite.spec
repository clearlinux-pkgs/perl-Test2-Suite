#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test2-Suite
Version  : 0.000147
Release  : 77
URL      : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Suite-0.000147.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Suite-0.000147.tar.gz
Summary  : 'Distribution with a rich set of tools built upon the Test2 framework.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test2-Suite-license = %{version}-%{release}
Requires: perl-Test2-Suite-perl = %{version}-%{release}
Requires: perl(Module::Pluggable)
Requires: perl(Scope::Guard)
Requires: perl(Term::Table)
BuildRequires : buildreq-cpan
BuildRequires : perl(Importer)
BuildRequires : perl(Module::Pluggable)
BuildRequires : perl(Scope::Guard)
BuildRequires : perl(Sub::Info)
BuildRequires : perl(Term::Table)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Test2::Suite - Distribution with a rich set of tools built upon the
Test2 framework.

%package dev
Summary: dev components for the perl-Test2-Suite package.
Group: Development
Provides: perl-Test2-Suite-devel = %{version}-%{release}
Requires: perl-Test2-Suite = %{version}-%{release}

%description dev
dev components for the perl-Test2-Suite package.


%package license
Summary: license components for the perl-Test2-Suite package.
Group: Default

%description license
license components for the perl-Test2-Suite package.


%package perl
Summary: perl components for the perl-Test2-Suite package.
Group: Default
Requires: perl-Test2-Suite = %{version}-%{release}

%description perl
perl components for the perl-Test2-Suite package.


%prep
%setup -q -n Test2-Suite-0.000147
cd %{_builddir}/Test2-Suite-0.000147

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test2-Suite
cp %{_builddir}/Test2-Suite-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test2-Suite/46e5653a9b161b127e04780a2ed6d8b1531663e8 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test2::AsyncSubtest.3
/usr/share/man/man3/Test2::AsyncSubtest::Event::Attach.3
/usr/share/man/man3/Test2::AsyncSubtest::Event::Detach.3
/usr/share/man/man3/Test2::AsyncSubtest::Hub.3
/usr/share/man/man3/Test2::Bundle.3
/usr/share/man/man3/Test2::Bundle::Extended.3
/usr/share/man/man3/Test2::Bundle::More.3
/usr/share/man/man3/Test2::Bundle::Simple.3
/usr/share/man/man3/Test2::Compare.3
/usr/share/man/man3/Test2::Compare::Array.3
/usr/share/man/man3/Test2::Compare::Bag.3
/usr/share/man/man3/Test2::Compare::Base.3
/usr/share/man/man3/Test2::Compare::Bool.3
/usr/share/man/man3/Test2::Compare::Custom.3
/usr/share/man/man3/Test2::Compare::DeepRef.3
/usr/share/man/man3/Test2::Compare::Delta.3
/usr/share/man/man3/Test2::Compare::Event.3
/usr/share/man/man3/Test2::Compare::EventMeta.3
/usr/share/man/man3/Test2::Compare::Float.3
/usr/share/man/man3/Test2::Compare::Hash.3
/usr/share/man/man3/Test2::Compare::Isa.3
/usr/share/man/man3/Test2::Compare::Meta.3
/usr/share/man/man3/Test2::Compare::Negatable.3
/usr/share/man/man3/Test2::Compare::Number.3
/usr/share/man/man3/Test2::Compare::Object.3
/usr/share/man/man3/Test2::Compare::OrderedSubset.3
/usr/share/man/man3/Test2::Compare::Pattern.3
/usr/share/man/man3/Test2::Compare::Ref.3
/usr/share/man/man3/Test2::Compare::Regex.3
/usr/share/man/man3/Test2::Compare::Scalar.3
/usr/share/man/man3/Test2::Compare::Set.3
/usr/share/man/man3/Test2::Compare::String.3
/usr/share/man/man3/Test2::Compare::Undef.3
/usr/share/man/man3/Test2::Compare::Wildcard.3
/usr/share/man/man3/Test2::Manual.3
/usr/share/man/man3/Test2::Manual::Anatomy.3
/usr/share/man/man3/Test2::Manual::Anatomy::API.3
/usr/share/man/man3/Test2::Manual::Anatomy::Context.3
/usr/share/man/man3/Test2::Manual::Anatomy::EndToEnd.3
/usr/share/man/man3/Test2::Manual::Anatomy::Event.3
/usr/share/man/man3/Test2::Manual::Anatomy::Hubs.3
/usr/share/man/man3/Test2::Manual::Anatomy::IPC.3
/usr/share/man/man3/Test2::Manual::Anatomy::Utilities.3
/usr/share/man/man3/Test2::Manual::Concurrency.3
/usr/share/man/man3/Test2::Manual::Contributing.3
/usr/share/man/man3/Test2::Manual::Testing.3
/usr/share/man/man3/Test2::Manual::Testing::Introduction.3
/usr/share/man/man3/Test2::Manual::Testing::Migrating.3
/usr/share/man/man3/Test2::Manual::Testing::Planning.3
/usr/share/man/man3/Test2::Manual::Testing::Todo.3
/usr/share/man/man3/Test2::Manual::Tooling.3
/usr/share/man/man3/Test2::Manual::Tooling::FirstTool.3
/usr/share/man/man3/Test2::Manual::Tooling::Formatter.3
/usr/share/man/man3/Test2::Manual::Tooling::Nesting.3
/usr/share/man/man3/Test2::Manual::Tooling::Plugin::TestExit.3
/usr/share/man/man3/Test2::Manual::Tooling::Plugin::TestingDone.3
/usr/share/man/man3/Test2::Manual::Tooling::Plugin::ToolCompletes.3
/usr/share/man/man3/Test2::Manual::Tooling::Plugin::ToolStarts.3
/usr/share/man/man3/Test2::Manual::Tooling::Subtest.3
/usr/share/man/man3/Test2::Manual::Tooling::TestBuilder.3
/usr/share/man/man3/Test2::Manual::Tooling::Testing.3
/usr/share/man/man3/Test2::Mock.3
/usr/share/man/man3/Test2::Plugin.3
/usr/share/man/man3/Test2::Plugin::BailOnFail.3
/usr/share/man/man3/Test2::Plugin::DieOnFail.3
/usr/share/man/man3/Test2::Plugin::ExitSummary.3
/usr/share/man/man3/Test2::Plugin::SRand.3
/usr/share/man/man3/Test2::Plugin::Times.3
/usr/share/man/man3/Test2::Plugin::UTF8.3
/usr/share/man/man3/Test2::Require.3
/usr/share/man/man3/Test2::Require::AuthorTesting.3
/usr/share/man/man3/Test2::Require::EnvVar.3
/usr/share/man/man3/Test2::Require::Fork.3
/usr/share/man/man3/Test2::Require::Module.3
/usr/share/man/man3/Test2::Require::Perl.3
/usr/share/man/man3/Test2::Require::RealFork.3
/usr/share/man/man3/Test2::Require::Threads.3
/usr/share/man/man3/Test2::Suite.3
/usr/share/man/man3/Test2::Todo.3
/usr/share/man/man3/Test2::Tools.3
/usr/share/man/man3/Test2::Tools::AsyncSubtest.3
/usr/share/man/man3/Test2::Tools::Basic.3
/usr/share/man/man3/Test2::Tools::Class.3
/usr/share/man/man3/Test2::Tools::ClassicCompare.3
/usr/share/man/man3/Test2::Tools::Compare.3
/usr/share/man/man3/Test2::Tools::Defer.3
/usr/share/man/man3/Test2::Tools::Encoding.3
/usr/share/man/man3/Test2::Tools::Event.3
/usr/share/man/man3/Test2::Tools::Exception.3
/usr/share/man/man3/Test2::Tools::Exports.3
/usr/share/man/man3/Test2::Tools::GenTemp.3
/usr/share/man/man3/Test2::Tools::Grab.3
/usr/share/man/man3/Test2::Tools::Mock.3
/usr/share/man/man3/Test2::Tools::Ref.3
/usr/share/man/man3/Test2::Tools::Refcount.3
/usr/share/man/man3/Test2::Tools::Spec.3
/usr/share/man/man3/Test2::Tools::Subtest.3
/usr/share/man/man3/Test2::Tools::Target.3
/usr/share/man/man3/Test2::Tools::Tester.3
/usr/share/man/man3/Test2::Tools::Warnings.3
/usr/share/man/man3/Test2::Util::Grabber.3
/usr/share/man/man3/Test2::Util::Ref.3
/usr/share/man/man3/Test2::Util::Stash.3
/usr/share/man/man3/Test2::Util::Sub.3
/usr/share/man/man3/Test2::Util::Table.3
/usr/share/man/man3/Test2::Util::Table::LineBreak.3
/usr/share/man/man3/Test2::Util::Times.3
/usr/share/man/man3/Test2::V0.3
/usr/share/man/man3/Test2::Workflow.3
/usr/share/man/man3/Test2::Workflow::BlockBase.3
/usr/share/man/man3/Test2::Workflow::Build.3
/usr/share/man/man3/Test2::Workflow::Runner.3
/usr/share/man/man3/Test2::Workflow::Task.3
/usr/share/man/man3/Test2::Workflow::Task::Action.3
/usr/share/man/man3/Test2::Workflow::Task::Group.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test2-Suite/46e5653a9b161b127e04780a2ed6d8b1531663e8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

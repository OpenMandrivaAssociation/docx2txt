Summary: cli tool to convert docx to ascii txt files
Name: docx2txt
Version: 1.2
Release: 2
Group: Office
License: GPLv3
Url: http://sourceforge.net/projects/docx2txt
Source0: http://downloads.sourceforge.net/project/docx2txt/docx2txt/v1.2/%{name}-%{version}.tgz
BuildArch: noarch
Requires: unzip

%description
Docx2txt is a Perl based command-line tool
to convert Microsoft docx documents to
(ASCII) text files, preserving some formatting
and document information (which MS
text conversion drops) along with appropriate
character conversions.

%prep
%setup -q

%build


%install
export BINDIR="%{buildroot}%{_bindir}"
export CONFIGDIR="%{buildroot}%{_sysconfdir}"
make INSTALLDIR=%{buildroot}%{_bindir}
mv %{buildroot}%{_bindir}/docx2txt.sh %{buildroot}%{_bindir}/docx2txt
rm -f %{buildroot}%{_sysconfdir}/docx2txt.config

%files
%doc ChangeLog README COPYING
%{_bindir}/%{name}
%{_bindir}/docx2txt.pl


%changelog
* Sun Jan 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2-1
+ Revision: 761647
- version update 1.2

* Sat Dec 17 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.1-1
+ Revision: 743394
- imported package docx2txt


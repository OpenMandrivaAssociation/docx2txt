Summary: cli tool to convert docx to ascii txt files
Name: docx2txt
Version: 1.1
Release: 1
Group: Office
License: GPLv3
Url: http://sourceforge.net/projects/docx2txt
Source0: http://downloads.sourceforge.net/project/docx2txt/docx2txt/v1.0/%{name}-%{version}.tgz
BuildArch: noarch
Requires: unzip

%description
Docx2txt is a Perl based command-line tool to convert Microsoft docx documents to
(ASCII) text files, preserving some formatting and document information (which MS
text conversion drops) along with appropriate character conversions.

%prep
%setup -q

%build


%install
#%makeinstall_std %{buildroot}%{_bindir}

make INSTALLDIR=%{buildroot}%{_bindir}
mv %{buildroot}%{_bindir}/docx2txt.sh %{buildroot}%{_bindir}/docx2txt
rm -f %{buildroot}%{_bindir}/docx2txt.config

%files
%doc ChangeLog README COPYING
%{_bindir}/%{name}
%{_bindir}/docx2txt.pl

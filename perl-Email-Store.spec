#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Store
Summary:	Email::Store - framework for database-backed email storage
Summary(pl):	Email::Store - szkielet przechowywania poczty w bazie danych
Name:		perl-Email-Store
Version:	0.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eeca6f779ee5a9276ff2e074fe1a7990
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Cache
BuildRequires:	perl-Class-DBI >= 0.9
BuildRequires:	perl-Class-DBI-DATA-Schema
BuildRequires:	perl-DBD-SQLite
BuildRequires:	perl-Email-Address >= 1.80
BuildRequires:	perl-Email-MessageID
BuildRequires:	perl-Email-MIME >= 1.8
BuildRequires:	perl-Email-MIME-Attachment-Stripper >= 1.1
BuildRequires:	perl-Email-Simple >= 1.92
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-Mail-ListDetector >= 0.31
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-Module-Pluggable >= 2.6
BuildRequires:	perl-Module-Pluggable-Ordered >= 1
BuildRequires:	perl-SQL-Translator
BuildRequires:	perl-Time-Piece
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Store is the ideal basis for any application which needs to
deal with databases of email: archiving, searching, or even storing
mail for implementing IMAP or POP3 servers.

Email::Store itself is a very lightweight framework, meaning it does
not provide very much functionality itself; in effect, it is merely a
Class::DBI interface to a database schema which is designed for
storing email. Incidentally, if you don't know much about Class::DBI,
you're going to need to in order to get much out of this.

Despite its minimalist nature, Email::Store is incredibly powerful.
Its power comes from its extensibility, through plugin modules and
hooks which allow you to add new database tables and concepts to the
system, and so access the mail store from a "different direction". In
a sense, Email::Store is a blank canvas, onto which you can pick and
choose (or even write!) the plugins which you want for your
application.

For instance, the core Email::Store::Entity plugin module addresses
the idea of "people" in the email universe, allowing you to search for
mails to or from particular people; (despite their changing names or
email addresses) Email::Store::Thread interfaces Email::Store to
Mail::Thread allowing you to navigate mails by their position in a
mail thread; the planned non-core Email::Store::Plucene module plugs
into the indexing process and stores information about emails in a
Plucene search index for quick retrieval later, and so on.

%description -l pl
Email::Store to idealna podstawa dla ka�dej aplikacji potrzebuj�cej
wsp�pracowa� z bazami danych list�w: archiwizowaniem,
przeszukiwaniem czy nawet przechowywaniem poczty przy implementowaniu
serwer�w IMAP lub POP3.

Sam Email::Store jest bardzo lekkim szkieletem, co znaczy, �e sam w
sobie nie dostarcza zbyt du�ej funkcjonalno�ci. W efekcie jest jedynie
interfejsem Class::DBI do schematu bazy danych zaprojektowanego do
przechowywania poczty. Przypadkowo, je�li programista nie wie zbyt
du�o o Class::DBI, musi si� troch� dowiedzie�, aby skorzysta� z
Email::Store.

Pomimo swojej minimalistycznej natury Email::Store jest zadziwiaj�co
pot�ny. Jego pot�ga wynika z rozszerzalno�ci poprzez modu�y wtyczek i
punkty zaczepienia pozwalaj�ce na dodawanie nowych tabel i idei baz
danych do systemu oraz dost�p do zasob�w pocztowych z "innej strony".
W tym sensie Email::Store to czyste p��tno, na kt�rym mo�na umieszcza�
wybrane (a nawet napisane przez siebie) wtyczki, kt�re chcemy u�y� we
w�asnej aplikacji.

Na przyk�ad, podstawowy modu� wtyczki Email::Store::Entity przedstawia
ide� "ludzi" w �wiecie poczty elektronicznej, pozwalaj�c wyszukiwa�
listy do lub od okre�lonych os�b (pomimo zmieniania przez nich imion
czy adres�w pocztowych). Email::Store::Thread ��czy Email::Store z
Email::Thread pozwalaj�c na nawigowanie poprzez listy po ich pozycji w
w�tku; planowany dodatkowy modu� Email::Store::Plucene pod��cza si� do
procesu indeksowania i przechowuje informacje o listach w indeksie
wyszukiwarki Plucene w celu szybszego wyszukiwania ich p�niej... i
tak dalej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes mailstore.sql
%{perl_vendorlib}/Email/*.pm
%{perl_vendorlib}/Email/Store
%{_mandir}/man3/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kmail
Version  : 20.12.1
Release  : 28
URL      : https://download.kde.org/stable/release-service/20.12.1/src/kmail-20.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.1/src/kmail-20.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.1/src/kmail-20.12.1.tar.xz.sig
Summary  : KDE mail client
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 GPL-3.0 LGPL-2.0
Requires: kmail-bin = %{version}-%{release}
Requires: kmail-data = %{version}-%{release}
Requires: kmail-lib = %{version}-%{release}
Requires: kmail-license = %{version}-%{release}
Requires: kmail-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : akonadi-search-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gpgme-dev
BuildRequires : grantleetheme-dev
BuildRequires : kbookmarks-dev
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcmutils-dev
BuildRequires : kcodecs-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcontacts-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdepim-apps-libs-dev
BuildRequires : kdoctools-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kldap-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : knotifications-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kontactinterface-dev
BuildRequires : kparts-dev
BuildRequires : kpimtextedit-dev
BuildRequires : kservice-dev
BuildRequires : ktextwidgets-dev
BuildRequires : ktnef-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : kxmlgui-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libgravatar-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : libksieve-dev
BuildRequires : mailcommon-dev
BuildRequires : messagelib-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtwebengine-dev
BuildRequires : sonnet-dev
BuildRequires : syntax-highlighting-dev

%description
No detailed description available

%package bin
Summary: bin components for the kmail package.
Group: Binaries
Requires: kmail-data = %{version}-%{release}
Requires: kmail-license = %{version}-%{release}

%description bin
bin components for the kmail package.


%package data
Summary: data components for the kmail package.
Group: Data

%description data
data components for the kmail package.


%package doc
Summary: doc components for the kmail package.
Group: Documentation

%description doc
doc components for the kmail package.


%package lib
Summary: lib components for the kmail package.
Group: Libraries
Requires: kmail-data = %{version}-%{release}
Requires: kmail-license = %{version}-%{release}

%description lib
lib components for the kmail package.


%package license
Summary: license components for the kmail package.
Group: Default

%description license
license components for the kmail package.


%package locales
Summary: locales components for the kmail package.
Group: Default

%description locales
locales components for the kmail package.


%prep
%setup -q -n kmail-20.12.1
cd %{_builddir}/kmail-20.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610068486
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1610068486
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmail
cp %{_builddir}/kmail-20.12.1/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kmail/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/kmail-20.12.1/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kmail/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kmail-20.12.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmail/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kmail-20.12.1/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kmail/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kmail-20.12.1/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kmail/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kmail-20.12.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmail/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kmail-20.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kmail/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kmail-20.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kmail/7d9831e05094ce723947d729c2a46a09d6e90275
pushd clr-build
%make_install
popd
%find_lang akonadi_archivemail_agent
%find_lang akonadi_followupreminder_agent
%find_lang akonadi_mailfilter_agent
%find_lang akonadi_sendlater_agent
%find_lang kmail
%find_lang ktnef
%find_lang akonadi_unifiedmailbox_agent
%find_lang kmail-refresh-settings

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/akonadi_archivemail_agent
/usr/bin/akonadi_followupreminder_agent
/usr/bin/akonadi_mailfilter_agent
/usr/bin/akonadi_sendlater_agent
/usr/bin/akonadi_unifiedmailbox_agent
/usr/bin/kmail
/usr/bin/kmail-refresh-settings
/usr/bin/ktnef

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/agents/archivemailagent.desktop
/usr/share/akonadi/agents/followupreminder.desktop
/usr/share/akonadi/agents/mailfilteragent.desktop
/usr/share/akonadi/agents/sendlateragent.desktop
/usr/share/akonadi/agents/unifiedmailboxagent.desktop
/usr/share/applications/kmail_view.desktop
/usr/share/applications/org.kde.kmail-refresh-settings.desktop
/usr/share/applications/org.kde.kmail2.desktop
/usr/share/applications/org.kde.ktnef.desktop
/usr/share/config.kcfg/archivemailagentsettings.kcfg
/usr/share/config.kcfg/kmail.kcfg
/usr/share/dbus-1/interfaces/org.kde.kmail.kmail.xml
/usr/share/dbus-1/interfaces/org.kde.kmail.kmailpart.xml
/usr/share/dbus-1/services/org.kde.kmail.service
/usr/share/icons/breeze-dark/16x16/emblems/gpg-key-trust-level-0.svg
/usr/share/icons/breeze-dark/16x16/emblems/gpg-key-trust-level-1.svg
/usr/share/icons/breeze-dark/16x16/emblems/gpg-key-trust-level-2.svg
/usr/share/icons/breeze-dark/16x16/emblems/gpg-key-trust-level-3.svg
/usr/share/icons/breeze-dark/16x16/emblems/gpg-key-trust-level-4.svg
/usr/share/icons/breeze-dark/22x22/emblems/gpg-key-trust-level-0.svg
/usr/share/icons/breeze-dark/22x22/emblems/gpg-key-trust-level-1.svg
/usr/share/icons/breeze-dark/22x22/emblems/gpg-key-trust-level-2.svg
/usr/share/icons/breeze-dark/22x22/emblems/gpg-key-trust-level-3.svg
/usr/share/icons/breeze-dark/22x22/emblems/gpg-key-trust-level-4.svg
/usr/share/icons/breeze-dark/8x8/emblems/gpg-key-trust-level-0.svg
/usr/share/icons/breeze-dark/8x8/emblems/gpg-key-trust-level-1.svg
/usr/share/icons/breeze-dark/8x8/emblems/gpg-key-trust-level-2.svg
/usr/share/icons/breeze-dark/8x8/emblems/gpg-key-trust-level-3.svg
/usr/share/icons/breeze-dark/8x8/emblems/gpg-key-trust-level-4.svg
/usr/share/icons/hicolor/128x128/apps/kmail.png
/usr/share/icons/hicolor/16x16/apps/kmail.png
/usr/share/icons/hicolor/16x16/emblems/gpg-key-trust-level-0.svg
/usr/share/icons/hicolor/16x16/emblems/gpg-key-trust-level-1.svg
/usr/share/icons/hicolor/16x16/emblems/gpg-key-trust-level-2.svg
/usr/share/icons/hicolor/16x16/emblems/gpg-key-trust-level-3.svg
/usr/share/icons/hicolor/16x16/emblems/gpg-key-trust-level-4.svg
/usr/share/icons/hicolor/22x22/actions/ktnef_extract_all_to.png
/usr/share/icons/hicolor/22x22/actions/ktnef_extract_to.png
/usr/share/icons/hicolor/22x22/apps/kmail.png
/usr/share/icons/hicolor/22x22/emblems/gpg-key-trust-level-0.svg
/usr/share/icons/hicolor/22x22/emblems/gpg-key-trust-level-1.svg
/usr/share/icons/hicolor/22x22/emblems/gpg-key-trust-level-2.svg
/usr/share/icons/hicolor/22x22/emblems/gpg-key-trust-level-3.svg
/usr/share/icons/hicolor/22x22/emblems/gpg-key-trust-level-4.svg
/usr/share/icons/hicolor/32x32/apps/kmail.png
/usr/share/icons/hicolor/48x48/apps/kmail.png
/usr/share/icons/hicolor/48x48/apps/ktnef.png
/usr/share/icons/hicolor/64x64/apps/kmail.png
/usr/share/icons/hicolor/8x8/emblems/gpg-key-trust-level-0.svg
/usr/share/icons/hicolor/8x8/emblems/gpg-key-trust-level-1.svg
/usr/share/icons/hicolor/8x8/emblems/gpg-key-trust-level-2.svg
/usr/share/icons/hicolor/8x8/emblems/gpg-key-trust-level-3.svg
/usr/share/icons/hicolor/8x8/emblems/gpg-key-trust-level-4.svg
/usr/share/icons/hicolor/scalable/apps/kmail.svg
/usr/share/kconf_update/kmail-15.08-kickoff.sh
/usr/share/kconf_update/kmail.upd
/usr/share/kconf_update/kmail2.sh
/usr/share/kconf_update/kmail2.upd
/usr/share/kmail2/pics/pgp-keys.png
/usr/share/knotifications5/akonadi_archivemail_agent.notifyrc
/usr/share/knotifications5/akonadi_followupreminder_agent.notifyrc
/usr/share/knotifications5/akonadi_mailfilter_agent.notifyrc
/usr/share/knotifications5/akonadi_sendlater_agent.notifyrc
/usr/share/knotifications5/kmail2.notifyrc
/usr/share/kontact/ksettingsdialog/kmail.setdlg
/usr/share/kontact/ksettingsdialog/summary.setdlg
/usr/share/kservices5/kcmkmailsummary.desktop
/usr/share/kservices5/kcmkontactsummary.desktop
/usr/share/kservices5/kmail_config_accounts.desktop
/usr/share/kservices5/kmail_config_appearance.desktop
/usr/share/kservices5/kmail_config_composer.desktop
/usr/share/kservices5/kmail_config_misc.desktop
/usr/share/kservices5/kmail_config_plugins.desktop
/usr/share/kservices5/kmail_config_security.desktop
/usr/share/kservices5/kontact/kmailplugin.desktop
/usr/share/kservices5/kontact/summaryplugin.desktop
/usr/share/kxmlgui5/kontactsummary/kontactsummary_part.rc
/usr/share/metainfo/org.kde.kmail2.appdata.xml
/usr/share/qlogging-categories5/kmail.categories
/usr/share/qlogging-categories5/kmail.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/akonadi_archivemail_agent/add-archive-mail.png
/usr/share/doc/HTML/ca/akonadi_archivemail_agent/configure-archive-mail-agent.png
/usr/share/doc/HTML/ca/akonadi_archivemail_agent/index.cache.bz2
/usr/share/doc/HTML/ca/akonadi_archivemail_agent/index.docbook
/usr/share/doc/HTML/ca/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/ca/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/ca/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/ca/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/ca/akonadi_sendlater_agent/sendlateragent-configure.png
/usr/share/doc/HTML/ca/akonadi_sendlater_agent/sendlateragent-dialog.png
/usr/share/doc/HTML/ca/kmail2/configure.docbook
/usr/share/doc/HTML/ca/kmail2/credits-and-licenses.docbook
/usr/share/doc/HTML/ca/kmail2/faq.docbook
/usr/share/doc/HTML/ca/kmail2/getting-started.docbook
/usr/share/doc/HTML/ca/kmail2/index.cache.bz2
/usr/share/doc/HTML/ca/kmail2/index.docbook
/usr/share/doc/HTML/ca/kmail2/intro.docbook
/usr/share/doc/HTML/ca/kmail2/menus.docbook
/usr/share/doc/HTML/ca/kmail2/troubleshooting.docbook
/usr/share/doc/HTML/ca/kmail2/using-kmail.docbook
/usr/share/doc/HTML/ca/ktnef/index.cache.bz2
/usr/share/doc/HTML/ca/ktnef/index.docbook
/usr/share/doc/HTML/de/akonadi_archivemail_agent/index.cache.bz2
/usr/share/doc/HTML/de/akonadi_archivemail_agent/index.docbook
/usr/share/doc/HTML/de/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/de/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/de/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/de/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/de/kmail2/configure.docbook
/usr/share/doc/HTML/de/kmail2/credits-and-licenses.docbook
/usr/share/doc/HTML/de/kmail2/faq.docbook
/usr/share/doc/HTML/de/kmail2/getting-started.docbook
/usr/share/doc/HTML/de/kmail2/index.cache.bz2
/usr/share/doc/HTML/de/kmail2/index.docbook
/usr/share/doc/HTML/de/kmail2/intro.docbook
/usr/share/doc/HTML/de/kmail2/menus.docbook
/usr/share/doc/HTML/de/kmail2/troubleshooting.docbook
/usr/share/doc/HTML/de/kmail2/using-kmail.docbook
/usr/share/doc/HTML/de/ktnef/index.cache.bz2
/usr/share/doc/HTML/de/ktnef/index.docbook
/usr/share/doc/HTML/en/akonadi_archivemail_agent/add-archive-mail.png
/usr/share/doc/HTML/en/akonadi_archivemail_agent/configure-archive-mail-agent.png
/usr/share/doc/HTML/en/akonadi_archivemail_agent/index.cache.bz2
/usr/share/doc/HTML/en/akonadi_archivemail_agent/index.docbook
/usr/share/doc/HTML/en/akonadi_followupreminder_agent/add-followup-reminder.png
/usr/share/doc/HTML/en/akonadi_followupreminder_agent/followupreminder-configure.png
/usr/share/doc/HTML/en/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/en/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/en/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/en/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/en/akonadi_sendlater_agent/sendlateragent-configure.png
/usr/share/doc/HTML/en/akonadi_sendlater_agent/sendlateragent-dialog.png
/usr/share/doc/HTML/en/kmail2/accountwizard.png
/usr/share/doc/HTML/en/kmail2/accountwizard2.png
/usr/share/doc/HTML/en/kmail2/accountwizard3.png
/usr/share/doc/HTML/en/kmail2/accountwizard4.png
/usr/share/doc/HTML/en/kmail2/aggregationtheme.png
/usr/share/doc/HTML/en/kmail2/composer-window.png
/usr/share/doc/HTML/en/kmail2/configure.docbook
/usr/share/doc/HTML/en/kmail2/configure.png
/usr/share/doc/HTML/en/kmail2/configurebutton.png
/usr/share/doc/HTML/en/kmail2/credits-and-licenses.docbook
/usr/share/doc/HTML/en/kmail2/document-decrypt.png
/usr/share/doc/HTML/en/kmail2/document-edit.png
/usr/share/doc/HTML/en/kmail2/document-import.png
/usr/share/doc/HTML/en/kmail2/document-new.png
/usr/share/doc/HTML/en/kmail2/document-open.png
/usr/share/doc/HTML/en/kmail2/faq.docbook
/usr/share/doc/HTML/en/kmail2/filter-dialog.png
/usr/share/doc/HTML/en/kmail2/folder-example.png
/usr/share/doc/HTML/en/kmail2/folder-properties.png
/usr/share/doc/HTML/en/kmail2/folderarchiveagent.png
/usr/share/doc/HTML/en/kmail2/getting-started.docbook
/usr/share/doc/HTML/en/kmail2/go-down.png
/usr/share/doc/HTML/en/kmail2/identitiesadvanced.png
/usr/share/doc/HTML/en/kmail2/identitycryptography.png
/usr/share/doc/HTML/en/kmail2/identitygeneral.png
/usr/share/doc/HTML/en/kmail2/identitypicture.png
/usr/share/doc/HTML/en/kmail2/identitysignature.png
/usr/share/doc/HTML/en/kmail2/identitytemplate.png
/usr/share/doc/HTML/en/kmail2/index.cache.bz2
/usr/share/doc/HTML/en/kmail2/index.docbook
/usr/share/doc/HTML/en/kmail2/intro.docbook
/usr/share/doc/HTML/en/kmail2/kmailwelcome.png
/usr/share/doc/HTML/en/kmail2/layout.png
/usr/share/doc/HTML/en/kmail2/mail-attachment.png
/usr/share/doc/HTML/en/kmail2/mail-mark-important.png
/usr/share/doc/HTML/en/kmail2/mail-mark-read.png
/usr/share/doc/HTML/en/kmail2/mail-mark-task.png
/usr/share/doc/HTML/en/kmail2/mail-mark-unread.png
/usr/share/doc/HTML/en/kmail2/mail-message-new.png
/usr/share/doc/HTML/en/kmail2/mail-queue.png
/usr/share/doc/HTML/en/kmail2/mail-receive.png
/usr/share/doc/HTML/en/kmail2/mail-send.png
/usr/share/doc/HTML/en/kmail2/mail-thread-ignored.png
/usr/share/doc/HTML/en/kmail2/mail-thread-watch.png
/usr/share/doc/HTML/en/kmail2/menus.docbook
/usr/share/doc/HTML/en/kmail2/message.png
/usr/share/doc/HTML/en/kmail2/messagelisttheme.png
/usr/share/doc/HTML/en/kmail2/newidentity.png
/usr/share/doc/HTML/en/kmail2/newidentity2.png
/usr/share/doc/HTML/en/kmail2/preferences-desktop-font.png
/usr/share/doc/HTML/en/kmail2/preview.png
/usr/share/doc/HTML/en/kmail2/receiving.png
/usr/share/doc/HTML/en/kmail2/sending.png
/usr/share/doc/HTML/en/kmail2/sending2.png
/usr/share/doc/HTML/en/kmail2/smile.png
/usr/share/doc/HTML/en/kmail2/troubleshooting.docbook
/usr/share/doc/HTML/en/kmail2/using-kmail.docbook
/usr/share/doc/HTML/en/ktnef/index.cache.bz2
/usr/share/doc/HTML/en/ktnef/index.docbook
/usr/share/doc/HTML/en/ktnef/mainwindow.png
/usr/share/doc/HTML/en/ktnef/winmail_dat.png
/usr/share/doc/HTML/es/akonadi_archivemail_agent/index.cache.bz2
/usr/share/doc/HTML/es/akonadi_archivemail_agent/index.docbook
/usr/share/doc/HTML/es/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/es/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/es/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/es/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/es/kmail2/configure.docbook
/usr/share/doc/HTML/es/kmail2/credits-and-licenses.docbook
/usr/share/doc/HTML/es/kmail2/faq.docbook
/usr/share/doc/HTML/es/kmail2/getting-started.docbook
/usr/share/doc/HTML/es/kmail2/index.cache.bz2
/usr/share/doc/HTML/es/kmail2/index.docbook
/usr/share/doc/HTML/es/kmail2/intro.docbook
/usr/share/doc/HTML/es/kmail2/menus.docbook
/usr/share/doc/HTML/es/kmail2/troubleshooting.docbook
/usr/share/doc/HTML/es/kmail2/using-kmail.docbook
/usr/share/doc/HTML/es/ktnef/index.cache.bz2
/usr/share/doc/HTML/es/ktnef/index.docbook
/usr/share/doc/HTML/et/akonadi_archivemail_agent/index.cache.bz2
/usr/share/doc/HTML/et/akonadi_archivemail_agent/index.docbook
/usr/share/doc/HTML/et/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/et/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/et/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/et/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/et/ktnef/index.cache.bz2
/usr/share/doc/HTML/et/ktnef/index.docbook
/usr/share/doc/HTML/it/akonadi_archivemail_agent/index.cache.bz2
/usr/share/doc/HTML/it/akonadi_archivemail_agent/index.docbook
/usr/share/doc/HTML/it/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/it/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/it/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/it/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/it/ktnef/index.cache.bz2
/usr/share/doc/HTML/it/ktnef/index.docbook
/usr/share/doc/HTML/nl/akonadi_archivemail_agent/index.cache.bz2
/usr/share/doc/HTML/nl/akonadi_archivemail_agent/index.docbook
/usr/share/doc/HTML/nl/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/nl/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/nl/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/nl/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/nl/kmail2/configure.docbook
/usr/share/doc/HTML/nl/kmail2/credits-and-licenses.docbook
/usr/share/doc/HTML/nl/kmail2/faq.docbook
/usr/share/doc/HTML/nl/kmail2/getting-started.docbook
/usr/share/doc/HTML/nl/kmail2/index.cache.bz2
/usr/share/doc/HTML/nl/kmail2/index.docbook
/usr/share/doc/HTML/nl/kmail2/intro.docbook
/usr/share/doc/HTML/nl/kmail2/menus.docbook
/usr/share/doc/HTML/nl/kmail2/troubleshooting.docbook
/usr/share/doc/HTML/nl/kmail2/using-kmail.docbook
/usr/share/doc/HTML/nl/ktnef/index.cache.bz2
/usr/share/doc/HTML/nl/ktnef/index.docbook
/usr/share/doc/HTML/pt/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/pt/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/pt/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/pt/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/pt/ktnef/index.cache.bz2
/usr/share/doc/HTML/pt/ktnef/index.docbook
/usr/share/doc/HTML/pt_BR/akonadi_archivemail_agent/index.cache.bz2
/usr/share/doc/HTML/pt_BR/akonadi_archivemail_agent/index.docbook
/usr/share/doc/HTML/pt_BR/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/pt_BR/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/pt_BR/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/pt_BR/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/pt_BR/kmail2/configure.docbook
/usr/share/doc/HTML/pt_BR/kmail2/credits-and-licenses.docbook
/usr/share/doc/HTML/pt_BR/kmail2/faq.docbook
/usr/share/doc/HTML/pt_BR/kmail2/getting-started.docbook
/usr/share/doc/HTML/pt_BR/kmail2/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kmail2/index.docbook
/usr/share/doc/HTML/pt_BR/kmail2/intro.docbook
/usr/share/doc/HTML/pt_BR/kmail2/menus.docbook
/usr/share/doc/HTML/pt_BR/kmail2/troubleshooting.docbook
/usr/share/doc/HTML/pt_BR/kmail2/using-kmail.docbook
/usr/share/doc/HTML/pt_BR/ktnef/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ktnef/index.docbook
/usr/share/doc/HTML/sv/akonadi_archivemail_agent/index.cache.bz2
/usr/share/doc/HTML/sv/akonadi_archivemail_agent/index.docbook
/usr/share/doc/HTML/sv/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/sv/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/sv/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/sv/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/sv/kmail2/configure.docbook
/usr/share/doc/HTML/sv/kmail2/credits-and-licenses.docbook
/usr/share/doc/HTML/sv/kmail2/faq.docbook
/usr/share/doc/HTML/sv/kmail2/getting-started.docbook
/usr/share/doc/HTML/sv/kmail2/index.cache.bz2
/usr/share/doc/HTML/sv/kmail2/index.docbook
/usr/share/doc/HTML/sv/kmail2/intro.docbook
/usr/share/doc/HTML/sv/kmail2/menus.docbook
/usr/share/doc/HTML/sv/kmail2/troubleshooting.docbook
/usr/share/doc/HTML/sv/kmail2/using-kmail.docbook
/usr/share/doc/HTML/sv/ktnef/index.cache.bz2
/usr/share/doc/HTML/sv/ktnef/index.docbook
/usr/share/doc/HTML/uk/akonadi_archivemail_agent/add-archive-mail.png
/usr/share/doc/HTML/uk/akonadi_archivemail_agent/configure-archive-mail-agent.png
/usr/share/doc/HTML/uk/akonadi_archivemail_agent/index.cache.bz2
/usr/share/doc/HTML/uk/akonadi_archivemail_agent/index.docbook
/usr/share/doc/HTML/uk/akonadi_followupreminder_agent/add-followup-reminder.png
/usr/share/doc/HTML/uk/akonadi_followupreminder_agent/followupreminder-configure.png
/usr/share/doc/HTML/uk/akonadi_followupreminder_agent/index.cache.bz2
/usr/share/doc/HTML/uk/akonadi_followupreminder_agent/index.docbook
/usr/share/doc/HTML/uk/akonadi_sendlater_agent/index.cache.bz2
/usr/share/doc/HTML/uk/akonadi_sendlater_agent/index.docbook
/usr/share/doc/HTML/uk/akonadi_sendlater_agent/sendlateragent-configure.png
/usr/share/doc/HTML/uk/akonadi_sendlater_agent/sendlateragent-dialog.png
/usr/share/doc/HTML/uk/kmail2/configure.docbook
/usr/share/doc/HTML/uk/kmail2/credits-and-licenses.docbook
/usr/share/doc/HTML/uk/kmail2/faq.docbook
/usr/share/doc/HTML/uk/kmail2/getting-started.docbook
/usr/share/doc/HTML/uk/kmail2/index.cache.bz2
/usr/share/doc/HTML/uk/kmail2/index.docbook
/usr/share/doc/HTML/uk/kmail2/intro.docbook
/usr/share/doc/HTML/uk/kmail2/menus.docbook
/usr/share/doc/HTML/uk/kmail2/troubleshooting.docbook
/usr/share/doc/HTML/uk/kmail2/using-kmail.docbook
/usr/share/doc/HTML/uk/ktnef/index.cache.bz2
/usr/share/doc/HTML/uk/ktnef/index.docbook
/usr/share/doc/HTML/uk/ktnef/mainwindow.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkmailprivate.so.5
/usr/lib64/libkmailprivate.so.5.16.1
/usr/lib64/qt5/plugins/akonadi/config/archivemailagentconfig.so
/usr/lib64/qt5/plugins/akonadi/config/followupreminderagentconfig.so
/usr/lib64/qt5/plugins/kcm_kmail.so
/usr/lib64/qt5/plugins/kcm_kmailsummary.so
/usr/lib64/qt5/plugins/kcm_kontactsummary.so
/usr/lib64/qt5/plugins/kmailpart.so
/usr/lib64/qt5/plugins/kontact5/kontact_kmailplugin.so
/usr/lib64/qt5/plugins/kontact5/kontact_summaryplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmail/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kmail/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kmail/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kmail/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kmail/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kmail/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f akonadi_archivemail_agent.lang -f akonadi_followupreminder_agent.lang -f akonadi_mailfilter_agent.lang -f akonadi_sendlater_agent.lang -f kmail.lang -f ktnef.lang -f akonadi_unifiedmailbox_agent.lang -f kmail-refresh-settings.lang
%defattr(-,root,root,-)


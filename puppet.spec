%global nm_dispatcher_dir %{_prefix}/lib/NetworkManager
%global puppet_libdir %{ruby_vendorlibdir}

Name:           puppet
Version:        6.14.0
Release:        1%{?dist}
Summary:        A network tool for managing many disparate systems
License:        ASL 2.0
URL:            http://puppetlabs.com
Source0:        http://downloads.puppetlabs.com/puppet/%{name}-%{version}.tar.gz
Source1:        http://downloads.puppetlabs.com/puppet/%{name}-%{version}.tar.gz.asc
Source2:        https://forge.puppet.com/v3/files/puppetlabs-mount_core-1.0.3.tar.gz
Source3:        https://forge.puppet.com/v3/files/puppetlabs-host_core-1.0.2.tar.gz
Source4:        https://forge.puppet.com/v3/files/puppetlabs-augeas_core-1.0.4.tar.gz
Source5:        https://forge.puppet.com/v3/files/puppetlabs-cron_core-1.0.3.tar.gz
Source6:        https://forge.puppet.com/v3/files/puppetlabs-scheduled_task-2.0.1.tar.gz
Source7:        https://forge.puppet.com/v3/files/puppetlabs-selinux_core-1.0.4.tar.gz
Source8:        https://forge.puppet.com/v3/files/puppetlabs-sshkeys_core-2.0.0.tar.gz
Source9:        https://forge.puppet.com/v3/files/puppetlabs-yumrepo_core-1.0.7.tar.gz
Source10:       https://forge.puppet.com/v3/files/puppetlabs-zfs_core-1.0.5.tar.gz
Source11:       https://forge.puppet.com/v3/files/puppetlabs-zone_core-1.0.3.tar.gz
Source12:       puppet-nm-dispatcher.systemd
Source13:       start-puppet-wrapper

# Puppetlabs messed up with default paths
Patch01: 0001-Fix-puppet-paths.patch

BuildArch: noarch

# ruby-devel does not require the base package, but requires -libs instead
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: systemd
BuildRequires: git
BuildRequires: hiera >= 3.3.1
BuildRequires: facter >= 3.9.6
BuildRequires: facter-devel >= 3.9.6
BuildRequires: ruby-facter >= 3.9.6
BuildRequires: rubygem-semantic_puppet >= 1.0.2
BuildRequires: rubygem-deep_merge
BuildRequires: rubygem-httpclient
BuildRequires: rubygem-multi_json
BuildRequires: ruby-augeas >= 0.5.0
BuildRequires: augeas >= 1.10.1
BuildRequires: augeas-libs >= 1.10.1
BuildRequires: cpp-hocon >= 0.2.1
BuildRequires: cpp-hocon-devel >= 0.2.1
BuildRequires: rubygem-concurrent-ruby >= 1.0.5
Requires: hiera >= 3.3.1
Requires: facter >= 3.9.6
Requires: ruby-facter >= 3.9.6
Requires: rubygem-semantic_puppet >= 1.0.2
Requires: rubygem-puppet-resource_api
Requires: rubygem-deep_merge
Requires: rubygem-httpclient
Requires: rubygem-multi_json
Requires: ruby-augeas >= 0.5.0
Requires: augeas >= 1.10.1
Requires: augeas-libs >= 1.10.1
Requires: cpp-hocon >= 0.2.1
Requires: rubygem-concurrent-ruby >= 1.0.5
Obsoletes: puppet-headless < 6.0.0
Obsoletes: puppet-server < 6.0.0
Obsoletes: puppet < 6.0.0
%{!?_without_selinux:Requires: ruby(selinux), libselinux-utils}

%description
Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts,
along with obviously discrete elements like packages, services, and files.

%prep
%autosetup -S git
%setup -D -b 2 puppetlabs-mount_core-1.0.3
%setup -D -b 3 puppetlabs-host_core-1.0.2
%setup -D -b 4 puppetlabs-augeas_core-1.0.4
%setup -D -b 5 puppetlabs-cron_core-1.0.3
%setup -D -b 6 puppetlabs-scheduled_task-2.0.1
%setup -D -b 7 puppetlabs-selinux_core-1.0.4
%setup -D -b 8 puppetlabs-sshkeys_core-2.0.0
%setup -D -b 9 puppetlabs-yumrepo_core-1.0.7
%setup -D -b 10 puppetlabs-zfs_core-1.0.5
%setup -D -b 11 puppetlabs-zone_core-1.0.3

%patch01 -p1

%build
# Nothing to build

%install
ruby install.rb --destdir=%{buildroot} \
 --bindir=%{_bindir} \
 --logdir=%{_localstatedir}/log/puppetlabs/puppet \
 --rundir=%{_rundir}/puppet \
 --localedir=%{_datadir}/puppetlabs/puppet/locale \
 --vardir=/var/lib/puppet \
 --sitelibdir=%{puppet_libdir}

mkdir -p %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules
mv %{_builddir}/puppetlabs-mount_core-1.0.3 %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules/mount_core
mv %{_builddir}/puppetlabs-host_core-1.0.2 %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules/host_core
mv %{_builddir}/puppetlabs-augeas_core-1.0.4 %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules/augeas_core
mv %{_builddir}/puppetlabs-cron_core-1.0.3 %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules/cron_core
mv %{_builddir}/puppetlabs-scheduled_task-2.0.1 %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules/scheduled_task
mv %{_builddir}/puppetlabs-selinux_core-1.0.4 %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules/selinux_core
mv %{_builddir}/puppetlabs-sshkeys_core-2.0.0 %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules/sshkeys_core
mv %{_builddir}/puppetlabs-yumrepo_core-1.0.7 %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules/yumrepo_core
mv %{_builddir}/puppetlabs-zfs_core-1.0.5 %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules/zfs_core
mv %{_builddir}/puppetlabs-zone_core-1.0.3 %{buildroot}/usr/share/puppetlabs/puppet/vendor_modules/zone_core

install -Dp -m0644 ext/redhat/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/puppet

%{__install} -d -m0755 %{buildroot}%{_unitdir}
install -Dp -m0644 ext/systemd/puppet.service %{buildroot}%{_unitdir}/puppet.service
ln -s %{_unitdir}/puppet.service %{buildroot}%{_unitdir}/puppetagent.service

install -Dpv -m0755 %{SOURCE12} \
 %{buildroot}%{nm_dispatcher_dir}/dispatcher.d/98-%{name}

# Install the ext/ directory to %%{_datadir}/puppetlabs/%%{name}
install -d %{buildroot}%{_datadir}/puppetlabs/%{name}
cp -a ext/ %{buildroot}%{_datadir}/puppetlabs/%{name}
chmod 0755 %{buildroot}%{_datadir}/puppetlabs/%{name}/ext/regexp_nodes/regexp_nodes.rb

# Install wrappers for SELinux
install -Dp -m0755 %{SOURCE13} %{buildroot}%{_bindir}/start-puppet-agent
sed -i 's|^ExecStart=.*/bin/puppet|ExecStart=/usr/bin/start-puppet-agent|' \
 %{buildroot}%{_unitdir}/puppet.service

# Setup tmpfiles.d config
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "D /run/%{name} 0755 %{name} %{name} -" > \
 %{buildroot}%{_tmpfilesdir}/%{name}.conf

# Unbundle
# Note(hguemar): remove unrelated OS/distro specific folders
# These mess-up with RPM automatic dependencies compute by adding
# unnecessary deps like /sbin/runscripts
# some other things were removed with the patch
rm -r %{buildroot}/usr/share/puppetlabs/puppet/ext/{debian,freebsd,gentoo,ips,osx,solaris,suse,windows}
rm %{buildroot}/usr/share/puppetlabs/puppet/ext/redhat/*.init
rm %{buildroot}/usr/share/puppetlabs/puppet/ext/{build_defaults.yaml,project_data.yaml}

%files
%attr(-, puppet, puppet) %{_localstatedir}/log/puppetlabs
%attr(-, puppet, puppet) %{_datadir}/puppetlabs/puppet
%dir %attr(-, puppet, puppet) %{_datadir}/puppetlabs
%{_unitdir}/puppet.service
%{_unitdir}/puppetagent.service
%{_tmpfilesdir}/%{name}.conf
%dir %{nm_dispatcher_dir}
%dir %{nm_dispatcher_dir}/dispatcher.d
%{nm_dispatcher_dir}/dispatcher.d/98-puppet
%{_bindir}/start-puppet-agent

%doc README.md examples
%license LICENSE
%{_datadir}/ruby/vendor_ruby/hiera
%{_datadir}/ruby/vendor_ruby/hiera_puppet.rb
%{_datadir}/ruby/vendor_ruby/puppet
%{_datadir}/ruby/vendor_ruby/puppet_pal.rb
%{_datadir}/ruby/vendor_ruby/puppet.rb
%{_datadir}/ruby/vendor_ruby/puppet_x.rb
%{_sharedstatedir}/puppet
%{_bindir}/puppet
%{_mandir}/man5/puppet.conf.5.gz
%{_mandir}/man8/puppet-plugin.8.gz
%{_mandir}/man8/puppet-report.8.gz
%{_mandir}/man8/puppet-resource.8.gz
%{_mandir}/man8/puppet-script.8.gz
%{_mandir}/man8/puppet-ssl.8.gz
%{_mandir}/man8/puppet-status.8.gz
%{_mandir}/man8/puppet-agent.8.gz
%{_mandir}/man8/puppet.8.gz
%{_mandir}/man8/puppet-apply.8.gz
%{_mandir}/man8/puppet-catalog.8.gz
%{_mandir}/man8/puppet-config.8.gz
%{_mandir}/man8/puppet-describe.8.gz
%{_mandir}/man8/puppet-device.8.gz
%{_mandir}/man8/puppet-doc.8.gz
%{_mandir}/man8/puppet-epp.8.gz
%{_mandir}/man8/puppet-facts.8.gz
%{_mandir}/man8/puppet-filebucket.8.gz
%{_mandir}/man8/puppet-generate.8.gz
%{_mandir}/man8/puppet-help.8.gz
%{_mandir}/man8/puppet-key.8.gz
%{_mandir}/man8/puppet-lookup.8.gz
%{_mandir}/man8/puppet-man.8.gz
%{_mandir}/man8/puppet-module.8.gz
%{_mandir}/man8/puppet-node.8.gz
%{_mandir}/man8/puppet-parser.8.gz

%config(noreplace) %attr(-, puppet, puppet) %dir %{_sysconfdir}/puppetlabs
%config(noreplace) %attr(-, puppet, puppet) %dir %{_sysconfdir}/puppetlabs/puppet
%config(noreplace) %attr(-, puppet, puppet) %dir %{_sysconfdir}/puppetlabs/code
%config(noreplace) %attr(644, puppet, puppet) %{_sysconfdir}/puppetlabs/puppet/auth.conf
%config(noreplace) %attr(644, puppet, puppet) %{_sysconfdir}/puppetlabs/puppet/puppet.conf
%config(noreplace) %attr(644, puppet, puppet) %{_sysconfdir}/puppetlabs/puppet/hiera.yaml
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/logrotate.d/%{name}

%ghost %attr(755, puppet, puppet) %{_rundir}/puppetlabs

%pre
getent group puppet &>/dev/null || groupadd -r puppet -g 52 &>/dev/null
getent passwd puppet &>/dev/null || \
useradd -r -u 52 -g puppet -d /usr/local/puppetlabs -s /sbin/nologin \
 -c "Puppet" puppet &>/dev/null

%post
%systemd_post puppet.service
%systemd_postun_with_restart puppet.service


%changelog
* Mon Jul 13 2020 Breno Brand Fernandes <brandfbb@gmail.com> - 6.14.0-1
- Build of puppet 6.

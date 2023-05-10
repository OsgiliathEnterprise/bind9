"""Role testing files using testinfra."""


def test_hosts_file_contains_the_new_entry(host):
    command = r"""cat /etc/hosts | \
    egrep -c \
    '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\s+poc\.osgiliath\.test'"""
    cmd = host.run(command)
    assert int(cmd.stdout) >= 1


def test_additional_hostname1_added(host):
    command = r"""cat /etc/hosts | \
    egrep -c '^192\.168\.122\.1\s+idm\.osgiliath\.test$'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_additional_hostname2_added(host):
    command = r"""cat /etc/hosts | \
    egrep -c '^192\.168\.122\.2.+infra\.osgiliath\.test'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_hostname_is_updated(host):
    command = r"""hostname | \
    grep -c 'dns.osgiliath.test'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_lookup_resolves_google(host):
    command = r"""nslookup google.fr | \
        grep -Pzoc 'Non-authoritative answer:\nName:\s+google.fr'"""
    cmd = host.run(command)
    assert int(cmd.stdout) >= 1


def test_lookup_resolves_node_as_client(host):
    command = r"""resolvectl query node0.osgiliath.test | \
    grep -c 'link: docker0'"""
    cmd = host.run(command)
    assert int(cmd.stdout) >= 1


# TODO make it work def test_lookup_resolves_reverse(host):
#    command = r"""nslookup 192.169.0.2 | \
#    grep -c 'node0.osgiliath.test.169.192.in-addr.arpa'"""
#    cmd = host.run(command)
#    assert int(cmd.stdout) >= 1

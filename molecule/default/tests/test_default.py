"""Role testing files using testinfra."""


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

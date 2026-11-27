from sentinel.security.policy import check_target_scope, normalize_hostname


def test_exact_allowlist_and_reference_required():
    allowlist = frozenset({"lab.example.test"})
    assert not check_target_scope("lab.example.test", allowlist).authorized
    assert check_target_scope("lab.example.test", allowlist, "ticket-123").authorized


def test_subdomain_is_not_implicitly_authorized():
    decision = check_target_scope("sub.lab.example.test", frozenset({"lab.example.test"}), "ticket-123")
    assert not decision.authorized


def test_reject_url_and_ip_literal():
    try:
        normalize_hostname("https://example.com")
        assert False, "expected ValueError"
    except ValueError:
        pass
    assert not check_target_scope("127.0.0.1", frozenset({"127.0.0.1"}), "ticket").authorized

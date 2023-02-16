from validate_email import validate_email_or_fail
from validate_email.exceptions import EmailValidationError

try:
    is_valid = validate_email_or_fail(
        email_address="example@gmail.com",
        check_format=True,
        check_blacklist=True,
        check_dns=True,
        dns_timeout=5,
        check_smtp=True,
        smtp_timeout=5,
        # smtp_helo_host='my.host.name',
        # smtp_from_address='my@from.addr.ess',
        smtp_skip_tls=False,
        smtp_tls_context=None,
        smtp_debug=False,
    )
    print(is_valid)
except EmailValidationError as e:
    print(e)

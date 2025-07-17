valid_emails = [
    "simple@example.com",
    "john.doe@example.com",
    "jane_doe123@example.co.uk",
    "user-name+alias@example.io",
    "contact_us@example.org",
    "x@example.net",
    "user.name+tag+sorting@example.com",
    "firstname.lastname@sub.domain.com",
    "email123@domain.travel",
    "email@domain.museum",
    "dash-in-name@my-domain.ca",
    "under_score@school.edu",
    "capsLOCK@Example.COM",
    "a.b.c.d.e@multi.parts.domain.biz",
    "email@123domain.com",
    "nobody+temp@fastmail.fm",
    "user+filter@protonmail.ch",
    "shop.orders@ecommerce.site",
    "info@company-name.com",
    "hello.world123@new-tech.dev",
    "alice@example.com",
    "bob.smith@example.org",
    "charlie_doe@example.net",
    "d.e.f.g@example.co.uk",
    "eve+security@example.com",
    "fiona@dev.mail",
    "g_harris@domain.io",
    "harold123@company.biz",
    "ian.o'reilly@example.info",
    "jack-the-hack@cyber.zone",
    "karen_2025@outlook.com",
    "leo+archive@gmail.com",
    "m_mclean@university.edu",
    "noah.t@sub.example.org",
    "olivia.west@startup.xyz",
    "paul@service-now.com",
    "quentin_44@backup.email",
    "rick.sanchez@galactic.net",
    "sue1989@data-center.ai",
    "tina@personal-domain.ca",
    "umar+test@fastmail.fm",
    "vicky_underscore@some-domain.tech",
    "winston@newsletter.site",
    "xander_zulu@enterprise.global",
    "yara.khan@distribution.group",
    "zed@my.email",
    "alpha.beta@projects.dev",
    "sales-team@shop.ca",
    "contact@portal.inc",
    "admin@cloud-hosting.app",
]


invalid_emails = [
    "plainaddress",                      # missing @
    "@no-local-part.com",               # missing local part
    "username@",                        # missing domain
    "username@.com",                    # domain starts with dot
    "username@com",                     # no dot in domain
    "user..name@example.com",           # double dot in local part
    ".username@example.com",            # local part starts with dot
    "username.@example.com",            # local part ends with dot
    "user@domain..com",                 # double dot in domain
    "user@-domain.com",                 # domain starts with dash
    "user@domain-.com",                 # domain ends with dash
    "user@domain.com-",                 # TLD ends with dash
    "user@.domain.com",                 # domain segment starts with dot
    "user@domain.com.",                 # domain ends with dot
    "user@domain.c",                    # TLD too short
    "user@domain.toolongtld",           # TLD too long or unlikely
    "user@do_main.com",                 # underscore in domain (not allowed)
    "user@domain..sub.com",             # double dot in subdomain
    "us er@example.com",                # space in local part
    "user@exa mple.com",                # space in domain
    "user@exam\nple.com",              # newline character
    "user@localhost",                   # localhost domain (not public-valid)
    "user@[192.168.0.1]",               # IP domain — rarely accepted
    "user@.123",                        # numeric-only TLD with dot
    "user@domain..com.",                # trailing dot and double dots
    "user@.invalid",                    # domain starts with dot
    "user@invalid.",                    # domain ends with dot
    "user@inv..alid.com",              # double dot mid-domain
    "user@inv@lid.com",                # multiple @ signs
    "user@invalid..",                  # trailing double dot
    "user@.invalid.com",               # domain segment starts with dot
    "user@invalid..com",               # domain segment has double dot
    "user@@example.com",               # double @
    "user@ example.com",               # space after @
    " user@example.com",               # leading space
    "user@example.com ",               # trailing space
    "user\t@example.com",              # tab character
    "user\n@example.com",              # newline character
    "user@#$.com",                     # garbage in domain
    "user@!domain.com",                # invalid character in domain
    "user@domain..com.com",            # triple-level double-dot
    "user..dot@example.com",           # double dot in local
    "\"user\"@example.com",            # quoted local part (RFC-valid, but reject in real-world)
    "user@domain.toolongtldddd",       # ridiculous TLD
    "user@sub_domain.com",             # underscore in domain
    "user@domain.com.",                # trailing period
    "user@.com.com",                   # leading dot segment
    "user@domain..",                   # incomplete double dot at end
    ".user@example.com",              # starts with dot
    "user.@example.com",              # ends with dot
]

Changelog
=========

2.0.0
-----
#. Stabilize on Jmbo 2.0.0.

2.0.0a1
-------
#. Add tests.
#. Django 1.6 compatibility.
#. Up minimum jmbo to 2.0.0.

0.1.3
-----
#. Add Poll Option ordering to use PK as the default

0.1.2
-----
#. Performance improvements.

0.1.1
-----
#. Add caching to detail and widget templates.

0.1
---
#. Add 'See results' link. This can possibly break current styling.

0.0.9
-----
#. Correctly limit poll vote counts to PollOption ContentType.

0.0.5
-----
#. Require minimum jmbo 0.1.20
#. Admin inline option reports.

0.0.4
-----
#. Polls do not abuse the base model liking settings anymore.
#. Vote detail page and widget now prompts user for login if required.
#. South migrations. If you have an existing database then run ./bin/django migrate poll 0001 --fake.

0.0.3
-----
#. Signal dispatched when poll option selected.

0.0.2
-----
#. Fix detail view can_vote check.

0.0.1
-----
#. Initial release.


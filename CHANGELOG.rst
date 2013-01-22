Changelog
=========

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


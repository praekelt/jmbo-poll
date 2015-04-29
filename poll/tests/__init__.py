from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from poll.models import Poll, PollOption


class TestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = Client()

        # Editor
        cls.editor, dc = User.objects.get_or_create(
            username='editor',
            email='editor@test.com'
        )
        cls.editor.set_password("password")
        cls.editor.save()

    def test_add_vote(self):
        # poll
        poll, dc = Poll.objects.get_or_create(
            title='Poll',
            owner=self.editor, state='published',
            comments_enabled=False,
        )
        poll.sites = [1]
        poll.save()

        option_one = PollOption(
            title='Option One',
            poll=poll
        )
        option_two = PollOption(
            title='Option Two',
            poll=poll
        )
        option_one.save()
        option_two.save()

        response = self.client.post(
            reverse('poll-detail-vote', kwargs={'poll_id': poll.id}),
            {'poll_option': 1},
            REMOTE_ADDR='127.0.0.1',
            HTTP_USER_AGENT='testclient'
        )
        self.assertEqual(response.status_code, 200)
        self.failUnless(
            "poll-detail-results" in response.content
        )

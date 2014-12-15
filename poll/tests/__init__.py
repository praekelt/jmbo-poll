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

        # poll
        obj, dc = Poll.objects.get_or_create(
            title='Poll',
            owner=cls.editor, state='published',
            comments_enabled=False,
        )
        obj.sites = [1]
        obj.save()
        cls.poll = obj

        option_one = PollOption(
            title='Option One',
            poll=cls.poll
        )
        option_two = PollOption(
            title='Option Two',
            poll=cls.poll
        )
        option_one.save()
        option_two.save()

    def test_add_vote(self):
        self.client.login(username='editor', password='password')
        response = self.client.post(
            reverse('poll-detail-vote', kwargs={'poll_id': self.poll.id}),
            {'poll_option': 1}
        )
        self.assertEqual(response.status_code, 200)
        # import ipdb; ipdb.set_trace()
        self.failUnless(
            "Your vote has been saved" in response.content
        )

import datetime as dt
from django.test import TestCase
from django.utils import timezone
from xp_tracker_app.models import Story, Task

class StoryTestCase(TestCase):
    def setUp(self):
        Story.objects.create(story_name="User story",
                             time_est=(timezone.now() + dt.timedelta(weeks=1)).date())

    def test_story_creates(self):
        story = Story.objects.get(story_name="User story")
        self.assertEqual(story.story_name, "User story")
        self.assertEqual(story.time_est, (timezone.now() + dt.timedelta(weeks=1)).date())
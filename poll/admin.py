from django.contrib import admin

from jmbo.admin import ModelBaseAdmin

from poll.models import Poll, PollOption


class PollOptionInline(admin.StackedInline):
    model = PollOption


class PollAdmin(ModelBaseAdmin):
    inlines = [PollOptionInline]


admin.site.register(Poll, PollAdmin)

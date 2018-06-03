from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from pinax.pages.models import Page


from account.decorators import login_required


@login_required
def dashboard(request):
    if request.session.get("pending-token"):
        return redirect("speaker_create_token", request.session["pending-token"])
    return render(request, "dashboard.html")


class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages_en = Page.published.filter(title='messages')
        if messages_en:
            context['conf_messages'] = messages_en[0].body_html
        messages_he = Page.published.filter(title='messages_hebrew')
        if messages_he:
            context['conf_messages_hebrew'] = messages_he[0].body_html
        return context

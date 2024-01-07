from django.views.generic import TemplateView
from django.contrib.staticfiles.finders import find
from utils import get_json_data

import json

class ExpensesListTemplateView(TemplateView):
    extra_context = {'page_title': 'Expense Report'}
    template_name = 'expenses/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expense_report'] = get_json_data('expenses.json')
        return context

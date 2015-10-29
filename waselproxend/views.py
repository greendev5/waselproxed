from django.views.generic import TemplateView


class ProxEndView(TemplateView):

    template_name = 'proxend/proxend.html'

    def get_context_data(self, **kwargs):
        context = super(ProxEndView, self).get_context_data(**kwargs)
        context['HOST_NAME'] = self.request.get_host()
        return context

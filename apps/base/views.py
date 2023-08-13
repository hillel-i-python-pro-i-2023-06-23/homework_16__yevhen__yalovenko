from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "base/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            greeting_text="Welcome! This is Yevhen Yalovenko homework-16 project. Today we learn " "how to admin.",
            #
            title="Home Page",
        )

        return context


class AboutUsView(TemplateView):
    template_name = "base/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            about="Contact info: jenyaya0007@gamil.com",
            #
            title="About us",
        )

        return context

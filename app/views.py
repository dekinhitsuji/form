from django.shortcuts import render
from . import forms
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from . forms import Contact_Form
from django.urls import reverse_lazy

class TopFormView(FormView):
    template_name = 'app/formpage.html'
    form_class = Contact_Form
    success_url = reverse_lazy('app:doui')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




    

def topic_create(request):
    template_name = 'app/formpage.html'
    ctx = {}
    if request.method == 'GET':
        ctx['form'] = TopFormView()
        return render(request, template_name, ctx)

    if request.method == 'POST':
        topic_form = TopFormView(request.POST)
        if topic_form.is_valid():
            topic_form.save()
            return redirect(reverse_lazy('app:doui'))
        else:
            ctx['form'] = topic_form
            return render(request, template_name, ctx)


# class FormView(TemplateView):
#
#     # #初期変数定義
#     # def __init__(self):
#     #     self.params = {"Message":"情報を入力してください。",
#     #                    "form":forms.Contact_Form(),
#     #                    }
#
#     #GET時の処理を記載
#     def get(self,request):
#         return render(request, "app/formpage.html",context=self.params)
#
#     #POST時の処理を記載
#     def post(self,request):
#         if request.method == "POST":
#             self.params["form"] = forms.Contact_Form(request.POST)
#
#             #フォーム入力が有効な場合
#             if self.params["form"].is_valid():
#                 #入力項目をデータベースに保存
#                 self.params["form"].save(commit=True)
#                 self.params["Message"] = "入力情報が送信されました。"
#
#
#         return render(request, "app/formpage.html",context=self.params)
#
#
class Index(TemplateView):
    template_name = "app/doui.html"

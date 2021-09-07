from django.shortcuts import render
from . import forms
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse


class FormView(TemplateView):

    #初期変数定義
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                       "form":forms.Contact_Form(),
                       }

    #GET時の処理を記載
    def get(self,request):
        return render(request, "app/formpage.html",context=self.params)

    #POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.Contact_Form(request.POST)

            #フォーム入力が有効な場合
            if self.params["form"].is_valid():
                #入力項目をデータベースに保存
                self.params["form"].save(commit=True)
                self.params["Message"] = "入力情報が送信されました。"


        return render(request, "app/formpage.html",context=self.params)
        HttpResponseRedirect('formpage/doui/')


class Index(TemplateView):
    template_name = "app/doui.html"

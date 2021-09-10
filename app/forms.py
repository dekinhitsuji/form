from django import forms
#モデルクラスを呼出
from .models import People
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.admin import widgets
import os


widget_textinput = forms.TextInput(
    attrs={
        "class":"form-control",
    }
)

#フォームクラス作成
class Contact_Form(forms.ModelForm):

    class Meta():
        #①モデルクラスを指定
        model = People

        #②表示するモデルクラスのフィールドを定義
        fields = ('Name','Furigana','Tell','Mail','Birthday','Adress')


        #③表示ラベルを定義
        labels = {
            'Name':"名前　　",
            'Furigana':"フリガナ",
            'Tell':"電話番号",
            'Mail':"メール　",
            'Birthday':"生年月日",
            'Adress':"住所　　",
        }
        widget = {
            'Name': widget_textinput,
            'Furigana': widget_textinput,
            'Tell': widget_textinput,
            'Mail': widget_textinput,
            'Birthday': widget_textinput,
            'Adress': widget_textinput,
        }



class CheckeForm(forms.Form):
    selected_time = forms.fields.ChoiceField(
        choices = (
            ('','同意します'),
        ),
        label = '上記の内容に同意できる場合下記ボックスにチェックを入れてください',
        required = True,
        widget = forms.widgets.RadioSelect

    )

# -*- coding: utf-8 -*-

import string

abbrevs = [u'акад\.',
u'б\.',
u'вл\.',
u'абл\.',
u'абс\.',
u'абх\.',
u'авар\.',
u'авг\.',
u'австр\.',
u'австрал\.',
u'авт\.',
u'агр\.',
u'адж\.',
u'адм\.',
u'адыг\.',
u'азерб\.',
u'акад\.',
u'акк\.',
u'акц\.',
u'алб\.',
u'алг\.',
u'алж\.',
u'алт\.',
u'алф\.',
u'альм\.',
u'альп\.',
u'амер\.',
u'анат\.',
u'англ\.',
u'ангол\.',
u'аннот\.',
u'антич\.',
u'ап\.',
u'апр\.',
u'арам\.',
u'аргент\.',
u'арифм\.',
u'арт\.',
u'архип\.',
u'архим\.',
u'асср',
u'асс\.',
u'ассир\.',
u'астр\.',
u'ат\.',
u'атм\.',
u'афг\.',
u'афр\.',
u'балк\.',
u'балт\.',
u'башк\.',
u'безв\.',
u'безл\.',
u'бельг\.',
u'библ\.',
u'биогр\.',
u'биол\.',
u'бирм\.',
u'бол\.',
u'болг\.',
u'буд\.',
u'бюдж\.',
u'бюлл\.',
u'вал\.',
u'вв\.',
u'вдхр\.',
u'вед\.',
u'вел\.',
u'венг\.',
u'вкл\.',
u'внеш\.',
u'внутр\.',
u'вод\. ст\.',
u'воен\.',
u'возв\.',
u'возд\.',
u'воскр\.',
u'вост\.',
u'вт\.',
u'вьетн\.',
u'г\.',
u'гг\.',
u'га\.',
u'гав\.',
u'газ\.',
u'гвин\.',
u'гВт\.',
u'ГГц\.',
u'ген\.',
u'ген\. л\.',
u'ген\. м\.',
u'ген\. п\.',
u'геогр\.',
u'геод\.',
u'геол\.',
u'геом\.',
u'герм\.',
u'г­жа\.',
u'гл\.',
u'гор\.',
u'гос\.',
u'госп\.',
u'град\.',
u'греч\.',
u'гр\.',
u'гражд\.',
u'греч\.',
u'груз\.',
u'губ\.',
u'Гц\.',
u'ГэВ\.',
u'дптр\.',
u'д\. б\. н\.',
u'Д\. В\.',
u'д\. г\. н\.',
u'д\. г\.­м\. н\.',
u'дер\.',
u'д\. и\. н\.',
u'д\. иск\.',
u'д\. м\. н\.',
u'д\. н\.',
u'д\. о\.',
u'д\. п\.',
u'д\. т\. н\.',
u'д\. ф\. н\.',
u'д\. ф\.­м\. н\.',
u'д\. х\. н\.',
u'д\. ч\.',
u'дБ\.',
u'деепр\.',
u'действ\.',
u'дек\.',
u'дер\.',
u'Дж\.',
u'диак\.',
u'диал\.',
u'диал\.',
u'диам\.',
u'див\.',
u'диз\.',
u'дир\.',
u'дисс\.',
u'дист\.',
u'дифф\.',
u'дкг\.',
u'дкл\.',
u'дкм\.',
u'дм\.',
u'доб\.',
u'док\.',
u'докт\.',
u'долл\.',
u'доп\.',
u'доц\.',
u'драм\.',
u'дубл\.',
u'евр\.',
u'европ\.',
u'егип\.',
u'ед\.',
u'ед\. ч\.',
u'ежедн\.',
u'ежемес\.',
u'еженед\.',
u'ефр\.',
u'ж\.',
u'ж\. д\.',
u'жен\.',
u'жит\.',
u'женск\.',
u'журн\.',
u'засл\. арт\.',
u'з\. д\.',
u'зав\.',
u'зав\. хоз\.',
u'загл\.',
u'зал\.',
u'зам\.',
u'заруб\.',
u'зем\.',
u'зол\.',
u'др\.',
u'пр\.',
u'и\. о\.',
u'и\.о\.',
u'игум\.',
u'иером\.',
u'им\.',
u'иностр\.',
u'инд\.',
u'индонез\.',
u'итал\.',
u'канд\.',
u'коп\.',
u'корп\.',
u'кв\.',
u'ква\.',
u'квт\.',
u'кг\.',
u'кгс\.',
u'кгц\.',
u'кд\.',
u'кдж\.',
u'кирг\.',
u'ккал\.',
u'кл\.',
u'км\.',
u'кмоль\.',
u'книжн\.',
u'кэв\.',
u'л\.с\.',
u'лаб\.',
u'лат\.',
u'латв\.',
u'лейт\.',
u'лит\.',
u'м\.',
u'мин\.',
u'м­р\.',
u'муж\.',
u'м\.н\.с\.',
u'макс\.',
u'матем\.',
u'мат\.',
u'маш\.',
u'м­во\.',
u'мгц\.',
u'мдж\.',
u'мед\.',
u'мес\.',
u'мин­во\.',
u'митр\.',
u'мка\.',
u'мкал\.',
u'мкв\.',
u'мквт\.',
u'мкм\.',
u'мкмк\.',
u'мком\.',
u'мкпа\.',
u'мкр\.',
u'мкф\.',
u'мкюри\.',
u'мл\.',
u'млк\.',
u'млн\.',
u'млрд\.',
u'мн\.ч\.',
u'моск\.',
u'мпа\.',
u'мс\.',
u'мужск\.',
u'мэв\.',
u'н\.э\.',
u'нем\.',
u'обл\.',
u'пос\.',
u'пер\.',
u'пр\.',
u'пл\.',
u'р\.',
u'рис\.',
u'стр\.',
u'сокр\.',
u'ст\.н\.с\.',
u'ст\.',
u'т\.',
u'т\.д\.',
u'т\.е\.',
u'т\.к\.',
u'т\.н\.',
u'т\.о\.',
u'т\.п\.',
u'т\.с\.',
u'тыс\.',
u'тел\.',
u'тов\.',
u'трлн\.',
u'ул\.',
u'франц\.',
u'ч\.',
u'чел\.']

rules = [u'[-\w.]+@(?:[A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}', #e-mail
         u'(?:[01]?[0-9]|2[0-4]):[0-5][0-9]', # times
         u'(?:mailto:|(?:news|http|https|ftp|ftps)://)[\w\.\-]+|^(?:www(?:\.[\w\-]+)+)', # urls
         u'[\w\.\-]+\.(?:com|org|net)', # url2
         u'--',
         u'\.\.\.',
         u'\d+\.\d+',
         u'[' + string.punctuation + u']',
         u'[а-яА-ЯёЁa-zA-Z0-9]+',
         u'\S']

final_regex = u'|'.join(abbrevs + rules)

def create_tokenizer_ru():
    from nltk.tokenize import RegexpTokenizer
    
    return RegexpTokenizer(final_regex)

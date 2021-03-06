from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from .forms import FeedingForm, AddFourniForm, ArticleForm, TakingForm
from django.core.paginator import Paginator




# Database Modeles needed *********************
from .models import (Article, Fournisseur, 
Taking, 
TakingArticles,
Feeding)



@login_required 
def home(request):
    return render(request, 'home.html')


# Article module ------------------------------------------------------------------------
@login_required
def addarticle(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article.objects.create(nom=form.cleaned_data["nom"], 
                                                group=form.cleaned_data["group"],
                                                fourni=form.cleaned_data["fourni"],
                                                prix=form.cleaned_data["prix"],
                                                qte=form.cleaned_data["qte"],
                                                )
            print("fed success")
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = ArticleForm()
    context = {
        "form" : form
    }
    return render(request, "add_article.html", context)



@login_required
def articleslist(request):
    articles = Article.objects.all()

    #calculate stock value
    single_values = []
    
    for article in articles :
        price = article.prix
        quantity = article.qte
        single_value = price * quantity
        article.single_value = single_value
        article.save()
        single_values.append(single_value)

    total_value = sum(single_values)


    context = {"articles": articles,
                "total_value": total_value,
            }
    return render(request, "article_list.html", context)


# Take Article module ------------------------------------------------------------------------
@login_required
def takearticle(request):
    taking = None
    if request.method == "POST":
        form = TakingForm(request.POST)
        if form.is_valid():
            taking = Taking.objects.create(poste=form.cleaned_data["poste"])
            print("fed success")
            take_id = taking.id
            return redirect('takearticledetails', id=take_id)
        else:
            print(form.errors)
    else:
        form = TakingForm()
   
    context = {
        "taking": taking,
        "form" : form
    }
    return render(request, 'takearticle.html', context)

@login_required
def notAuto(request):
    return render(request, "not_autho.html")
@login_required
def takearticledetails(request, id):
    taking = Taking.objects.get(id=id)
    ArticleFormset = inlineformset_factory(Taking, TakingArticles, fields=('articles', 'qte',), can_delete=False, extra=1)
    formset = ArticleFormset(request.POST, instance=taking)
    total_value_of_taking = []
    price_of_all_takings = None
    if formset.is_valid():
        for f in formset:
            article = f.cleaned_data['articles']
            quantite = f.cleaned_data['qte']
            selected_article = Article.objects.get(nom=article)
            if selected_article.qte < quantite :
                taking.delete()
                return redirect ("not_autho")
            else:
                selected_article.qte = selected_article.qte - quantite
                selected_article.save() 
                selected_article_price = selected_article.prix
                value_of_take_per_article = selected_article_price * quantite
                total_value_of_taking.append(value_of_take_per_article)
        formset.save()
        total_value = sum(total_value_of_taking)
        taking.total_value = total_value
        taking.save()
        return redirect('takearticledetails', id=id)
    formset = ArticleFormset(instance=taking)
    return render(request, 'takearticledetails.html', {'formset': formset})

@login_required
def takelist(request):
    takelist = Taking.objects.all()
    # page = request.GET.get('page', 1)
    # paginator = Paginator(take, 7)
    # takelist = paginator.page(page) 
    price_of_all_takings = Taking.objects.aggregate(Sum('total_value'))
    return render(request, "takelist.html", {"takelist": takelist, 'pr': price_of_all_takings})

@login_required
def takedetails(request, id):
    take = Taking.objects.get(id=id)
    takedetails = TakingArticles.objects.filter(taking=take)
    return render(request, "takedetails.html", {"taked": takedetails})



# Article module ------------------------------------------------------------------------

@login_required
def feedarticle(request):
    if request.method == "POST":
        form = FeedingForm(request.POST)
        if form.is_valid():
            feeding = Feeding.objects.create(user=request.user, 
                                                article=form.cleaned_data["article"],
                                                qt??=form.cleaned_data["qt??"],
                                                prix=form.cleaned_data["prix"]
                                                )
            arti = Article.objects.get(nom=form.cleaned_data["article"])
            arti.prix = form.cleaned_data["prix"]
            previous_quantity = arti.qte
            new_quantity = previous_quantity + form.cleaned_data["qt??"]
            arti.qte = new_quantity
            arti.single_value = new_quantity * form.cleaned_data["prix"]
            arti.save()
            print("fed success")
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = FeedingForm()
    context = {
        "form" : form
    }
    return render(request, "fedform.html", context)

@login_required
def addfourni(request):
    if request.method == "POST":
        form = AddFourniForm(request.POST)
        if form.is_valid():
            fourni = Fournisseur.objects.create(nom = form.cleaned_data["nom"], 
                                                adresse = form.cleaned_data["adresse"],
                                                tel = form.cleaned_data["tel"])
            return redirect("home")
    else:
        form = AddFourniForm()
    context = {
        "form": form
    }
    return render(request, "ajout_fourni.html", context) 

@login_required
def fournilist(request):
    fournil = Fournisseur.objects.all()
    context = {
        "fournil": fournil
    }
    return render(request, "fourni_list.html", context)

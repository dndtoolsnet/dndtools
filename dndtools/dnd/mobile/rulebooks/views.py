from django.shortcuts import render, get_object_or_404
from dnd.menu import menu_item, submenu_item
from dnd.filters import RulebookFilter
from dnd.mobile.dnd_paginator import DndMobilePaginator
from dnd.mobile.views import permanent_redirect_object_mobile
from dnd.models import Rulebook, DndEdition
from dnd.views import is_3e_edition


@menu_item("rulebooks")
@submenu_item("rulebooks")
def rulebook_list_mobile(request):
    f = RulebookFilter(request.GET, queryset=Rulebook.objects.select_related(
        'dnd_edition'))

    form_submitted = 1 if '_filter' in request.GET else 0

    paginator = DndMobilePaginator(f.qs, request)

    return render(request, 'dnd/mobile/rulebooks/rulebook_list.html', context={
      'rulebook_list': paginator.items(), 'paginator': paginator, 'filter': f,
      'form_submitted': form_submitted,},)


@menu_item("rulebooks")
@submenu_item("editions")
def edition_list_mobile(request):
    edition_list = DndEdition.objects.all()

    paginator = DndMobilePaginator(edition_list, request)

    return render(request, 'dnd/mobile/rulebooks/edition_list.html', context={
      'edition_list': paginator.items(), 'paginator': paginator,},)


@menu_item("rulebooks")
@submenu_item("editions")
def edition_detail_mobile(request, edition_slug, edition_id):
    dnd_edition = get_object_or_404(DndEdition, id=edition_id)
    if dnd_edition.slug != edition_slug:
        return permanent_redirect_object_mobile(request, dnd_edition)

    rulebook_list = dnd_edition.rulebook_set.select_related('dnd_edition').all()

    paginator = DndMobilePaginator(rulebook_list, request)

    return render(request, 'dnd/mobile/rulebooks/edition_detail.html', context=
      {'dnd_edition': dnd_edition, 'rulebook_list': paginator.items(), 'paginator': paginator,
       'i_like_it_url': request.build_absolute_uri(), 'inaccurate_url': request.build_absolute_uri(),
       'display_3e_warning': is_3e_edition(dnd_edition),},)


@menu_item("rulebooks")
@submenu_item("rulebooks")
def rulebook_detail_mobile(request, edition_slug, edition_id, rulebook_slug,
                           rulebook_id):
    rulebook = get_object_or_404(Rulebook, id=rulebook_id)
    if (rulebook.slug != rulebook_slug or
                str(rulebook.dnd_edition.id) != edition_id or
                rulebook.dnd_edition.slug != edition_slug):
        return permanent_redirect_object_mobile(request, rulebook)

    return render(request, 'dnd/mobile/rulebooks/rulebook_detail.html', context={'rulebook': rulebook,
      'dnd_edition': rulebook.dnd_edition, 'i_like_it_url': request.build_absolute_uri(),
      'inaccurate_url': request.build_absolute_uri(), 'display_3e_warning': is_3e_edition(rulebook.dnd_edition),},)
    
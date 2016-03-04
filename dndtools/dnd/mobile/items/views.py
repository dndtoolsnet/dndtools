from math import ceil

from django.shortcuts import get_object_or_404, render
from dnd.menu import menu_item, submenu_item
from dnd.mobile.views import permanent_redirect_object_mobile
from dnd.utilities import int_with_commas
from dnd.mobile.dnd_paginator import DndMobilePaginator
from dnd.filters import ItemFilter
from dnd.models import Rulebook, Item
from dnd.views import is_3e_edition, permanent_redirect_view


@menu_item("items")
@submenu_item("items")
def item_index_mobile(request):
    f = ItemFilter(request.GET, queryset=Item.objects.select_related(
        'rulebook', 'rulebook__dnd_edition', 'body_slot', 'property').distinct())

    paginator = DndMobilePaginator(f.qs, request)

    form_submitted = 1 if '_filter' in request.GET else 0

    return render(request, 'dnd/mobile/items/item_index.html', context={'item_list': paginator.items(),
      'paginator': paginator, 'filter': f, 'form_submitted': form_submitted,},)


@menu_item("items")
@submenu_item("by_rulebooks")
def item_list_by_rulebook_mobile(request):
    rulebook_list = Rulebook.objects.select_related('dnd_edition').all()

    paginator = DndMobilePaginator(rulebook_list, request)

    return render(request, 'dnd/mobile/items/item_list_by_rulebook.html', context=
      {'rulebook_list': paginator.items(), 'paginator': paginator,},)


@menu_item("items")
@submenu_item("by_rulebooks")
def items_in_rulebook_mobile(request, rulebook_slug, rulebook_id):
    rulebook = get_object_or_404(Rulebook, pk=rulebook_id)
    if not rulebook.slug == rulebook_slug:
        return permanent_redirect_view(request, 'dnd:mobile:items:items_in_rulebook_mobile',
                                       kwargs={
                                           'rulebook_slug': rulebook.slug,
                                           'rulebook_id': rulebook_id, })

    item_list = rulebook.item_set.select_related(
        'rulebook', 'rulebook__dnd_edition').all()

    paginator = DndMobilePaginator(item_list, request)

    return render(request, 'dnd/mobile/items/items_in_rulebook.html', context=
      {'rulebook': rulebook, 'item_list': paginator.items(), 'paginator': paginator,
       'display_3e_warning': is_3e_edition(rulebook.dnd_edition),},)


@menu_item("items")
@submenu_item("items")
def item_detail_mobile(request, rulebook_slug, rulebook_id, item_slug, item_id):
    item = get_object_or_404(Item.objects.select_related(
        'rulebook', 'rulebook__dnd_edition', 'body_slot', 'aura',
        'activation', 'property', 'synergy_prerequisite',
    ).prefetch_related('aura_schools', 'required_feats', 'required_spells'),
    pk=item_id)
    assert isinstance(item, Item)

    if (item.slug != item_slug or
                str(item.rulebook.id) != rulebook_id or
                item.rulebook.slug != rulebook_slug):
        return permanent_redirect_object_mobile(request, item)

    required_feats = item.required_feats.select_related('rulebook').all()
    required_spells = item.required_spells.select_related('rulebook').all()

    cost_to_create = item.cost_to_create
    # calculate CTC
    if not cost_to_create:
        if item.price_gp and not item.price_bonus:
            cost_to_create = "%s gp, %s XP, %d day(s)" % (
                int_with_commas(ceil(item.price_gp / 2.0)), int_with_commas(ceil(item.price_gp / 25.0)),
                ceil(item.price_gp / 1000.0))
        elif not item.price_gp and item.price_bonus:
            cost_to_create = "Varies"

    return render(request, 'dnd/mobile/items/item_detail.html', context={'item': item,
      'aura_schools': item.aura_schools.all(), 'required_feats': required_feats,
      'required_spells': required_spells, 'cost_to_create': cost_to_create, 'rulebook': item.rulebook,
      'ItemType': Item.ItemType, 'i_like_it_url': request.build_absolute_uri(),
      'inaccurate_url': request.build_absolute_uri(), 'display_3e_warning': is_3e_edition(item.rulebook.dnd_edition),},)
    
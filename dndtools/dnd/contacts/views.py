from django.core.mail.message import EmailMessage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from dnd.menu import menu_item, submenu_item, MenuItem
from dnd.forms import ContactForm
from dnd.models import StaticPage


@menu_item(MenuItem.CONTACTS)
@submenu_item(MenuItem.Contacts.CONTACT_US)
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,
                           initial={
                               'captcha': request.META['REMOTE_ADDR']})
        if form.is_valid():
            if form.cleaned_data['sender']:
                headers = {
                    'Reply-To': form.cleaned_data['sender']}
            else:
                headers = {}

            email = EmailMessage(
                subject=form.cleaned_data['subject'],
                body="%s\n\nfrom: %s" % (form.cleaned_data['message'],
                                         form.cleaned_data['sender']),
                from_email='mailer@dndtools.eu',
                to=('dndtoolseu@googlegroups.com', 'dndtools.eu@gmail.com'),
                headers=headers,
            )

            email.send()

            # Redirect after POST
            return HttpResponseRedirect(reverse('contact_sent'))

    else:
        form = ContactForm()  # An unbound form

    # request context required for CSRF
    return render(request, 'dnd/contacts/contact.html', context={'form': form,},)


@menu_item(MenuItem.CONTACTS)
@submenu_item(MenuItem.Contacts.CONTACT_US)
def contact_sent(request):
    return render(request, 'dnd/contacts/contact_sent.html',)


@menu_item(MenuItem.CONTACTS)
@submenu_item(MenuItem.Contacts.STAFF)
def staff(request):
    page_body = StaticPage.objects.filter(name='staff')[0]

    return render(request, 'dnd/contacts/staff.html', {'page_body': page_body,},)

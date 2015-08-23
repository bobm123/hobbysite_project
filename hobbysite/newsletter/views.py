from django.shortcuts import render

from newsletter.models import Newsletter


def browse_by_year(request, year='2015'):
    newsletters = Newsletter.objects.filter(
                name__contains=year).order_by('name')
        
    return render(request, 'newsletter.html', {
        'newsletters': newsletters,
        'year' : year,
        'filter_keys' : ['2010', '2011', '2012', '2013', '2014', '2015'],
    })

    

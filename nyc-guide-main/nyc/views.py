from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    '''Corresponds to the urls.py'''
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    '''Selection of one of the five given boroughs'''
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )


class ActivityView(View):
    '''The particular activity in a borough'''
    def get(self, request, borough, activity):
        return render(
             request = request, 
             template_name = 'activities.html',
             context={'activity' : activity , 'borough' : borough, 'venues': boroughs[borough][activity].keys()}
        )
        # selection via the dict got tricky for me, above is how to navigate in getting the activites
       

class VenueView(View):
    '''The specific venue, site or locale and it's given description'''
    def get(self, request, borough, activity, venue):
        return render(
            request=request,
            template_name='venue.html',
            context={'borough' : borough, 'activity' : activity, 'venue' : venue, 'description':boroughs[borough][activity][venue].get('description')}
        )
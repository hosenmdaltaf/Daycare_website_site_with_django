from django.shortcuts import render

def homepage(request):
    return render(request,'homeapp/homepage.html')

    
# from django.shortcuts import render

# def band_listing(request):
#     """A view of all bands."""
#     bands = models.Band.objects.all()
#     return render(request, 'bands/band_listing.html', {'bands': bands})

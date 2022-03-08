from unicodedata import category
from django.shortcuts import redirect, render
from .models import Category,Image
# Create your views here.
def gallery(request):
    category= request.GET.get('category')
    if category == None:
        images = Image.objects.all()
    else:
        images = Image.objects.filter(category__name=category) 
        
            
    categories = Category.objects.all()
    context = {'categories': categories,'images': images}
    return render(request,'images/gallery.html',context)

def viewImage(request,pk):
    image = Image.objects.get(id=pk)
    return render(request,'images/images.html', {'image': image})

def addImage(request):
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
    
        if data['category'] != 'none':
            category = Category.objects.get(id=data[category])
        elif data['category_new'] != '':
            category,created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
            image = Image.objects.create(
                category=category,
                description = data['description'],
                image= image,
            )
            
            return redirect('gallery')
    context ={ 'categories': categories}
    return render(request,'images/add.html')
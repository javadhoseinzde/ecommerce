from django.shortcuts import render
from django.http import JsonResponse

from django.template.loader import render_to_string

from django.views.generic import ListView, DetailView
from .models import Product, Images, Variants
from .query import filter_product, get_product ,get_comment, get_slider, get_image


class IndexView(ListView):
    template_name = "shop/index.html"

    def get_queryset(self):
        queryset = {
            "query": filter_product(),
            "slider": get_slider()
        }
        return queryset

class ProductDetail(DetailView):
    template_name = "shop/product-detail1.html"

    def get_object(self):
        pk = self.kwargs.get("pk")
        query = Product.objects.get(pk=pk)
        print(type(query.data))
        for i in query.data:
            
            print(str(i) + " == " + str(query.data[i]))
        queryset = {
            "detail": get_product(pk),
            "comment": get_comment(pk),
            "image":get_image(pk),
            "product":filter_product()
        }
        print(get_image(pk))
        return queryset
    

def product_detail(request,id,slug):
    query = request.GET.get('q')
    print("salam")
    # >>>>>>>>>>>>>>>> M U L T I   L A N G U G A E >>>>>> START

    #category = categoryTree(0, '', currentlang)


    print("salam")


    product = Product.objects.get(pk=id)
    #q = product.data
    
    print("salam")


    # <<<<<<<<<< M U L T I   L A N G U G A E <<<<<<<<<<<<<<< end

    images = Images.objects.filter(product_id=id)
    print("salam")  

    comments = get_comment(id)
    print("salam")

    context = {'product': product,
               'images': images, 'comments': comments,
               }
    print("salam")

    if product.variant !="None": # Product have variants
        print("salam")

        if request.method == 'POST': #if we select color
            print("salam az dakhele variant_id")
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id) #selected product by click color radio
            colors = Variants.objects.filter(product_id=id)
            print("salam")

        else:
            variants = Variants.objects.filter(product_id=id)
            print("salam")

            colors = Variants.objects.filter(product_id=id)
            # sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id',[id])
            variant =Variants.objects.get(id=variants[0].id)
        context.update({'colors': colors,
                        'variant': variant,'query': query,
                        'comments':comments
                        })
    return render(request,'shop/product-detail.html',context)



def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)




class ProductList(ListView):
    template_name = "shop/product-list.html"
    
    def get_queryset(self):
        return Product.objects.all()
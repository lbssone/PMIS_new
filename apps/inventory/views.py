from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import Product, Component, Material

# Create your views here.
class InventoryList(TemplateView):
    template_name = 'modules/inventory/inventory.html'

    def get_context_data(self, **kwargs):
        context = super(InventoryList, self).get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        context['component_list'] = Component.objects.all()
        context['material_list'] = Material.objects.all()
        return context
    # model = Product, Component, Material

    # def get(self, request):
    #     product_list = Product.objects.all()
    #     component_list = Component.objects.all()
    #     material_list = Material.objects.all()
    #     return render(request, 'modules/inventory/inventory.html', {'product_list': product_list, 'component_list': component_list, 'material_list': material_list})


class ProductDetail(DetailView):
    model = Product
    template_name = 'modules/inventory/product_detail.html'
    context_object_name = 'product'

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetail, self).get_context_data(**kwargs)
    #     context['components_required'] = Product.getComponents(self)
    #     return context


class ScheduleForm(View):
    def get(self, request):
        return render(request, 'modules/inventory/schedule_form.html')

    def post(self, request):
        get_um = request.POST.get('umbrella')
        num = int(request.POST.get('num_of_umbrella'))
        umbrella = ""
        if get_um == "抗UV直傘":
            umbrella = Product.objects.get(number="1")
        elif get_um == "防風直傘":
            umbrella = Product.objects.get(number="2")
        elif get_um == "輕量直傘":
            umbrella = Product.objects.get(number="3")
        component_tree_list = []
        material_list = []
        plastic = 0
        frp = 0
        fabric = 0
        plastic_q = 0
        for component in umbrella.components_required.all():
            component_wanted = component.number_needed*num
            component_quan = component_wanted - component.inventory
            component_tree_list.append([component.name, component.number_needed, component.weight, component_wanted, component.inventory, component_quan])
            if component.required_material not in material_list:
                material_list.append(component.required_material)
            if component.required_material.name == "塑膠":
                plastic += (component.weight * component_quan)
            if component.required_material.name == "玻璃纖維(FRP)":
                frp += (component.weight * component_quan)
            if component.required_material.name == "黑膠傘布":
                fabric += (component.weight * component_quan)
                fabric_q = fabric - Material.objects.get(name="黑膠傘布").inventory
            if component.required_material.name == "防潑水傘布":
                fabric += (component.weight * component_quan)
                fabric_q = fabric - Material.objects.get(name="防潑水傘布").inventory
        # plastic = plastic * num 
        # frp = frp * num 
        # fabric = fabric * num
        plastic_q = plastic - Material.objects.get(name="塑膠").inventory
        frp_q = frp - Material.objects.get(name="玻璃纖維(FRP)").inventory
        return render(request, 'modules/inventory/schedule_form.html',
            {'component_tree_list': component_tree_list, 'material_list': material_list, 'plastic': plastic, 
            'frp': frp, 'fabric': fabric, 'name': get_um, 'p_quan': plastic_q, 'frp_quan': frp_q, 'fabric_quan': fabric_q})


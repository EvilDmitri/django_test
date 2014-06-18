import json
from django.db.models import get_model
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext


def get_qs(request, model_name):
    model = get_model('dynamic_models', model_name)
    if not model:
        raise Http404
    field_names = [f.name for f in model._meta.fields if f.name is not 'id']
    qs = model.objects.all().values_list(*field_names)
    fields = [f.verbose_name for f in model._meta.fields if f.verbose_name is not 'id']
    result = {'fields': fields, 'qs': list(qs), 'names': field_names}
    if request.is_ajax():
        return HttpResponse(json.dumps(result),
                            mimetype='application/json')
    else:
        raise Http404


def create(request, model_name):
    model = get_model('dynamic_models', model_name)
    if not model:
        raise Http404
    fields = [f.name for f in model._meta.fields if f.name is not 'id']
    new_fields = dict()
    for field in fields:
        new_fields[field] = request.POST.get(field)


    new_obj = model.objects.create(**new_fields)
    new_obj.save()
    return HttpResponse(json.dumps('OK'),
                        mimetype='application/json')
    # except ValueError:
    #     return HttpResponse(json.dumps('Wrong value'),
    #                         mimetype='application/json')




def change(request, model_name, id):
    model = get_model('dynamic_models', model_name)
    if not model:
        raise Http404
    fields = [f.name for f in model._meta.fields]
    qs = model.objects.get(pk=id)

    new_fields = dict()
    for field in fields:
        new_fields[field] = request.POST.get(field)
        setattr(qs, field, new_fields[field])

    print new_fields


def model_list(request):
    if request.is_ajax():
        raise Http404
    return render_to_response('dynamic_models/model_list.html',
                              {'data': 'data'},
                              context_instance=RequestContext(request)
    )

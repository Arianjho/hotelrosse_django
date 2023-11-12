from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Habitacion, Huesped, Huespedxhabitacion
from django.http import HttpResponse
from openpyxl import Workbook
from django.http import JsonResponse
import datetime, requests

def inicio(request):
    habitaciones = Habitacion.objects.all()
    huespedes_ocupando = Huespedxhabitacion.objects.filter(estado=1).values_list('huesped_rel_id', flat=True)
    huespedes = Huesped.objects.filter(estado=1).exclude(id__in=huespedes_ocupando)
    huespedesxhab = Huespedxhabitacion.objects.filter(estado=1).all()

    context = {
        "habitaciones": habitaciones,
        "huespedes": huespedes,
        "huespedesxhab": huespedesxhab
    }

    if request.method == "POST":
        if 'agregar_huespedes' in request.POST:
            modalid = request.POST.get('modalid')
            huespedes_form = request.POST.getlist('huespedes')
            habitacion_id = request.POST.get('idhabitacion')
            ingreso = request.POST.get('ingreso')
            salida = request.POST.get('salida')
            tarifa = request.POST.get('tarifa')

            for huesped_id in huespedes_form:
                nuevos_accesos = Huespedxhabitacion(ingreso=ingreso, salida=salida, tarifa=tarifa, habitacion_rel_id=habitacion_id, huesped_rel_id=huesped_id, estado=1)
                nuevos_accesos.save()

            habitacion = get_object_or_404(Habitacion, id=habitacion_id)
            habitacion.estado = 3
            habitacion.save()

            messages.success(request, "Los huespedes fueron agregados correctamente!")
            messages.warning(request, modalid)

        if 'forzar_salida' in request.POST:
            habitacion_id_rel = request.POST.get('idhabitacion_rel')
            Huespedxhabitacion.objects.filter(habitacion_rel_id=habitacion_id_rel).update(estado=0)
            
            habitacion_rel = get_object_or_404(Habitacion, id=habitacion_id_rel)
            habitacion_rel.estado = 1
            habitacion_rel.save()

            messages.info(request, f"La salida de la habitacion N°{habitacion_rel.habitacion} fue forzada!")

        return redirect('inicio')

    return render(request, 'inicio.html', context)

def habitaciones(request):
    habitaciones_list = Habitacion.objects.all()
    ultima_habitacion = Habitacion.objects.order_by('id').last()

    if request.method == "POST":
        habitacion = request.POST.get('habitacion')
        tipo = request.POST.get('tipo')

        nueva_habitacion = Habitacion(habitacion=habitacion, tipo=tipo, estado=1)
        nueva_habitacion.save()

        messages.success(request, "La habitacion fue agregada correctamente!")
        return redirect('habitaciones')

    context = {
        'habitaciones': habitaciones_list,
        'last_hab': ultima_habitacion.habitacion,
        'tipos': ["Individual", "Matrimonial", "Doble", "Triple"],
        'estados': list(enumerate(["No disponible", "Disponible", "En mantenimiento"]))
    }
    
    return render(request, 'habitaciones.html', context)

def habitacion_update(request, idhabitacion):
    habitacion = get_object_or_404(Habitacion, id=idhabitacion)

    if request.method == "POST":
        habitacion_form = request.POST.get('habitacion')
        tipo = request.POST.get('tipo')
        estado = request.POST.get('estado')

        habitacion.habitacion = habitacion_form
        habitacion.tipo = tipo
        habitacion.estado = estado
        habitacion.save()

        messages.info(request, "La habitación fue actualizada correctamente!")
    else:
        messages.error(request, "Ocurrió un error al editar la habitación")

    return redirect('habitaciones')

def habitacion_delete(request, idhabitacion):
    habitacion = get_object_or_404(Habitacion, id=idhabitacion)

    if request.method == "POST":
        if habitacion:
            habitacion.delete()
            messages.info(request, "La habitación fue eliminada correctamente")
        else:
            messages.error(request, "Ocurrió un error al eliminar la habitación")

    return redirect('habitaciones')

def huespedes(request):
    huespedes_list = Huesped.objects.filter(estado=1)

    if request.method == "POST":
        dni = request.POST.get('dni')
        huesped = request.POST.get('huesped')
        direccion = request.POST.get('direccion')
        estado_civil = request.POST.get('estado_civil')
        telefono = request.POST.get('telefono')
        ciudad = request.POST.get('ciudad')
        pais = request.POST.get('pais')
        profesion = request.POST.get('profesion')
        
        nuevo_huesped = Huesped(dni=dni, huesped=huesped, direccion=direccion, estado_civil=estado_civil, telefono=telefono, ciudad=ciudad, pais=pais, profesion=profesion, estado=1)
        nuevo_huesped.save()

        messages.success(request, "El huesped fue agregado correctamente!")
        return redirect('huespedes')

    context = {
        'huespedes': huespedes_list,
    }
    
    return render(request, 'huespedes.html', context)

def huesped_update(request, idhuesped):
    huesped = get_object_or_404(Huesped, id=idhuesped)

    if request.method == "POST":
        dni = request.POST.get('dni')
        huesped_form = request.POST.get('huesped')
        direccion = request.POST.get('direccion')
        estado_civil = request.POST.get('estado_civil')
        telefono = request.POST.get('telefono')
        ciudad = request.POST.get('ciudad')
        pais = request.POST.get('pais')
        profesion = request.POST.get('profesion')

        huesped.dni = dni
        huesped.huesped = huesped_form
        huesped.direccion = direccion
        huesped.estado_civil = estado_civil
        huesped.telefono = telefono
        huesped.ciudad = ciudad
        huesped.pais = pais
        huesped.profesion =profesion
        huesped.save()

        messages.info(request, "Los datos del huesped se actualizó correctamente!")
    else:
        messages.error(request, "Ocurrió un error al actualizar los datos del huesped")

    return redirect('huespedes')

def huesped_delete(request, idhuesped):
    huesped = get_object_or_404(Huesped, id=idhuesped)

    if request.method == "POST":
        if huesped:
            huesped.estado = 0;
            huesped.save()
            messages.info(request, "El huesped fue eliminado correctamente")
        else:
            messages.error(request, "Ocurrió un error al eliminar el huesped")

    return redirect('huespedes')

def descargar(request):
    if request.method == 'POST':
        mes = int(request.POST.get('mes'))
        year = datetime.datetime.now().year
        start_date = datetime.date(year, mes, 1)
        if mes == 12:
            end_date = datetime.date(year+1, 1, 1)
        else:
            end_date = datetime.date(year, mes+1, 1)
        
        registros = Huespedxhabitacion.objects.filter(ingreso__date__range=(start_date, end_date))

        wb = Workbook()
        ws = wb.active

        ws.append(['Habitacion', 'Ingreso', 'Salida Probable', 'Tarifa', 'Huesped',  'DNI', 'Estado Civil', 'Ciudad', 'Pais', 'Direccion', 'Profesion u ocupacion'])

        for registro in registros:
            ingreso = registro.ingreso.astimezone().replace(tzinfo=None)
            ws.append([str(registro.habitacion_rel.habitacion), ingreso,  registro.salida, registro.tarifa, str(registro.huesped_rel.huesped), str(registro.huesped_rel.dni), str(registro.huesped_rel.estado_civil), str(registro.huesped_rel.ciudad), str(registro.huesped_rel.pais), str(registro.huesped_rel.direccion), str(registro.huesped_rel.profesion)])

        for column in ws.columns:
            max_length = 0
            column = [cell for cell in column]
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2)
            ws.column_dimensions[column[0].column_letter].width = adjusted_width

        mes_nombre = start_date.strftime('%B')
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="registros_{mes_nombre}_{year}.xlsx"'

        wb.save(response)
        return response
    else:
        return HttpResponse("Método no permitido", status=405)
    
def proxy(request, dni):
    url = f"https://api.apis.net.pe/v2/reniec/dni?numero={dni}"

    headers = {
        'Authorization': 'Bearer apis-token-5672.AOO1BHFkHRjnPgSyrwku3bA0ZLviqsZ8'
    }

    response = requests.get(url, headers=headers)
    
    return JsonResponse(response.json(), safe=False)
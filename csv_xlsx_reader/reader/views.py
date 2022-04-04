import pathlib
from django.shortcuts import redirect, render
import datetime
from utils.utils import Utils
from .models import Xlsx, Uploader, CsvModel
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/login/")
def dashboard(request):
    files = Uploader.objects.filter(user=request.user)
    context = {"files": files}
    return render(request, "dashboard.html", context)


def upload_files(request):
    valid_ext = [".xlsx", ".csv"]
    message = None
    document = None
    if request.method == "POST" and request.FILES["file"]:
        name = request.POST.get("name", "")
        file = request.FILES.get("file", "")
        extension = pathlib.Path(file.name).suffix
        if(str(extension) in valid_ext):
            document = Uploader(name=name, file=file, user=request.user)
            document.save()
            message = None
            return redirect(f"/lector/read_file/{document.id}")
        else:
            message = "Archivo no Valido"
    return render(request, 'upload_files.html', {"message": message})


@login_required(login_url="/login/")
def read_file(request, id):
    file = Uploader.objects.get(pk=id)
    extension = pathlib.Path(file.file.path).suffix
    if(extension == ".csv"):
        return redirect(f"/lector/save_csv/{file.id}")
    else:
        return redirect(f"/lector/save_excel/{file.id}")


@login_required(login_url="/login/")
def save_csv(request, id):
    file = Uploader.objects.get(pk=id)
    data = Utils.read_csv(file.file.path)
    for row in data:
        date = row["Date"].split("-")[::-1]
        date_formated = datetime.datetime(
            int(date[0]), Utils.month_to_number(date[1]), int(date[2]))
        CsvModel.objects.create(
            date=date_formated,
            description=row["Description"],
            deposits=float(row["Deposits"].replace(",", "")),
            withdrawls=float(row["Withdrawls"].replace(",", "")),
            balance=float(row["Balance"].replace(",", "")),
            document=file,
        )
    return redirect("/lector/dashboard/")


@login_required(login_url="/login/")
def save_excel(request, id):
    file = Uploader.objects.get(pk=id)
    data = Utils.read_excel(file.file.path)
    for index in data.index:
        order_data = data["Order Date"][index]
        order_data_formated = Utils.formate_date(order_data)
        ship_date = data["Ship Date"][index]
        ship_date_formated = Utils.formate_date(ship_date)
        Xlsx.objects.create(
            region=data["Region"][index],
            country=data["Country"][index],
            item_type=data["Item Type"][index],
            sales_channel=data["Sales Channel"][index],
            order_priority=data["Order Priority"][index],
            order_date=order_data_formated,
            order_id=int(data["Order ID"][index]),
            ship_date=ship_date_formated,
            units_sold=int(data["Units Sold"][index]),
            unit_price=float(data["Unit Price"][index]),
            unit_cost=float(data["Unit Cost"][index]),
            total_revenue=float(data["Total Revenue"][index]),
            total_cost=float(data["Total Cost"][index]),
            total_profit=float(data["Total Profit"][index]),
            document=file
        )
    return redirect("/lector/dashboard/")


@login_required(login_url="/login/")
def list_data(request, id):
    file = Uploader.objects.get(pk=id)
    extension = pathlib.Path(file.file.path).suffix
    if(extension == ".csv"):
        return redirect(f"/lector/list_csv/{file.id}")
    else:
        return redirect(f"/lector/list_excel/{file.id}")


@login_required(login_url="/login/")
def list_csv(request, id):
    file = Uploader.objects.get(pk=id)
    data = CsvModel.objects.filter(document=file)
    context = {"data": data}
    return render(request, "list_csv_view.html", context)


@login_required(login_url="/login/")
def list_excel(request, id):
    file = Uploader.objects.get(pk=id)
    data = Xlsx.objects.filter(document=file)
    context = {"data": data}
    return render(request, "list_xlsx_view.html", context)


@login_required(login_url="/login/")
def statistic(request):
    files = Uploader.objects.filter(user=request.user)
    if (request.method == "POST"):
        file = Uploader.objects.get(pk=request.POST.get("file-id"))
        extension = pathlib.Path(file.file.path).suffix
        if(extension == ".xlsx"):
            return redirect(f'/lector/statistics/excel/{file.id}')
        else:
            return redirect(f'/lector/statistics/csv/{file.id}')
    return render(request, 'statistics.html', {"files": files})


@login_required(login_url="/login/")
def statistic_excel(request, id):
    files = Uploader.objects.filter(user=request.user)
    file = Uploader.objects.get(pk=id)
    registers = Xlsx.objects.filter(document=file)
    rows_imported = registers.count()
    items = []
    regions = []
    orders = []
    order_by_items = {}
    for register in registers:
        if(str(register.item_type) not in items):
            items.append(str(register.item_type))
        if(str(register.region) not in regions):
            regions.append(str(register.region))
        if(str(register.order_priority) not in orders):
            orders.append(str(register.order_priority))
        if(str(register.item_type) not in list(order_by_items.keys())):
            order_by_items[str(register.item_type)] = [
                str(register.order_priority)]
        else:
            order_by_items[str(register.item_type)].append(
                str(register.order_priority))

    context = {
        "registers": registers,
        "files": files,
        "item_types": items,
        "regions": regions,
        "rows_imported": rows_imported,
        "orders": orders,
        "order_by_items": order_by_items
    }
    return render(request, 'excel_statistics.html', context)


@login_required(login_url="/login/")
def statistic_csv(request, id):
    files = Uploader.objects.filter(user=request.user)
    file = Uploader.objects.get(pk=id)
    registers = CsvModel.objects.filter(document=file)
    rows_imported = registers.count()
    descriptions = []
    transaction_by_year = {}

    for register in registers:
        if(str(register.description) not in descriptions):
            descriptions.append(str(register.description))
        if (register.date.year not in list(transaction_by_year.keys())):
            transaction_by_year[register.date.year] = [register.description]
        else:
            transaction_by_year[register.date.year].append(
                register.description)
    context = {
        "files": files,
        "registers": registers,
        "rows_imported": rows_imported,
        "description": descriptions,
        "transaction_by_year": transaction_by_year
    }

    return render(request, 'csv_statistics.html', context)

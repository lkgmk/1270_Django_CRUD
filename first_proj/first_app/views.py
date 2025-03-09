from django.shortcuts import render, HttpResponse, redirect
from .models import EmpDetails


# Create your views here.
def emp_details(request):
    # database operation to read the data form table

    # select * from EmpDetails
    details = EmpDetails.objects.all()

    # select * from EmpDetails where emp_name="AAAA"
    # single_data = EmpDetails.objects.get(emp_name="AAAA")

    context = {'details': details}
    # context = {'single_data': single_data}

    # return HttpResponse(data)
    return render(request, "EmpDetails.html", context)


def emp_details_home(request):
    return render(request, "EmpDetails_form.html")


def create_emp_details(request):
    mesg = "Not Saved"
    if request.method == "POST":
        # get the form data
        emp_name_form = request.POST['EmpName']
        emp_city_form = request.POST['EmpCity']
        emp_company_form = request.POST['EmpCompany']

        # save the form data into DB
        EmpDetails(emp_name=emp_name_form,
                   emp_city=emp_city_form,
                   emp_company=emp_company_form).save()

        mesg = "Data Saved"

    context = {'mesg': mesg}
    return render(request, "EmpDetails_form.html", context)


def delete_emp_details(request, pk):
    data = EmpDetails.objects.get(id=pk)
    data.delete()
    details = EmpDetails.objects.all()
    context = {'details': details}
    return render(request, "EmpDetails.html", context)


def update_emp_details(request, pk=None):
    if request.method == "POST":
        # get the form data
        emp_id_form = request.POST['EmpId']

        # data from database
        single_data = EmpDetails.objects.get(id=emp_id_form)

        # updated form data
        emp_name_form = request.POST['EmpName']
        emp_city_form = request.POST['EmpCity']
        emp_company_form = request.POST['EmpCompany']

        single_data.emp_name = emp_name_form
        single_data.emp_city = emp_city_form
        single_data.emp_company = emp_company_form

        single_data.save()
        return redirect('emp_details_url')

    if pk:
        single_data = EmpDetails.objects.get(id=pk)
    context = {'single_data': single_data}
    return render(request, "EmpDetails_update_form.html", context)

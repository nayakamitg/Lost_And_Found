from django.shortcuts import render,redirect,get_object_or_404
from Home.models import Person,Mails
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def home(request):
    AllPerson=Person.objects.all().order_by('-sno')
    data={
        "AllPerson":AllPerson
    }
    return render(request,"home.html",data)

def add_person(request):
    if request.method=="POST":
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        age=request.POST.get("age")
        height=request.POST.get("height")
        weight=request.POST.get("weight")
        address=request.POST.get("address")
        desc=request.POST.get("description")
        gender=request.POST.get("gender")
        photos=request.FILES["photo"]
        contact_person=request.POST.get("contact")
        contact_person_number=request.POST.get("phone")
        last_seen_loc=request.POST.get("last_seen")
        missing_date=request.POST.get("date_missing")

        con=Person(name=name,mobile=mobile,age=age,height=height,weight=weight,address=address,desc=desc,gender=gender,photos=photos,contact_person=contact_person,contact_person_number=contact_person_number,last_seen_loc=last_seen_loc,missing_date=missing_date)
        con.save()
        messages.success(request, "Missing Person Details Updated and Send the Mail and Notification in Police Station")
        html_message = f""" <table border='1'>
        <tr>
          <th>Name</th>
          <td>{name}</td>
        </tr>
     
        <tr>
          <th>Age</th>
          <td>{age}</td>
        </tr>
        <tr>
          <th>Gender</th>
          <td>{gender}</td>
        </tr>
        <tr>
          <th>Height</th>
          <td>{height} Feet</td>
        </tr>
        <tr>
          <th>Weight</th>
          <td>{weight} kg</td>
        </tr>
        <tr>
          <th>Mobile no.</th>
          <td>{mobile}</td>
        </tr>
       
          <th>Last Seen Location</th>
          <td>{last_seen_loc}</td>
        </tr>
         <tr>
          <th>Missing Date</th>
          <td>{missing_date}</td>
        </tr>
        <tr>
        <tr>
          <th>Contact person</th>
          <td>{contact_person}</td>
        </tr>
        <tr>
          <th>Contact Person Number</th>
          <td>{contact_person_number}</td>
        </tr>
        <tr>
          <th>Adddress</th>
          <td>{address}</td>
        </tr>
      
        <tr>
          <th>Descriptions</th>
          <td>{desc}</td>
        </tr>
      
      </table>
        """
        
        All_mail=Mails.objects.all()
        for i in All_mail:
            
            send_mail(
    name,
    "⚠️Missing Alert⚠️",
    "tempuser12345@sharklasers.com",
    [i.mails],
    fail_silently=False,
    html_message=html_message
)
        return redirect('home')


    return render(request,"add_person.html")



def detail(request,sno):
    person= get_object_or_404(Person, sno=sno)
    return render(request,"detail.html",{"person":person})

def edit(request,sno):
    person= get_object_or_404(Person, sno=sno)
    if request.method=="POST":
        person.name=request.POST.get("name")
        person.mobile=request.POST.get("mobile")
        person.age=request.POST.get("age")
        person.height=request.POST.get("height")
        person.weight=request.POST.get("weight")
        person.address=request.POST.get("address")
        person.desc=request.POST.get("description")
        person.gender=request.POST.get("gender")
        person.contact_person=request.POST.get("contact")
        person.contact_person_number=request.POST.get("phone")
        person.last_seen_loc=request.POST.get("last_seen")
        person.missing_date=request.POST.get("date_missing")
        person.f_status=request.POST.get("fstatus")
        person.save()
        return redirect('home')
    return render(request,"add_person.html",{"person":person})
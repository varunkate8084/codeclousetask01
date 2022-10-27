from django.shortcuts import render
from .import pool
from docx2pdf import convert

def Action_Interface(request):
        return render(request,"Interface.html")
def Submit_Records(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    uname=request.POST['uname']
    files = request.FILES['files']
    Q="insert into details(uname,files) values('{0}','{1}')".format(uname,files.name)
    print(Q)
    docfile=files.name
    l=len(docfile)
    docfile=docfile[0:l-5]
    F=open("d:/converttopdf/assets/"+files.name,'wb')
    for chunk in files.chunks():
        F.write(chunk)
    F.close()
    CMD.execute(Q)
    # print(type(docfile))
    # print(docfile)
    # print(r"D:\converttopdf\assets\{0}.docx".format(docfile),r"D:\converttopdf\assets\{0}.pdf".format(uname))
    convert(r"D:\converttopdf\assets\{0}.docx".format(docfile),r"C:\Users\varun\Downloads\{0}.pdf".format(docfile))
    DB.commit()
    DB.close()
    return render(request,'Interface.html',{'message': "PDF Successfully Downloaded in Computer"})
  except  Exception as d:
      print("error:",d)
      return render(request, 'Interface.html', {'message':'Record Failed'})

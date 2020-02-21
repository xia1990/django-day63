from django.shortcuts import render,redirect
from app01 import models
#图书管理系统

#图书列表
def book_list(request):
    #从数据库中查询所有图书信息
    book_list=models.Book.objects.all()
    #将图书信息返回到html页面上
    return render(request,"book_list.html",{"book_list":book_list})


#添加图书
def add_book(request):
    #get请求得到所有出版社名称
    if request.method=="GET":
        publisher_list=models.Publisher.objects.all()
        return render(request,"add_book.html",{'publisher_list':publisher_list})
    else:
        #post请求得到新添加的图书名称和选择的出版社的ID
        new_bname=request.POST.get("bname")
        new_publisher_id=request.POST.get("publisher")
        #去数据库中创建新添加的图书
        models.Book.objects.create(bname=new_bname,publisher_id=new_publisher_id)
        #返回到图书列表页面
        return redirect("/book_list/")


#删除图书
def delete_book(request):
    #得到要删除书籍的id
    del_id=request.GET.get("bid")
    print(del_id)
    print("="*100)
    #得到要删除书籍对象，并执行删除操作
    models.Book.objects.get(bid=del_id).delete()
    return redirect("/book_list/")


#编辑图书
def edit_book(request):
    if request.method=="GET":
        #得到所有的出版社
        publisher_list=models.Publisher.objects.all()
        #要编辑图书id
        edit_id=request.GET.get("bid")
        #得到要编辑图书对象(这里的bid是数据库中图书编号的属性)
        edit_book=models.Book.objects.get(bid=edit_id)
        return render(
            request,
            "edit_book.html",
            {"publisher_list":publisher_list,"book":edit_book}
        )
    else:
        #得到要编辑书的编号
        new_edit_id=request.POST.get("id")
        # 得到要编辑的图书对象
        edit_book = models.Book.objects.get(bid=new_edit_id)
        #得到要编辑书的名称（即修改后的书名）
        new_edit_name=request.POST.get("name")
        #得到要编辑出版社id
        new_edit_pid=request.POST.get("publisher")
        #更新图书名称和出版社编号
        edit_book.bname=new_edit_name
        edit_book.publisher_id=new_edit_pid
        #保存
        edit_book.save()
        #返回修改后的图书页面
        return redirect("/book_list/")







from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

# price and item mapping
items ={
    '1001':19.99,
    '1002':24.99,
    '1003':4.99,
    '1004':49.99
}

def index(request):
    return render(request,'amadon/index.html')

def buy(request):
    product_id = request.POST['product_id'] # product id
    unit_price = items[product_id]
    print('unit price is= '+str(unit_price))

    quantity = int(request.POST['quantity'])
    print('quantity is= '+str(quantity))
    purchase = round(unit_price * quantity, 2)
    print(type(purchase))
    print('purchase is='+str(purchase))

    if 'item_count' not in request.session or not request.session['item_count']:
        request.session['item_count'] = quantity
    else:
        curQuan = request.session['item_count']
        print('curQuan= '+str(curQuan))
        curQuan += quantity
        print('after update curQuan'+str(curQuan))
        request.session['item_count'] = curQuan
        request.session.modified = True

    if 'total_spend' not in request.session or not request.session['total_spend']:
        request.session['total_spend'] = purchase
    else:
        curPur = round(request.session['total_spend'],2)
        print(type(curPur))
        print('curPur= '+str(curPur))
        curPur += purchase
        curPur = round(curPur,2)
        print('after update curPur'+str(curPur))
        request.session['total_spend'] = curPur
        request.session.modified = True
   

    request.session['purchase'] = purchase
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request,'amadon/checkout.html')

def clearcart(request):
    del request.session['total_spend']
    del request.session['item_count']
    return redirect('/amadon')


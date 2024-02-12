from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import yfinance as yf
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import io 
import base64
from .models import Record, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from decimal import Decimal

data_uri, info = None, None

# Create your views here.
def home(request):
    global data_uri, info

    if request.method == 'GET':
        search_query = request.GET.get('search_query', 'BTC-USD')

        dummy_username = 'dummy_user'
        dummy_password = 'dummy_password'

        try:
            dummy_user = User.objects.get(username=dummy_username)
        except User.DoesNotExist:
            dummy_user = User.objects.create_user(username=dummy_username, password=dummy_password)
            user_profile = UserProfile.objects.create(user=dummy_user, total_cash=10000)

            Record.objects.create(user_profile=user_profile, stock='BHP', quantity=50, value=2000)
            Record.objects.create(user_profile=user_profile, stock='NAB', quantity=30, value=1200)

        login(request, dummy_user)

        user_profile = request.user.userprofile
        total_cash = user_profile.total_cash
        records = Record.objects.filter(user_profile=user_profile)

        if info is not None:
            print(info['symbol'], search_query)

        if info is None or info['symbol'] != search_query:
            data = yf.download(search_query, "2017-01-01") 
            try:
                info = yf.Ticker("ETH-USD").info
                dates = mdates.date2num(data.index.to_pydatetime())
                plt.plot_date(dates, data['Adj Close'], '-')

                plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
                plt.gca().xaxis.set_minor_locator(mdates.MonthLocator())

                plt.grid(True)
                plt.ylabel(r'Price [$]')
                plt.title(search_query)
                plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
                for label in plt.gca().get_xticklabels(which='major'):
                    label.set(rotation=30, horizontalalignment='right')

                buf = io.BytesIO() 
                plt.savefig(buf, format='png')
                buf.seek(0)

                data_uri = base64.b64encode(buf.read()).decode('utf-8')
                plt.close()
            except:
                data_uri = None
    else:
        user_profile = request.user.userprofile
        total_cash = user_profile.total_cash

        if 'item_quantity' in request.POST:
            quantity = int(request.POST.get('item_quantity'))
            stock = info['symbol']
            value = info['previousClose']
            value = Decimal(str(value))
            stock_value = quantity * value
            item_type = request.POST.get('item_type')

            try:
                record = Record.objects.get(stock=stock)
                if item_type == 'sell':
                    if quantity <= record.quantity:
                        transaction_amount = value * quantity
                        total_cash += transaction_amount
                        record.quantity -= quantity
                        record.value -= transaction_amount
                        messages.success(request, "Successful transaction")
                    else:
                        messages.error(request, 'Insufficient funds...')
                else:
                    transaction_amount = value * quantity
                    if transaction_amount > total_cash:
                        messages.error(request, "Insufficient funds...")
                    else:
                        messages.success(request, "Successful transaction")
                        total_cash -= transaction_amount
                        record.quantity += quantity
                        record.value += transaction_amount
                record.save()
                user_profile.total_cash = total_cash
                user_profile.save()

            except Record.DoesNotExist:
                if item_type == 'sell':
                    messages.error(request, 'Insufficient funds...')
                else:
                    transaction_amount = value * quantity
                    if transaction_amount > total_cash:
                        messages.error(request, "Insufficient funds...")
                    else:
                        total_cash -= transaction_amount
                        messages.success(request, "Successful transaction")
                        Record.objects.create(user_profile=user_profile, stock=stock, quantity=quantity, value=stock_value)
                        user_profile.total_cash = total_cash
                        user_profile.save()
                
        else:
            record_id = request.POST.get('record_id')
            transaction_quantity = int(request.POST.get('transaction_quantity'))
            transaction_type = request.POST.get('transaction_type')

            try:
                record = Record.objects.get(id=record_id)
                value = record.value / record.quantity
                value = Decimal(str(value))
                if transaction_type == 'buy':
                    transaction_amount = value * transaction_quantity
                    transaction_amount = Decimal(str(transaction_amount))
                    if transaction_amount > total_cash:
                        messages.error(request, "Insufficient funds...")
                    else:
                        messages.success(request, "Successful transaction")
                        total_cash -= transaction_amount
                        record.quantity += transaction_quantity
                        record.value += transaction_amount
                elif transaction_type == 'sell':
                    transaction_amount = value * transaction_quantity
                    transaction_amount = Decimal(str(transaction_amount))
                    total_cash += transaction_amount
                    record.quantity -= transaction_quantity
                    record.value -= transaction_amount
                    messages.success(request, "Successful transaction")

                record.save()
                user_profile.total_cash = total_cash
                user_profile.save()

            except Record.DoesNotExist:
                pass
        records = Record.objects.filter(user_profile=user_profile)

    return render(request, 'index.html', {'data_uri': data_uri, 'records' : records, 'total_cash': total_cash})
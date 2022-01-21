from app.models import Client


class FormList:

    @staticmethod
    def user_form_valid(request):
        names = request.POST.getlist('first_name')
        surnames = request.POST.getlist('last_name')
        phone_numbers = request.POST.getlist('phone')
        prices = request.POST.getlist('price')
        for i in range(len(phone_numbers) - 1):
            clients = Client.objects.filter(phone=phone_numbers[i])
            if not clients.exists():
                client = Client(
                    first_name=names[i],
                    last_name=surnames[i],
                    phone=phone_numbers[i],
                    price=prices[i],
                )
                client.save()
            else:
                client = clients.first()
                client.price += int(prices[i])
                if not client.first_name and names[i]:
                    client.first_name = names[i]
                if not client.last_name and surnames[i]:
                    client.last_name = surnames[i]
                client.count += 1
                client.save()
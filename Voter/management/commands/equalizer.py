from django.core.management.base import BaseCommand, CommandError
from Voter.models import Voters
from nominees.models import *
from nominees.views import *
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help ='Daily profit multiplies'
    def handle(self, *args, **options):
        users = Voters.objects.all()
        nominees = Nominees.objects.all()
        categories = Categories.objects.all()
        print("   ")
        print("   ")     
        print('*****Start of the log*****')
        for m in nominees:
            ids = m.name
            if m.name:
                print(m.name)
                print('Votes', Voters.objects.filter(voted_for=m.name, category=m.category).count())
                print('Category', Voters.objects.filter(category=m.category).count())
                nominee=Nominees.objects.filter(name=m.name, category=m.category).update(number_of_votes=Voters.objects.filter(voted_for=m.name, category=m.category).count())
                category=Categories.objects.filter(category_name=m.category).update(number_of_votes=Voters.objects.filter(category=m.category).count())
        print('*****End of the log*****')
        print("   ")
        print("   ")       
                # for k in nominee:
                #     if k.number_of_votes:
                        # print(k.number_of_votes)
                        # print(k.number_of_votes)
                # mogo = Voters.objects.filter(voted_for=n.fullname).count()
                # print(mogo)
                
                # if m.sign == Unconfirmed:
                #     if m.a_amount > 2:
                #         if m.Plan == 'Daily Plan':
                #             advcash = AdvCashDeposit.objects.get(user=m.user, hashid=m.hashid)
                #             bal = Investment.objects.get(user__username=advcash.user)
                #             amounte = UserInfo.objects.get(user__username=advcash.user)
                #             prie = Processors.objects.get(user__username=advcash.user)

                #             if advcash.package == Silver:
                #                 bal.balance = bal.balance + advcash.a_amount * 0.01
                #                 prie.adcash = prie.adcash + advcash.a_amount * 0.01

                #             elif advcash.package == Tarnish:
                #                 bal.balance = bal.balance + advcash.a_amount * 4 / 100
                #                 prie.adcash = prie.adcash + advcash.a_amount *  4 / 100

                #             elif advcash.package == Charoite:
                #                 bal.balance = bal.balance + advcash.a_amount * 6 / 100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 6 / 100

                #             elif advcash.package == TANZANITE:
                #                 bal.balance = bal.balance + advcash.a_amount * 0.8 /100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 0.8 /100

                #             elif advcash.package == Karat:
                #                 bal.balance = bal.balance + advcash.a_amount * 2.8/100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 2.8/100

                #             elif advcash.package == Corundum:
                #                 bal.balance = bal.balance + advcash.a_amount * 3.2/100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 3.2/100

                #             elif advcash.package == TITANIUM:
                #                 bal.balance = bal.balance + advcash.a_amount * 1.1/100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 1.1/100

                #             elif advcash.package == Niello:
                #                 bal.balance = bal.balance + advcash.a_amount * 2.2/100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 2.2/100

                #             elif advcash.package == DIAMOND:
                #                 bal.balance = bal.balance + advcash.a_amount * 3 /100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 3 /100

                #             elif advcash.package == Quartz:
                #                 bal.balance = bal.balance + advcash.a_amount * 0.8/100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 0.8/100

                #             elif advcash.package == Carbon:
                #                 bal.balance = bal.balance + advcash.a_amount * 2.8/100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 2.8/100

                #             elif advcash.package == Gold:
                #                 bal.balance = bal.balance + advcash.a_amount * 1.4/100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 1.4/100

                #             elif advcash.package == Silver:
                #                 bal.balance = bal.balance + advcash.a_amount * 0.01
                #                 prie.adcash = prie.adcash + advcash.a_amount * 0.01

                #             elif advcash.package == Platnum:
                #                 bal.balance = bal.balance + advcash.a_amount * 2.8/100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 2.8/100

                #             elif advcash.package == Pearl:
                #                 bal.balance = bal.balance + advcash.a_amount * 3/100
                #                 prie.adcash = prie.adcash + advcash.a_amount * 3/100
                #             amounte.save()
                #             advcash.save()
                #             prie.save()
                #             bal.save()


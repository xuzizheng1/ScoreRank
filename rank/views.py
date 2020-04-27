from django.shortcuts import render
from django.views import View

from rank.models import Score


class InputView(View):
    def post(self, request):
        # print(request.POST)
        client = request.POST.get('client')
        score = request.POST.get('score')
        try:
            client_exist = Score.objects.filter(client=client)
            if client_exist:
                client_exist[0].score = score
                client_exist[0].save()
            else:
                Score.objects.create(client=client, score=score)
        except Exception as e:
            print(e)
        return render(request, 'score.html')

    def get(self, request):
        return render(request, 'score.html')


class RankView(View):
    def get(self, request):
        scores = Score.objects.order_by('-score')
        return render(request, 'rank.html', {'scores': scores})

    def post(self, request):
        # print(request.POST)
        client = request.POST.get('client')
        min = int(request.POST.get('min'))
        max = int(request.POST.get('max'))
        score_list = []
        my_rank = None
        my_obj = None
        try:
            queryset = Score.objects.order_by('-score')
            if client:
                my_obj = queryset.get(client=client)
                my_score = my_obj.score
                my_rank = queryset.filter(score__gte=my_score).count()
            for i in range(min - 1, max):
                score_i = queryset[i]
                score_list.append([i + 1, score_i])
            # print(score_list)
        except Exception as e:
            print(e)
        context = {
            'score_list': score_list,
            'my_obj': my_obj,
            'my_rank': my_rank,
        }
        return render(request, 'rank2.html', context)

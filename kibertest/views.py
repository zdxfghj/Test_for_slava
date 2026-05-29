from django.shortcuts import render
import os
import json
from .models import Person,Card
from .serializers import PersonSerializer, CardSerializer
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .parser import parse_gift_file, get_random_questions
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.http import require_POST
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework import permissions


class CardsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number']

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


def index(request):
    # Вариант А: передаём вопросы прямо в шаблон (без API-запроса)
    file_path = os.path.join(settings.BASE_DIR, 'questions.gift')
    all_questions = parse_gift_file(file_path)
    selected = get_random_questions(all_questions, 10)

    context = {
        'questions_json': json.dumps(selected),
        'total_available': len(all_questions),
    }
    return render(request, 'kibertest/index.html', context)


def main(request):
    if 'lastname' in request.GET:
        lastname = request.GET.get('lastname')
    if 'year' in request.GET:
        year = request.GET.get('year')
    result = Person.objects.filter(name=lastname,year=year)
    if result.count() > 0:
        first = result.first()
        first.wentToLink = True
        first.save()
    return render(request, 'kibertest/main.html', )


def auth(request):
    return render(request, 'kibertest/auth.html')

@login_required
def search(request):
    return render(request, 'kibertest/search.html')


# def test_page(request):
#     """Страница с тестом"""
#     context = {
#         'questions_json': json.dumps(questions_data),
#         'total_available': total_questions_count
#     }
#     return render(request, 'test_page.html', context)


@require_POST
def save_test_result(request):
    """Сохранение результатов теста (первый этап)"""
    try:
        data = json.loads(request.body)

        person = Person.objects.create(

            name=data.get('name'),
            group=data.get('group'),
            answer=data.get('answer', 0),
            # Поля карты пока не заполнены
            takeCardNumber=False,
            takeCardCVV=False,
            takeCardFIO=False,
            takeCardDATA=False
        )

        return JsonResponse({
            'success': True,
            'message': 'Результаты теста сохранены',
            'person_id': person.id
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


def card_form_page(request):
    """Страница с формой для данных карты"""
    person_id = request.GET.get('person_id')
    if not person_id:
        return render(request, 'card_form.html', {'error': 'ID не указан'})

    person = get_object_or_404(Person, id=person_id)

    return render(request, 'card_form.html', {
        'person': person,
        'person_id': person_id
    })


@require_POST
def save_card_data(request):
    """Сохранение данных карты (второй этап)"""
    try:
        data = json.loads(request.body)
        person_id = data.get('person_id')

        if not person_id:
            return JsonResponse({'success': False, 'error': 'ID не указан'})

        person = get_object_or_404(Person, id=person_id)

        # Обновляем поля карты
        person.takeCardNumber = data.get('takeCardNumber', False)
        person.takeCardCVV = data.get('takeCardCVV', False)
        person.takeCardFIO = data.get('takeCardFIO', False)
        person.takeCardDATA = data.get('takeCardDATA', False)
        person.save()

        # Здесь можно сохранить сами данные карты в зашифрованном виде
        # или в отдельной модели

        return JsonResponse({
            'success': True,
            'message': 'Данные карты сохранены'
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)
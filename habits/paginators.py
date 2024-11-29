from rest_framework.pagination import PageNumberPagination


class HabitUserListPagination(PageNumberPagination):
    """
    Кастомный пагинатор для списка привычек пользователя
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
import calendar
from datetime import (
    date,
    timedelta,
)
from typing import Any

from django.contrib import admin


class CreatedAtFilter(admin.SimpleListFilter):
    title = "Created On"
    parameter_name = "created_at"

    def lookups(self, request: Any, model_admin: Any) -> Any:

        return [
            ("yesterday", "Yesterday"),
            ("today", "Today"),
            ("this_week", "This Week"),
            ("last_week", "Last Week"),
            ("this_month", "This Month"),
            ("last_month", "Last Month"),
        ]

    def queryset(self, request: Any, queryset: Any) -> Any:
        today = date.today()
        if self.value() == "yesterday":
            yesterday = today - timedelta(days=1)

            return queryset.filter(created_at__date=yesterday)

        if self.value() == "today":
            return queryset.filter(created_at__date=today)

        if self.value() == "tomorrow":
            tomorrow = today + timedelta(days=1)
            return queryset.filter(created_at__date=tomorrow)

        if self.value() == "this_week":
            start = today - timedelta(days=today.weekday())
            end = start + timedelta(days=6)
            return queryset.filter(
                created_at__date__gte=start, created_at__date__lte=end
            )

        if self.value() == "last_week":
            start = today - timedelta(days=today.weekday(), weeks=1)
            end = start + timedelta(days=6)
            return queryset.filter(
                created_at__date__gte=start, created_at__date__lte=end
            )

        if self.value() == "this_month":
            month = today.month
            year = today.year

            start = date(year, month, 1)
            end = date(
                year,
                month,
                calendar.monthrange(year, month)[1],
            )
            return queryset.filter(
                created_at__date__gte=start, created_at__date__lte=end
            )

        if self.value() == "last_month":
            month = today.month - 1
            year = today.year

            if month < 1:
                month = 12
                year -= year

            start = date(year, month, 1)
            end = date(
                year,
                month,
                calendar.monthrange(year, month)[1],
            )
            return queryset.filter(
                created_at__date__gte=start, created_at__date__lte=end
            )

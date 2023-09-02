USER_GROUPS = ["customer", "agent", "delivery_officer", "driver"]


USER_SEARCH_FIELDS = (
    "id",
    "phone_number",
    "first_name",
    "last_name",
    "alternate_phone_number",
)


REGISTRATION_DETAILS_SEARCH_FIELDS = (
    ("id",)
    + tuple(f"user__{search_field}" for search_field in USER_SEARCH_FIELDS)
    + tuple(
        f"registered_by__{search_field}" for search_field in USER_SEARCH_FIELDS
    )
)

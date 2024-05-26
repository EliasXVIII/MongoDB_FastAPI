def user_schema(user) -> dict: ## va a devolver un diccionario que va a contener un JSON con id username y el email.
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]}

# Creo otra lista de usuarios para hacer las consultas.
def users_schema(users) -> list:
    return [user_schema(user) for user in users]

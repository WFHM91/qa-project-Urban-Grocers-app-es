import data
import sender_stand_request

# Función para crear el body del kit con el nombre seleccionado.
def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

# Función para recuperar el authToken.
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

# Función para pruebas positivas.
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201

# Función para pruebas negativas.
def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

# ==========================================
#                CHECKLIST
# ==========================================

# Prueba 1. Crear un kit con un nombre de 1 carácter.
def test_01_create_kit_with_one_character_name():
    new_kit_body = get_kit_body("a")
    positive_assert(new_kit_body)

# Prueba 2. Crear un kit con un nombre de 511 caracteres (límite permitido).
def test_02_create_kit_with_511_character_name():
    new_kit_body = get_kit_body(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
        "dabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    )
    positive_assert(new_kit_body)

# Prueba 3. Crear un kit con un nombre de 0 caracteres.
def test_03_create_kit_with_0_character_name():
    new_kit_body = get_kit_body("")
    negative_assert_code_400(new_kit_body)

# Prueba 4. Crear un kit con un nombre de 512 caracteres (1 sobre el límite).
def test_04_create_kit_with_512_character_name():
    new_kit_body = get_kit_body(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
        "dabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
        "D"
    )
    negative_assert_code_400(new_kit_body)

# Prueba 5. Crear un kit con un nombre con caracteres especiales.
def test_05_create_kit_with_special_characters_name():
    new_kit_body = get_kit_body("\"№%@\",")
    positive_assert(new_kit_body)

# Prueba 6. Crear un kit con un nombre con espacios.
def test_06_create_kit_with_whitespace_name():
    new_kit_body = get_kit_body(" A Aaa ")
    positive_assert(new_kit_body)

# Prueba 7. Crear un kit con un nombre con números.
def test_07_create_kit_with_numbers_name():
    new_kit_body = get_kit_body("123")
    positive_assert(new_kit_body)

# Prueba 8. Crear un kit sin el parámetro "name".
def test_08_create_kit_without_name_param():
    new_kit_body = get_kit_body("")
    new_kit_body.pop("name")
    negative_assert_code_400(new_kit_body)

# Prueba 9. Crear un kit con un nombre con integer.
def test_09_create_kit_with_integer_name():
    new_kit_body = get_kit_body(123)
    negative_assert_code_400(new_kit_body)
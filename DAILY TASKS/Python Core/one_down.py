# Щойно звільнили вашого дуже пасивно-агресивного колегу.
# Поки він збирав свої речі, він швидко вставив жучок у вашу систему який перейменував все на тарабарщину.
# Він залишив дві записки на своєму столі, в одній записці текст: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz, в іншій: Uif usjdl up uijt lbub jt tjnqmf kvtu sfqmbdf fwfsz mfuufs xjui uif mfuufs uibu dpnft cfgpsf ju".
#
# Замість того, щоб годинами намагатись знайти помилку самому, ти вирішуєш спробувати її розшифрувати.
#
# Напиши функцію one_down, яка приймає рядок txt, і декодує його на один символ вниз, якщо аргумент не є рядком, функція повинна повертати Input is not a string. Функція повинна мати можливість обробляти великі та малі літери. Тобі не треба турбуватися про пунктуацію.
#
# Приклади:
#
# one_down("Ifmmp")  # повертає "Hello"
# one_down(["Привіт", "Світ"])  # повертає "Input is not a string"
# one_down("XiBu BcPvU dSbAz UfYu")  # повертає "WhAt AbOuT cRaZy TeXt"

def one_down(txt: str) -> str:
    if not isinstance(txt, str):
        return "Input is not a string"

    decoded_txt = ""
    for char in txt:
        if char.isalpha():
            char_code = ord(char.lower())
            if char_code == ord("a"):
                decoded_txt += "z" if char.islower() else "Z"
            else:
                decoded_txt += chr(char_code - 1).upper() if char.isupper() else chr(char_code - 1)
        else:
            decoded_txt += char

    return decoded_txt

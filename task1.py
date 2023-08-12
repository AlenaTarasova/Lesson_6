"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""

from task1_1 import date_validate

if __name__ == "__main__":
    print(date_validate("00.01.2000"))
    print(date_validate("16.04.2023"))
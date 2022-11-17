"""Генератор приветствий."""
import pprint


def Greeting(name: str) -> str:

    """Возвращает текст приветствия.

      Args:
          name: Имя пользователя

      Returns:
          str: Текст приветствия
      """
    pprint.pprint(name.title())
    return f'Привет, {name.title()}'

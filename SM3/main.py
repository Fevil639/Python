from spivrobitnyk import Spivrobitnyk
from menedzher import Menedzher

if __name__ == "__main__":
    # об'єкти
    s1 = Spivrobitnyk("Євгеній", 25000, 28, 10)
    s2 = Spivrobitnyk("Сергій", 15000, 30, 10)
    m1 = Menedzher("Стьопа", 30000, 30, 3, 10)
    m2 = Menedzher("Миша", 28000, 29, 6, 15)

    spivrobitnyky = [s1, s2, m1, m2]

    for sp in spivrobitnyky:
        print(f"Співробітник: {sp.get_imya()}")
        print(f"  Зарплата: {sp.rozrahuvaty_zarplatu():.2f} грн")
        print(f"  Бонус: {sp.rozrahuvaty_bonus():.2f} грн")
        if isinstance(sp, Menedzher):
            print(" ", sp.zvit())
        print("-" * 40)

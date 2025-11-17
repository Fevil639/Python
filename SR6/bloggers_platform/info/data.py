class BloggersData:
    def __init__(self):
        self.bloggers = [
            {
                "name": "ТехноЇжак",
                "category": "Технології",
                "description": "Розповідає про ПК.",
                "social": "https://t.me/TechnoHedgehog"
            },
            {
                "name": "Марія Волжанка",
                "category": "Подорожі",
                "description": "Ділиться досвідом подорожей світом.",
                "social": "https://instagram.com/mariacvolga1"
            },
            {
                "name": "ZWORMz Gaming",
                "category": "Ігри",
                "description": "Стріми на Twitch та YouTube.",
                "social": "https://twitch.tv/zwormzgaming"
            },
            {
                "name": "Petrenko",
                "category": "Ігри",
                "description": "Стріми на Twitch та YouTube.",
                "social": "https://twitch.tv/petrenko"
            }
        ]

    def get_all(self):
        return self.bloggers

    def get_by_id(self, blogger_id: int):
        try:
            return self.bloggers[blogger_id - 1]  # 1-based ID
        except IndexError:
            return None

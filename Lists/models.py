class Superhero:
    """
    Clase que representa un superhéroe o villano del dataset.
    """
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name} ({'Villano' if self.is_villain else 'Héroe'}) - {self.alias}"

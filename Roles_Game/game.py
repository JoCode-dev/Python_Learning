import random


class Player():
    def __init__(self, name, number_of_flasks=3, health=50):
        self.name = name
        self.number_of_flasks = number_of_flasks
        self.health = health

    def __str__(self):
        return f"({self.name}: {self.health} HP)"

    @property
    def damage(self):
        return random.randint(1, 10)

    @damage.setter
    def damage(self, value):
        raise 'Cette Valeur ne peut pas être modifiée'

    def attack(self, enemy: "Player"):
        dammage_inflicted = self.damage
        enemy.health -= dammage_inflicted
        print(f"{self.name} a infligé {dammage_inflicted} points de dégats à {enemy.name}")

    def take_flask(self) -> bool:
        if self.number_of_flasks:
            health_earned = random.randint(5, 50)
            self.health = health_earned
            print(f"Vous avez récupéré {health_earned} points de vie")
            self.number_of_flasks -= 1
            return True


def _show_instructions():
    pass


def _create_players() -> [Player, Player]:
    player_name = input("Entrez le nom du joueur: ")
    enemy_name = input("Entrez le nom de l'ennemi: ")

    return Player(name=player_name), Player(name=enemy_name)


def _start_game(player: Player, enemy: Player):
    skip_turn = False

    while player.health > 0 and enemy.health > 0:
        if skip_turn:
            print("Vous avez passé votre tour")
            enemy.attack(player)
            skip_turn = False
            continue

        action = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")

        if action == "1":
            # Attaque
            player.attack(enemy)

        elif action == "2":
            # Potion
            if player.take_flask():
                skip_turn = True

        # L'ennemi attaque
        enemy.attack(player)
        print(player)
        print(enemy)

    print(f"{player.name if player.health > 0 else enemy.name} a gagné 🎉 !")


def start():
    player, enemy = _create_players()
    _start_game(player, enemy)

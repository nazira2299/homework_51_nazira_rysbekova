from random import randint


class Cat:
    name = ''
    age = 1
    happiness = 40
    satiety = 40
    sleep = False

    @staticmethod
    def add_name(request):
        name = request.POST.get('name')
        if name:
            Cat.name = name

    @staticmethod
    def add_action(request):
        action = request.POST.get('action')

        if action == 'play':
            Cat.play_cat()
        elif action == 'feed':
            Cat.feed_cat()
        elif action == 'sleep':
            Cat.sleep_cat()
        else:
            pass

        if Cat.happiness < 0:
            Cat.happiness = 0

        if Cat.satiety < 0:
            Cat.satiety = 0


    @classmethod
    def feed_cat(cls):
        if cls.sleep == True:
            return

        if cls.satiety >= 100:
            cls.satiety = 100
            cls.happiness -= 30
            return

        cls.satiety += 15
        cls.happiness += 5

    @classmethod
    def play_cat(cls):
        if cls.sleep == True:
            cls.sleep = False
            cls.happiness -= 5
        else:
            cls.happiness += 15
            cls.satiety -= 10

        chance = randint(1, 3)
        if chance == 3:
            cls.happiness = 0
            return

    @classmethod
    def sleep_cat(cls):
        cls.sleep = True

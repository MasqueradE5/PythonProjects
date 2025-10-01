from abc import ABC, abstractmethod
import random

class Crewmember:
    def __init__(self,name,rank,health,energy):
        self.name = name
        self.rank = rank
        self.health = health
        self.energy = energy

    @abstractmethod
    def work(self):
        pass

    def rest(self):
        self.energy += 30
        if self.energy > 100:
            self.energy = 100
        self.health += 5
        if self.health > 100:
            self.health = 100
        return f"{self.name} немного отдохнул"

    def status_report(self):
        return f"{self.name} в звании {self.rank}. Показатели здоровья равны: {self.health}/100. Показатели энергии: {self.energy}/100"

class Engeneer(Crewmember):
    def __init__(self, name, rank, health, energy, skill):
        super().__init__(name, rank, health, energy)
        self.skill = skill

    def work(self):
        if self.energy < 20:
            return f"{self.name} отчаянно пытается выполнить задачу но валится с ног от усталости"
        else:
            self.energy -= 20
            return f"{self.name} производит диагностику и ремонт систем"

    def mastery(self):
        return f"{self.name} обладает следующим уровнем навыка: {self.skill}"

class Pilot(Crewmember):
    def __init__(self, name, rank, health, energy, skill):
        super().__init__(name, rank, health, energy)
        self.skill = skill

    def work(self):
        if self.energy < 20:
            return f"{self.name} отчаянно пытается выполнить задачу но не может держать глаза открытыми"
        else:
            self.energy -= 20
            return f"{self.name} рассчитывает оптимальные маршруты и прогнозирует возможные столкновения"

    def mastery(self):
        return f"{self.name} имеет опыт пилотирования в часах: {self.skill}"

class Scientist(Crewmember):
    def __init__(self, name, rank, health, energy, research_field):
        super().__init__(name, rank, health, energy)
        self.research_field = research_field

    def work(self):
        if self.energy < 20:
            return f"{self.name} отчаянно пытается выполнить задачу но мысли путаются"
        else:
            self.energy -= 20
            return f"{self.name} проводит исследования в области {self.research_field}"

    def mastery(self):
        return f"{self.name} проводит исследования в области: {self.research_field}"

class Spaceship:
    def __init__(self,name,ship_type,crew_capacity,current_crew,hull_integrity):
        self.name = name
        self.ship_type = ship_type
        self.crew_capacity = crew_capacity
        self.current_crew = current_crew
        self.hull_integrity = hull_integrity

    def add_crew_member(self,name):
        self.current_crew.append(name)

    def remove_crew_member(self,name):
        self.current_crew.remove(name)

    def launch_mission(self,destination):
        return f"Экипаж корабля {self.name} отправляется в экспидицию на {destination}"

    def show(self):
        return self.current_crew

class SpaceStation:
    def __init__(self, name, crew, fleet, resources):
        self.name = name
        self.crew = crew
        self.fleet = fleet
        self.resources = resources

    def add_crew_member(self, name):
        self.crew.append(name)

    def assign_ship_to_fleet(self, ship):
        self.fleet.append(ship)

    def show_crew(self):
        return self.crew

    def show_fleet(self):
        return self.fleet

    def daily_routine(self):
        return f"На станции {self.name} выполняются ежедневные операции"

    def generate_report(self):
        return f"Экипаж: {self.crew} \n Флот: {self.fleet} \n Ресурсы станции:{self.resources}"

cur_resources = {'Еда': 90, 'Вода': 90, 'Кислород': 90}


ss= SpaceStation("Paradise", [], [], cur_resources) #1. Создайте объект космической станции класса SpaceStation и задайте ей название.

crew1 = Engeneer('Борис', 'Ассистент-инжинер', 100, 100, random.randint(5,30))     #2. Создайте несколько членов экипажа разных специализаций ( Engineer , Pilot , Scientist ), задав их характеристики
crew2 = Pilot('Татьяна', 'Помощник капитана', 60, 80, random.randint(1000, 8000))  #
crew3 = Scientist('Роберт', 'Доктор', 50, 100, 'Ксенобиология')                    #

ss.add_crew_member(crew1.name) #3. Добавьте созданных членов экипажа на станцию методом add_crew_member() .
ss.add_crew_member(crew2.name) #
ss.add_crew_member(crew3.name) #

ship1 = Spaceship("Аркадия", "Линкор", 1000, [], 100) #4. Создайте космический корабль класса Spacecraft , указав его параметры (название, тип, вместимость, прочность корпуса).

ss.assign_ship_to_fleet(ship1.name) #5. Включите созданный корабль во флот станции

ship1.add_crew_member(crew1.name) #6. Назначьте часть экипажа (например, пилота и инженера) на корабль методом assign_crew_to_ship() .
ship1.add_crew_member(crew2.name) #

print(crew1.work())             #7. Выполните работу экипажем: вызовите метод work() у каждого члена экипажа и выведите их отчёты через status_report()
print(crew1.status_report())    #
print(crew2.work())             #
print(crew2.status_report())    #
print(crew3.work())             #
print(crew3.status_report())    #

print(ship1.launch_mission('Марс')) #8. Запустите миссию корабля, вызвав метод launch_mission(destination) , указав пункт назначения.

print(crew3.work())             #9. Организуйте работу учёного, оставшегося на станции: вызовите его метод work() и выведите отчёт.
print(crew3.status_report())    #

print(ss.daily_routine()) #10. Выполните ежедневные операции станции, вызвав метод daily_operations() .

print(ss.generate_report()) #11. Сформируйте и выведите итоговый отчёт о состоянии станции и её компонентов методом generate_report() .

import sqlite3
conn = sqlite3.connect('resistance.db')
cursor = conn.cursor()
missionsstat= ['planned', 'in progress', 'complete', 'failed']
#Create 1.3 позывной будет уникальным изөза UNIQUE в типе данных поля
cursor.execute('''
    CREATE TABLE IF NOT EXISTS agents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codename TEXT UNIQUE,
        rank INTEGER CHECK(rank >= 1),
        skill TEXT,
        alive BOOLEAN
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS missions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        difficulty INTEGER CHECK(difficulty >= 1 AND difficulty <= 10),
        status TEXT,
        assigned_agent INTEGER NOT NULL,
        FOREIGN KEY (assigned_agent) REFERENCES agents(id) ON DELETE CASCADE
    )
''')
 #Закомментировать или удалить после первого запуска
#Create 1.1
agents_data = [
    ('Silverhand', 8, 'Проникновение', 0),
    ('Eagle', 5, 'Снайпер', 1),
    ('Polite', 6, 'Шпионаж', 0),
    ('Clever', 4, 'Саботаж', 1),
    ('Engine', 3, 'Лидерство', 1),
    ('Flick', 4, 'Зачистка', 1)
]

cursor.executemany('''
 INSERT INTO agents (codename, rank, skill, alive)
 VALUES (?, ?, ?, ?)
''', agents_data)
#Create 1.2 Закомментировать или удалить после первого запуска
missions_data = [
    ('Башня Арасака', 10, 'success', 1),
    ('Объединение', 2, 'in progress', 5),
    ('Маскарад', 4, 'success', 3),
    ('Культурный приём', 7, 'failde', 3),
    ('Лунный свет', 3,'success',2),
    ('Белый шум', 9, 'planned', 4),
    ('Атлантида', 1, 'success', 6),
    ('Сверхновая', 3, 'in progress', 6),
    ('Калипсо', 5, 'in progress', 4),
    ('Раскаяние', 7, 'failed', 2)
]

cursor.executemany('''
 INSERT INTO missions (title, difficulty, status, assigned_agent)
 VALUES (?, ?, ?, ?)
''', missions_data)

def mainCRUD_func():

    cursor.execute('''
    SELECT * FROM agents
    ORDER BY rank DESC''')
    results = cursor.fetchall()
    print('Read 2.1:')
    for row in results:
        print(row)

    print('Read 2.2')
    read2_2= input("введите ранк агента: ")
    cursor.execute('''
    SELECT * FROM agents
    WHERE alive > 0 AND rank >= ''' + read2_2)
    results = cursor.fetchall()
    for row in results:
        print(row)
    print('Read2.3')
    cursor.execute('''
    SELECT missions.id, missions.title, missions.difficulty, missions.status, agents.codename
    FROM missions
    LEFT JOIN agents ON agents.id = missions.assigned_agent
    ''')
    results = cursor.fetchall()
    for row in results:
        print(row)

    test= []
    max_diff = 0
    cursor.execute('''
    SELECT missions.id, missions.title, missions.difficulty, missions.status, agents.codename
    FROM missions
    LEFT JOIN agents ON agents.id = missions.assigned_agent
    ''')
    results = cursor.fetchall()
    print('Read 2.4')
    for row in results:
        test.append(row)
    max_diff= max(test, key=lambda x: x[2])
    print(max_diff)
    # Далее CRUD операции будут реализованны через консоль.
    conn.commit()

def operator():
    print("1. Просмотр всех агентов")
    print("2. Просмотр всех миссий")
    print("3. Добавить миссию")
    print("4. Поменять статус миссии")
    print("5. Назад")
    op_input = int(input())
    if op_input == 1:
        agentcheck()
    elif op_input == 2:
        missioncheck()
    elif op_input == 3:
        new_mission()
    elif op_input == 4:
        changestatus()
    elif op_input == 5:
        select_client()
    else:
        print('неверный ввод')
        operator()

def admin():
    print("1. Работа с агентами")
    print("2. Смена рангов")
    print("3. Аналитика")
    print("4. Список агентов")
    print("5. Назад")
    op_input = int(input())
    if op_input == 1:
        agents_operations()
    elif op_input == 2:
        change_rank()
    elif op_input == 3:
        analysis()
    elif op_input == 4:
        agentcheck()
    elif op_input == 5:
        select_client()
    else:
        print("Неверный ввод")
        admin()

def missioncheck():
    cursor.execute('SELECT * FROM missions')
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.commit()
    select_client()

def agentcheck():
    cursor.execute('SELECT * FROM agents')
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.commit()
    select_client()

def new_mission():
    temp_title = input('Введите название миссии ')
    temp_diff = input('Введите сложность миссии ')
    temp_asagent= int(input('Введите индекс назначенного агента '))
    test= []
    agentisalive=[]
    cursor.execute('SELECT * FROM agents')
    results = cursor.fetchall()
    for row in results:
        test.append(row)
    conn.commit()
    operator()

    for i in range(len(test)):
        if test[i][0] == temp_asagent:
            agentisalive= test[i]
    if agentisalive[4] == False:
        print('Агент в состоянии не стояния')
        new_mission()
    else:
        temp_asagent= str(temp_asagent)
        cursor.execute(f'''
        INSERT INTO missions(title, difficulty, assigned_agent)
        VALUES({temp_title}, {temp_diff} , planned, {temp_asagent})''' )
        conn.commit()
        operator()


def changestatus():
    cursor.execute('SELECT * FROM missions')
    results = cursor.fetchall()
    for row in results:
        print(row)
    select_mission= input('Выберите индекс миссии которую надо поменять')
    print('Выберите новый статус миссии')
    print('1. planned')
    print('2. in progress')
    print('3. complete')
    print('4. failed')
    temp_status= int(input('Ваш выбор:'))
    if temp_status == 1:
        cursor.execute('UPDATE missions SET status = '+missionsstat[temp_status]+' WHERE id = '+str(select_mission))
        conn.commit()
        operator()
    elif temp_status == 2:
        cursor.execute('UPDATE missions SET status = '+missionsstat[temp_status]+' WHERE id = '+str(select_mission))
        conn.commit()
        operator()
    elif temp_status == 3:
        cursor.execute('UPDATE missions SET status = '+missionsstat[temp_status]+' WHERE id = '+str(select_mission))
        conn.commit()
        operator()
    elif temp_status == 4:
        cursor.execute('UPDATE missions SET status = '+missionsstat[temp_status]+' WHERE id = '+str(select_mission))
        conn.commit()
        operator()
    else:
        print('неверный ввод')
        changestatus()

def mission_counter():
    cursor.execute('''SELECT agents.codename, COUNT(missions.assigned_agent) as agent_mission
                   FROM agents
                   LEFT JOIN missions ON agents.id = missions.assigned_agent
                   GROUP BY agents.id, agents.codename''')
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.commit()
    analysis()

def skilled_missions_counter():
    cursor.execute('''SELECT agents.codename, COUNT(missions.assigned_agent) as agent_mission
                   FROM agents
                   LEFT JOIN missions ON agents.id = missions.assigned_agent
                   GROUP BY agents.id, agents.codename
                   HAVING COUNT(missions.assigned_agent) >= 3''')
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.commit()
    analysis()

def change_rank():
    temp_agent_id= input("Введите индекс агента")
    temp_new_agent_rank= input("Введите новый ранг агента")
    cursor.execute(f'''UPDATE agents SET rank ={temp_new_agent_rank} WHERE id ={temp_agent_id}''')
    conn.commit()

def analysis():
    print("1. Количество миссий каждого агента")
    print("2. Агенты у которых 3+ миссий")
    print("3. Назад")
    op_input = int(input("Ваш выбор:"))
    if op_input == 1:
        mission_counter()
    elif op_input == 2:
        skilled_missions_counter()
    elif op_input == 3:
        admin()
    else:
        print("Неверный ввод")
        analysis()

def select_client():
    print("1. Админ")
    print("2. Оператор")
    op_input = input("Ваш ввод: ")
    if int(op_input) == 1:
        admin()
    elif int(op_input) == 2:
        operator()
    else:
        print("Неверный ввод")
        select_client()

def agents_operations():
    print("1. Добавить агента")
    print("2. Изменить агента")
    print("3. Удалить агента")
    print("4. Назад")
    op_input = int(input("Ваш ввод: "))
    if op_input == 1:
        agent_add()
    elif op_input == 2:
        agent_update()
    elif op_input == 3:
        agent_delete()
    elif op_input == 4:
        admin()
    else:
        print("Неверный ввод")
        agents_operations()

def agent_add():
    temp_agent_data= []
    for i in range(1,4):
        if i == 1:
            temp_agent_data.append(input('Введите позывной агента'))
        if i == 2:
            temp_agent_data.append(input('Введите ранг агента'))
        if i == 3:
            temp_agent_data.append(input('Введите особые навыки агента'))
    cursor.execute('''INSERT INTO agents (codename, rank, skill)
                   VALUES('''+temp_agent_data[0]+''', '''+temp_agent_data[1]+''', '''+ temp_agent_data[2]+''')''')
    conn.commit()

def agent_update():
    agent_id= int(input("Введите индекс агента или любые буквы для выхода: "))
    temp_agent_data= []
    if agent_id.isdigit() == True:
        agents_operations()
    else:
        for i in range(1,5):
            if i == 1:
                temp_agent_data.append(input('Введите позывной агента'))
            if i == 2:
                temp_agent_data.append(input('Введите ранг агента'))
            if i == 3:
                temp_agent_data.append(input('Введите особые навыки агента'))
            if i == 4:
                temp_agent_data.append(input('Введите жив ли агент(1-жив 0-нет)'))
        cursor.execute('''UPDATE agents SET codename= '''+temp_agent_data[0]+''', rank= '''+temp_agent_data[1]+''', skill= '''+temp_agent_data[2]+''', alive='''+temp_agent_data[3]+f'''
        WHERE id = {agent_id}''')

def agent_delete():
    agent_id= input('Введите индекс агента или любые буквы для выхода: ')
    if agent_id.isdigit() == True:
        agents_operations()
    else:
        agent_id = int(agent_id)
        cursor.execute(f'DELETE FROM agents WHERE id = {agent_id}')
        conn.commit()

select_client()
conn.commit()
conn.close()

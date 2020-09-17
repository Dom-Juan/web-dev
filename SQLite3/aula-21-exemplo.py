import sqlite3

banco = sqlite3.connect('hello-world.db')

#banco.execute('''
#    create table company
#    (
#        id int primary key not null,
#        name text not null,
#        age int not null,
#        address char(50),
#        salary real
#    );
#''')

#print("Tabela criada com sucesso!!!\n\n")

banco.close()

banco = sqlite3.connect('hello-world.db')

#banco.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1,'Paul',32,'California',20000.00)")
#banco.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2,'James',23,'California',400.00)")
#banco.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3,'A',22,'California',200.00)")
#banco.commit()

#print("Elementos adicionados com sucesso!!!\n\n")
#banco.close()

cursor = banco.execute("SELECT id, name, address, salary from COMPANY")

for row in cursor:
    print("ID: ",row[0])
    print("NAME: ",row[1])
    print("ADDRESS: ",row[2])
    print("SALARY: ",row[3])
    print("\n")

banco.close()

banco = sqlite3.connect('hello-world.db')

banco.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
banco.commit()

cursor = banco.execute("SELECT id, name, address, salary from COMPANY")
print("Agora feito com mudanças!\n")
for row in cursor:
    print("ID: ",row[0])
    print("NAME: ",row[1])
    print("ADDRESS: ",row[2])
    print("SALARY: ",row[3])
    print("\n")

banco.close()

banco = sqlite3.connect('hello-world.db')

banco.execute("DELETE from COMPANY where ID = 2")
banco.commit()

print("Número de remoções: ", banco.total_changes)

cursor = banco.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID: ",row[0])
    print("NAME: ",row[1])
    print("ADDRESS: ",row[2])
    print("SALARY: ",row[3])
    print("\n")

banco.close()



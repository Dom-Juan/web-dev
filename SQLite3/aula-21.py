import sqlite3

banco = sqlite3.connect('aula-21.db')


banco.execute('''
    create table address
    (
        id int primary key not null,
        cidade char(50),
        bairro text not null,
        rua char(50),
        numero int not null
    );
''')

banco.execute('''
    create table people
    (
        id int primary key not null,
        name text not null,
        CPF char(50)
    );
''')

print("Tabela criada com sucesso!!!\n\n")


banco.execute("INSERT INTO PEOPLE (ID,NAME,CPF) VALUES (1,'A','0123456-11')")
banco.execute("INSERT INTO PEOPLE (ID,NAME,CPF) VALUES (2,'D','7899101-15')")
banco.execute("INSERT INTO PEOPLE (ID,NAME,CPF) VALUES (3,'C','1213141-16')")
banco.commit()

banco.execute("INSERT INTO ADDRESS (ID,CIDADE,BAIRRO,RUA,NUMERO) VALUES (1,'São Paulo','Imirim','R. Angelica',110)")
banco.execute("INSERT INTO ADDRESS (ID,CIDADE,BAIRRO,RUA,NUMERO) VALUES (2,'Rio de Janeiro','Sei lá','Dom Pedro',10)")
banco.execute("INSERT INTO ADDRESS (ID,CIDADE,BAIRRO,RUA,NUMERO) VALUES (3,'Bahia','Nao conheço','R. Rua',9)")
banco.commit()

print("Elementos adicionados com sucesso!!!\n\n")

print("Mostrando elementos Tabela 1:\n")
cursor = banco.execute("SELECT * FROM PEOPLE")

for row in cursor:
    print("ID: ",row[0])
    print("NAME: ",row[1])
    print("CPF: ",row[2])
    print("\n")

print("Mostrando elementos Tabela 2:\n")
cursor = banco.execute("SELECT * FROM PEOPLE JOIN ADDRESS ON PEOPLE.id = ADDRESS.id")

for row in cursor:
    print("ID: ",row[3])
    print("CIDADE: ",row[4])
    print("BAIRRO: ",row[5])
    print("RUA: ",row[6])
    print("NUMERO: ",row[7])
    print("\n")

print("Mostrando elementos Tabela 1 + Tabela 2:\n")

cursor = banco.execute("SELECT * FROM PEOPLE JOIN ADDRESS ON PEOPLE.id = ADDRESS.id")

for row in cursor:
    print("ID: ",row[0])
    print("NAME: ",row[1])
    print("CPF: ",row[2])
    print("CIDADE: ",row[3])
    print("BAIRRO: ",row[4])
    print("RUA: ",row[5])
    print("NUMERO: ",row[6])
    print("\n")

print("Realizando Remoções...\n")
banco.execute("DELETE from PEOPLE where ID = 2")
banco.execute("DELETE from ADDRESS where ID = 2")

cursor = banco.execute("SELECT * FROM PEOPLE JOIN ADDRESS ON PEOPLE.id = ADDRESS.id")

print("Número de remoções: ", banco.total_changes)
for row in cursor:
    print("ID: ",row[0])
    print("NAME: ",row[1])
    print("CPF: ",row[2])
    print("CIDADE: ",row[3])
    print("BAIRRO: ",row[4])
    print("RUA: ",row[5])
    print("NUMERO: ",row[6])
    print("\n")


print("Realizando Update:\n")

banco.execute("UPDATE PEOPLE set Name = 'B' where ID = 1")
cursor = banco.execute("SELECT * FROM PEOPLE JOIN ADDRESS ON PEOPLE.id = ADDRESS.id")
for row in cursor:
    print("ID: ",row[0])
    print("NAME: ",row[1])
    print("CPF: ",row[2])
    print("CIDADE: ",row[4])
    print("BAIRRO: ",row[5])
    print("RUA: ",row[6])
    print("NUMERO: ",row[7])
    print("\n")

banco.close()



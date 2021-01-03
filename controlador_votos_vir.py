import psycopg2

def crear_tablas():
    commands = (
        """CREATE TABLE departamento(
            codigo_departamento VARCHAR(5) PRIMARY KEY,
            nombre_departamento VARCHAR(45) NOT NULL)
        """,
        """CREATE TABLE provincia(
            codigo_prov VARCHAR(5) PRIMARY KEY,
            nombre_prov VARCHAR(80) NOT NULL,
            departamento_prov VARCHAR(5) REFERENCE departamento NOT NULL)
        """,
        """CREATE TABLE distrito(
            codigo_distri VARCHAR(5) PRIMARY KEY,
            nombre_distri VARCHAR(80) NOT NULL,
            provincia_distri VARCHAR(5) REFERENCE provincia NOT NULL)
        """,
        """CREATE TABLE partidos(
            codigo_partido INTEGER PRIMARY KEY,
            nombre_partido VARCHAR(80) NOT NULL,
            candidato_presidencia VARCHAR(80) NOT NULL,
            primera_vicepresidencia VARCHAR(80) NOT NULL,
            segunda_vicepresidencia VARCHAR(80) NOT NULL)
        """,
        """CREATE TABLE poblacion_capital_distrito(
            dni INTEGER PRIMARY KEY,
            codigo_verificacion_dni INTEGER,
            nombre_completo VARCHAR(100) NOT NULL,
            distrito_poblacion_capital VARCHAR(5) REFERENCE distrito NOT NULL,
            voto INTEGER REFERENCE partidos)
        """,
        """CREATE TABLE caserio(
            codigo_caserio INTEGER PRIMARY KEY,
            nombre_caserio VARCHAR(80) NOT NULL,
            distrito_caserio VARCHAR(5) REFERENCE distrito NOT NULL)
        """,
        """CREATE TABLE poblacion_caserio(
            dni INTEGER PRIMARY KEY,
            codigo_verificacion_dni INTEGER,
            nombre_completo VARCHAR(100) NOT NULL,
            caserio_poblacioncaserio INTEGER REFERENCE caserio NOT NULL,
            voto INTEGER REFERENCE partidos)
        """)
    
    conn = None
    try:
        conn = psycopg2.connect(host="localhost",
                                database="votosvir",
                                user="postgres",
                                password="zxmloop0198",
                                port="5432")
        cur = conn.cursor()
        
        for command in commands:
            cur.execute(command)
            
        cur.close()
        conn.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def insert_departamento(codigo_departamento, nombre_departamento):
    sql = """INSERT INTO departamento (codigo_departamento, nombre_departamento)
             VALUES(%s, %s, %s);"""

    conn = None

    try:
        conn = psycopg2.connect(host="localhost",
                                database="votosvir",
                                user="postgres",
                                password="zxmloop0198",
                                port="5432")
        cur = conn.cursor()
        cur.execute(sql, (codigo_departamento, nombre_departamento))

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def insert_provincia(codigo_prov, nombre_prov):
    sql = """INSERT INTO departamento (codigo_departamento, nombre_departamento)
             VALUES(%s, %s);"""

    conn = None

    try:
        conn = psycopg2.connect(host="localhost",
                                database="votosvir",
                                user="postgres",
                                password="zxmloop0198",
                                port="5432")
        cur = conn.cursor()
        cur.execute(sql, (codigo_departamento, nombre_departamento))

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def insert_distrito(codigo_distri, nombre_distri, provincia_distri):
            
    sql = """INSERT INTO departamento (codigo_distri, nombre_distri, provincia_distri)
             VALUES(%s, %s, %s);"""

    conn = None

    try:
        conn = psycopg2.connect(host="localhost",
                                database="votosvir",
                                user="postgres",
                                password="zxmloop0198",
                                port="5432")
        cur = conn.cursor()
        cur.execute(sql, (codigo_distri, nombre_distri, provincia_distri))

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def partidos(codigo_partido, nombre_partido, candidato_presidencia, primera_vicepresidencia, segunda_vicepresidencia):

    sql = """INSERT INTO departamento (codigo_partido, nombre_partido, candidato_presidencia, primera_vicepresidencia, segunda_vicepresidencia)
             VALUES(%s, %s, %s, %s, %s);"""

    conn = None

    try:
        conn = psycopg2.connect(host="localhost",
                                database="votosvir",
                                user="postgres",
                                password="zxmloop0198",
                                port="5432")
        cur = conn.cursor()
        cur.execute(sql, (codigo_partido, nombre_partido, candidato_presidencia, primera_vicepresidencia, segunda_vicepresidencia))

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def insert_poblacion_capital_distrito(dni, codigo_verificacion_dni, nombre_completo, distrito_poblacion_capital, voto):

    sql = """INSERT INTO departamento (dni, codigo_verificacion_dni, nombre_completo, distrito_poblacion_capital, voto)
             VALUES(%s, %s, %s, %s, %s);"""

    conn = None

    try:
        conn = psycopg2.connect(host="localhost",
                                database="votosvir",
                                user="postgres",
                                password="zxmloop0198",
                                port="5432")
        cur = conn.cursor()
        cur.execute(sql, (dni, codigo_verificacion_dni, nombre_completo, distrito_poblacion_capital, voto))

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def insert_caserio(codigo_caserio, nombre_caserio, distrito_caserio):
            
    sql = """INSERT INTO departamento (codigo_caserio, nombre_caserio, distrito_caserio)
             VALUES(%s, %s, %s);"""

    conn = None

    try:
        conn = psycopg2.connect(host="localhost",
                                database="votosvir",
                                user="postgres",
                                password="zxmloop0198",
                                port="5432")
        cur = conn.cursor()
        cur.execute(sql, (codigo_caserio, nombre_caserio, distrito_caserio))

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def insert_poblacion_caserio(dni, codigo_verificacion_dni, nombre_completo, caserio_poblacioncaserio, voto):

    sql = """INSERT INTO departamento (dni, codigo_verificacion_dni, nombre_completo, caserio_poblacioncaserio, voto)
             VALUES(%s, %s, %s, %s, %s);"""

    conn = None

    try:
        conn = psycopg2.connect(host="localhost",
                                database="votosvir",
                                user="postgres",
                                password="zxmloop0198",
                                port="5432")
        cur = conn.cursor()
        cur.execute(sql, (dni, codigo_verificacion_dni, nombre_completo, caserio_poblacioncaserio, voto))

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()





"""def insert_curso(codigo_curso, nombre_curso):
    sql = """INSERT INTO curso_ej (codigo_curso, nombre_curso)
             VALUES(%s, %s);"""
             
    conn = None

    try:
        conn = psycopg2.connect(host="localhost",
                                database="mibasededatos",
                                user="postgres",
                                password=" ",
                                port="5433")
        cur = conn.cursor()
        cur.execute(sql, (codigo_curso, nombre_curso))

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def select_curso_id(curso):
    conn = None
    try:
        conn = psycopg2.connect(host="localhost",
                                database="mibasededatos",
                                user="postgres",
                                password=" ",
                                port="5433")
        cur = conn.cursor()
        
        cur.execute("SELECT codigo_curso FROM curso_ej WHERE nombre_curso=%s", (curso,))  
        codigo_curso = cur.fetchone()       
        cur.close()
        
        if conn is not None:
            conn.close()
            
        return codigo_curso
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

def select_estudiante_id(estudiante):
    conn = None
    try:
        conn = psycopg2.connect(host="localhost",
                                database="mibasededatos",
                                user="postgres",
                                password=" ",
                                port="5433")
        cur = conn.cursor()
        
        cur.execute("SELECT codigo_est FROM estudiante_ej WHERE nombre_est=%s", (estudiante,))    
        codigo_est = cur.fetchone() 
        cur.close()
        
        if conn is not None:
            conn.close()
            
        return codigo_est
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            
def insert_registro(curso_reg, estudiante_reg, nombre_reg, cal_reg):
    sql = """INSERT INTO registro (curso_reg, estudiante_reg, nombre_reg, cal_reg)
             VALUES(%s, %s, %s, %s);"""     
   
    conn = None

    try:
        conn = psycopg2.connect(host="localhost",
                                database="mibasededatos",
                                user="postgres",
                                password=" ",
                                port="5433")
        cur = conn.cursor()
        cur.execute(sql, (curso_reg, estudiante_reg, nombre_reg, cal_reg))

        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            
def select_registro(curso, estudiante):
    
    conn = None
    try:
        conn = psycopg2.connect(host="localhost",
                                database="mibasededatos",
                                user="postgres",
                                password=" ",
                                port="5433")
        cur = conn.cursor()
        
        cur.execute("SELECT codigo_curso FROM curso_ej WHERE nombre_curso=%s", (curso,))
        codigo_curso = cur.fetchone()
        
        cur.execute("SELECT codigo_est FROM estudiante_ej WHERE nombre_est=%s", (estudiante,))
        codigo_est = cur.fetchone()
        
        cur.execute("SELECT nombre_reg, cal_reg FROM registro WHERE curso_reg=%s AND estudiante_reg=%s",
                    (codigo_curso,codigo_est))
        
        registros = cur.fetchall()
        
        print(curso.upper())
        for registro in registros:
            print(registro)
            
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
"""
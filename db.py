import sqlite3
from sqlite3 import Error

def conectar():
    dbname= 'Ecommerce.db'
    conn= sqlite3.connect(dbname)
    return conn

def obtenerUsuarios(usuario):
    conn= conectar()
    sql = "select * from Usuarios where usuario= ?;"
    cursor= conn.execute(sql, (usuario, ))
    resultSet= cursor.fetchone()
    close_db(conn)
    return resultSet

def obtenerUsuariosID(userid):
    conn= conectar()
    sql = "select * from Usuarios where id= ?;"
    cursor= conn.execute(sql, (userid, ))
    resultSet= cursor.fetchone()
    close_db(conn)
    return resultSet

def obtenerProducto(codigo):
    conn= conectar()
    sql = "select * from Productos where codigo= ?;"
    cursor= conn.execute(sql, (codigo, ))
    resultSet= cursor.fetchone()
    close_db(conn)
    return resultSet

def obtenerProductoNom(nombre):
    conn= conectar()
    sql = "select * from Productos where nombre= ?;"
    cursor= conn.execute(sql, (nombre, ))
    resultSet= cursor.fetchone()
    close_db(conn)
    return resultSet

def obtenerProductoCate(categoria):
    conn= conectar()
    sql = "select * from Productos where categoria= ?;"
    cursor= conn.execute(sql, (categoria, ))
    resultSet= cursor.fetchall()
    close_db(conn)
    return resultSet

def obtenerAllProductos():
    conn= conectar()
    cursor= conn.execute("select * from Productos;")
    resultSet= cursor.fetchall()
    close_db(conn)
    return resultSet

def obtenerListaDes():
    conn= conectar()
    cursor= conn.execute("select * from ListaDeseos;")
    resultSet= cursor.fetchall()
    close_db(conn)
    return resultSet

def obtenerComentarios(idp):
    conn= conectar()
    sql = "select * from Comentarios where PRODUCTO=?;"
    cursor= conn.execute(sql,(idp, ))
    resultSet= cursor.fetchall()
    close_db(conn)
    return resultSet

def obtenerCarrito(id):
    conn=conectar()
    cursor = conn.execute('SELECT * FROM Carrito, Productos WHERE Carrito.PRODUCTO = PRODUCTOS.codigo AND Carrito.USUARIO = ? ', (id,))
    resultSet= cursor.fetchall()
    close_db(conn)
    return resultSet

def obtenerCompras(id):
    conn=conectar()
    cursor = conn.execute('SELECT * FROM Compras, Productos WHERE Compras.PRODUCTO = PRODUCTOS.codigo AND Compras.USUARIO = ? ', (id,))
    resultSet= cursor.fetchall()
    close_db(conn)
    return resultSet


def eliminarProducto(codigo):
    try:
        print("---------------",codigo)
        conn= conectar()
        sql = "delete from Productos where codigo = ?;"

        conn.execute(sql, (codigo, ))
        conn.commit()
        close_db(conn)

    except:
        return False

def eliminarListaDeseos(id):
    try:
        print("---------------",id)
        conn= conectar()
        sql = "delete from LISTAD where ID = ?;"
        conn.execute(sql, (id, ))
        conn.commit()
        close_db(conn)
    except:
        return False

def eliminarCarrito(id):
    try:
        print("---------------",id)
        conn= conectar()
        sql = "delete from Carrito where ID = ?;"
        conn.execute(sql, (id, ))
        conn.commit()
        close_db(conn)
    except:
        return False

def eliminarComentario(comentario):
    try:
        print("---------------",id)
        conn= conectar()
        sql = "delete from Comentarios where Comentario = ?;"
        conn.execute(sql, (comentario, ))
        conn.commit()
        close_db(conn)
    except:
        return False

def eliminarUsuario(user):
    try:
        if len(obtenerUsuarios(user)) > 0:
            print(user)
            conn= conectar()
            sql = "delete from Usuarios where usuario = ?;"
            conn.execute(sql, (user, ))
            conn.commit()
            close_db(conn)
        else:
            return False
    except:
        print("no se pudo")
        return False


def actualizarProducto(codi,nom, cate, cant,prec,desc):
    try:
        conn= conectar()
        sql = "update Productos set codigo = ?, nombre = ?, categoria = ?, cantidad = ?, precio = ?, descripcion = ? where codigo = ?;"

        conn.execute(sql, (codi,nom,cate,cant,prec,desc,codi))
        conn.commit()
        close_db(conn)

    except:
        return False

def actualizarUsuario(nom, corr, cont,user):
    try:
        conn= conectar()
        sql = "update Usuarios set usuario = ?, correo = ?, password = ? where usuario = ?;"
        conn.execute(sql, (nom,corr,cont,user))
        conn.commit()
        close_db(conn)

    except:
        return False

def registrarUsuario(nom, tel, correo,usua,contra):
    try :
        print(nom, tel, correo,usua,contra)
        conn=conectar()
        conn.execute("insert into Usuarios (nombre, telefono, correo, usuario, password)  values(?,?,?,?,?);", (nom, tel, correo,usua,contra))
        conn.commit()
        conn.close()
        return True
    except Error as error:
        print(error)
        return False

def agregarPBase(codi,nom, cate, cant,prec,desc,foto):
    try :
        print(codi,nom, cate, cant,prec,desc,foto)
        conn=conectar()
        conn.execute("insert into Productos (codigo, nombre, categoria, cantidad, precio, descripcion, foto)  values(?,?,?,?,?,?,?);", (codi,nom, cate, cant,prec,desc,foto))
        conn.commit()
        conn.close()
        return True
    except Error as error:
        print(error)
        return False

def agregarALista(id,codigo):
    try :
        print(id,codigo)
        conn=conectar()
        conn.execute("INSERT INTO LISTAD(USUARIO,PRODUCTO) VALUES(?,?);", (id, codigo))
        conn.commit()
        conn.close()
        return True
    except Error as error:
        print(error)
        return False


def agregarACarrito(id,codigo):
    try :
        print(id,codigo)
        conn=conectar()
        conn.execute("INSERT INTO Carrito(USUARIO,PRODUCTO) VALUES(?,?);", (id, codigo))
        conn.commit()
        conn.close()
        return True
    except Error as error:
        print(error)
        return False

def agregarComentario(id,user,comentario):
    try :
        print(id,comentario)
        conn=conectar()
        conn.execute("INSERT INTO Comentarios(PRODUCTO, USUARIO,COMENTARIO) VALUES(?,?,?);", (id,user, comentario))
        conn.commit()
        conn.close()
        return True
    except Error as error:
        print(error)
        return False

def agregarCompra(id,codigo):
    print(id,codigo)
    try:
        conn= conectar()
        conn.execute("INSERT INTO COMPRAS(USUARIO,PRODUCTO) VALUES(?,?);",(id, codigo))
        conn.commit()
        conn.close()
    except:
        return False

def vaciarCarrito(id):
    print(id)
    try:
        conn= conectar()
        sql = "delete from Carrito where usuario = ?;"
        conn.execute(sql, (id, ))
        conn.commit()
        conn.close()
    except:
        return False
        
def close_db(conn):
    print('Cerrando conexion a BDD')
    conn.close()

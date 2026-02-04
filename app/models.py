from app.database import get_connection

def crear_orden(cliente, descripcion):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ordenes (cliente, descripcion, estado) VALUES (?, ?, ?)",
        (cliente, descripcion, "Pendiente")
    )
    conn.commit()
    conn.close()

def listar_ordenes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ordenes")
    ordenes = cursor.fetchall()
    conn.close()
    return ordenes

def actualizar_estado(orden_id, nuevo_estado):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE ordenes SET estado = ? WHERE id = ?",
        (nuevo_estado, orden_id)
    )
    conn.commit()
    conn.close()

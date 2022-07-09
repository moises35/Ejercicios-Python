const sqlite3 = require('sqlite3');

const conexion = new sqlite3.Database('citas.db', (err) => {
    if (err) {
        console.log("Error de conexión a DB: " + err.message);
    } else {
        console.log("Conexión exitosa");
    }
});

const sql = `CREATE TABLE IF NOT EXISTS citas(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    nombre TEXT NOT NULL,
    detalle TEXT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    estado TEXT NOT NULL 
);`

conexion.run(sql);

module.exports = conexion;
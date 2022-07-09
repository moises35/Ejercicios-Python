const conexion = require('./../conection');

// Ver todos los registros de cita
const viewAll = (req, res) => {
    const sql = 'SELECT * FROM citas'
    conexion.all(sql, (res, err) => {
        if(err) {
            res.send('Ha ocurrido un error: ' + err)
        } else {
            res.send(res)
        }
    });
}   


// Registrar citas
const createCita = (req, res) => {
    const {name, detalle, fecha, hora, estado} = req.body.name;
    const sql = `INSERT INTO citas(nombre, detalle, fecha, hora, estado)
        VALUES('${name}', '${detalle}', '${fecha}', '${hora}', '${estado}')`
    conexion.run(sql, (err)=> {
        if(err) {
            res.send('Ha ocurrido un error: ' + err);
        } else {
            res.send('Registro exitoso');
        }
    });
}


// Ver citas de hoy
const viewToday = (req, res) => {
    const dia = req.body.dia;
    const sql =  `SELECT * FROM citas WHERE fecha = ${fecha} AND estado = 'Agendada'`
    conexion.all(sql, (res, err) => {
        if(err) {
            res.send('Ha ocurrido un error: ' + err)
        } else {
            res.send(res)
        }
    });
}


// Modificar citas
const updateCita = (req, res) => {
    const {id} = req.params
    const {estado} = req.body
    const sql = `UPDATE citas SET estado = '${estado}' WHERE id = '${id}'` 
    conexion.run(sql, (err)=> {
        if(err) {
            res.send('Ha ocurrido un error: ' + err);
        } else {
            res.send('Actualización exitosa');
        }
    });
}


// Eliminar citas
const deleteCita = (req, res) => {
    const {id} = req.params
    const sql = `DELETE FROM citas WHERE id = '${id}'` 
    conexion.run(sql, (err)=> {
        if(err) {
            res.send('Ha ocurrido un error: ' + err);
        } else {
            res.send('Eliminacion exitosa');
        }
    });
}


module.exports = {viewAll, createCita, viewToday, updateCita, deleteCita}
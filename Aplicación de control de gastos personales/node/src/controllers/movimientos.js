// Conexión a la BD
const conection = require('./../conection');

// Función callback para obtener todos los movimientos
const getAll = (req, res) => {
    const sql = 'SELECT * FROM movimientos';
    conection.query(sql, (err, result) => {
        if(err) {
            res.send('Ha ocurrrido un error: ' + err);
        } else {
            res.send(result);
        }
    });
};


// Función callback para obtener un movimiento por su id
const getById = (req, res) => {
    const id = req.params.id;
    const sql = `SELECT * FROM movimientos WHERE id = ${id}`;
    conection.query(sql, (err, result) => {
        if(err) {
            res.send('Ha ocurrrido un error: ' + err);
        } else {
            res.send(result);
        }
    });
};

// Función callback para crear un movimiento
const createMovimiento = (req, res) => {
    const movimiento = req.body;
    const sql = 'INSERT INTO movimientos SET ?';
    conection.query(sql, movimiento, (err, result) => {
        if(err) {
            res.send('Ha ocurrrido un error: ' + err);
        } else {
            res.send('Movimiento creado con éxito');
        }
    });
};

// Función callback para actualizar un movimiento
const updateById = (req, res) => {
    const id = req.params.id;
    const campo = req.body.campo;
    const new_valor = req.body.new_valor;
    const sql = `UPDATE movimientos SET ${campo} = ${new_valor} WHERE id = ${id}`;
    conection.query(sql, (err, result) => {
        if(err) {
            res.send('Ha ocurrrido un error: ' + err);
        } else {
            res.send('Movimiento actualizado con éxito');
        }
    });
};

// Función callback para eliminar un movimiento
const deleteById = (req, res) => {
    const id = req.params.id;
    const sql = `DELETE FROM movimientos WHERE id = ${id}`;
    conection.query(sql, (err, result) => {
        if(err) {
            res.send('Ha ocurrrido un error: ' + err);
        } else {
            res.send('Movimiento eliminado con éxito');
        }
    });
};


module.exports = {
    getAll, getById, createMovimiento, updateById, deleteById
}
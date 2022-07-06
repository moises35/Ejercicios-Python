// Importamos express
const express = require('express');

// Usamos las rutas de express
const routes = express.Router();

// Importamos los controladores
const controllersMovimientos = require('../controllers/movimientos');

// Agregamos las rutas
routes.get('/all', controllersMovimientos.getAll);
routes.get('/search/:id', controllersMovimientos.getById);
routes.post('/create', controllersMovimientos.createMovimiento);
routes.post('/update/:id', controllersMovimientos.updateById);
routes.post('/delete/:id', controllersMovimientos.deleteById);


module.exports = routes;
const express = require('express');
const router = express.Router();
const citasControllers = require('./../controllers/citas');

// Rutas de la app
router.get('/all', citasControllers.viewAll);
router.post('/create', citasControllers.createCita);
router.get('/viewToday', citasControllers.viewToday);
router.post('/update/:id', citasControllers.updateCita);
router.post('/delete/:id', citasControllers.deleteCita);

// Exportamos las rutas para poder utilizarlas
module.exports = router;
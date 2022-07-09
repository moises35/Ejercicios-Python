const express = require('express');
const app = express();
const citaRoutes = require('./routes/citas');

// Settings
app.set('PORT', 3000);

// Middleware
app.use(express.urlencoded({extended: false}));
app.use(express.json());

// Routes
app.use('/citas', citaRoutes);

// Server
app.listen(app.get('PORT'), ()=> {
    console.log(`Server running in port ${app.get('PORT')}`)
});
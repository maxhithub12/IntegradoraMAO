const express = require('express');
const router = express.Router();
const connection = require('../conexion');

router.get('/datos', (req, res) => {
  connection.query('SELECT * FROM quejas_sugerencias', (error, results) => {
    if (error) {
      console.error('Error al obtener los datos:', error);
      res.status(500).json({ error: 'Error del servidor' });
      return;
    }
    res.json(results);
  });
});

module.exports = router;

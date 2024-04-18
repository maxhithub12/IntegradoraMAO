const express = require("express");
const morgan = require("morgan");
const database= require("./database");
const swaggerSetup = require("./swagger");
const { MongoClient } = require("mongodb");


//Config inicial
const app = express();
app.set("port",4000);
app.listen(app.get("port"));
swaggerSetup(app); // Integra Swagger en tu aplicación

//Middlewares
app.use(morgan("dev"))

console.log("Escuchando al puerto "+app.get("port"));
console.log("http://localhost:4000/api-docs");

//Rutas
/**
 * @swagger
 * /usuarios:
 *   get:
 *     summary: Obtiene todos los usuarios
 *     responses:
 *       '200':
 *         description: Respuesta exitosa
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 type: object
 *                 properties:
 *                   Persona_ID:
 *                     type: integer
 *                   Nombre_Usuario:
 *                     type: string
 *                   Password:
 *                     type: string
 *                   Tipo:
 *                     type: string 
 *                   Estatus_Conexion:
 *                      type: string
 *                   Ultima_Conexion:
 *                      type: string
 *                      format: date-time
 *                   
 */
app.get("/usuarios", async (req, res) => {
    try {
        const connection = await database.getConnection();
        const result = await connection.query("SELECT * FROM usuarios ");
        console.log(result);
        res.json(result); // Envía los resultados como JSON al cliente
    } catch (error) {
        console.error("Error al consultar la base de datos:", error);
        res.status(500).send("Error interno del servidor");
    }
});

// Rutas conexion MONGODB
/**
 * @swagger
 * /seguimiento_queja:
 *   get:
 *     summary: Obtiene seguimiento de quejas
 *     responses:
 *       '200':
 *         description: Respuesta exitosa
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 type: object
 *                 properties:
 *                   _id:
 *                     type: string
 *                   queja_id:
 *                     type: string
 *                   fecha:
 *                     type: string
 *                     format: date-time
 *                   usuario:
 *                     type: object
 *                     properties:
 *                       nombre:
 *                         type: string
 *                       email:
 *                         type: string
 *                         format: email
 *                   empleado:
 *                     type: object
 *                     properties:
 *                       nombre:
 *                         type: string
 *                       email:
 *                         type: string
 *                         format: email
 *                   descripcion:
 *                     type: string
 *                   estatus:
 *                     type: string
 *                   tipo:
 *                     type: string
 *                   createdAt:
 *                     type: string
 *                     format: date-time
 *                   updatedAt:
 *                     type: string
 *                     format: date-time
 */
app.get("/seguimiento_queja", async (req, res) => {
    try {
        // Conexión a la base de datos MongoDB
        const client = new MongoClient("mongodb://localhost:27017", { useNewUrlParser: true, useUnifiedTopology: true });
        await client.connect();

        // Seleccionar la base de datos
        const database = client.db("bd_gimnasio_8b_idgs_MAO");
        
        // Obtener la colección de seguimiento de quejas
        const seguimientoCollection = database.collection("seguimiento_queja");
        
        // Consultar el seguimiento de quejas (limitando a 30 por ahora)
        const seguimiento = await seguimientoCollection.find().limit(30).toArray();
        console.log(seguimiento);
        
        // Enviar la respuesta JSON al cliente
        res.json(seguimiento);
        
        // Cerrar la conexión con la base de datos
        await client.close();
        
        
    } 
    catch (error) {
        console.error("Error al consultar la base de datos:", error);
        res.status(500).send("Error interno del servidor");
    }
});

import express from 'express' // framework de mode.js
import mongoose from 'mongoose' // librería para conectarse a mongo

const Animal = mongoose.model('Animal', new mongoose.Schema({
  tipo: String,
  estado: String,
})) //definimos modelo de atributos tipo y estado

const app = express() // creamos la app

mongoose.connect('mongodb://nico:password@monguito:27017/miapp?authSource=admin')
// url tiene usuario, password, la maquina, el puerto, la app y que se conecte como admin

//en la ruta main lista los animales
app.get('/', async (_req, res) => {
  console.log('listando... chanchitos...')
  const animales = await Animal.find();
  return res.send(animales)
})

// en la ruta crear crea un chanchito feliz y devuelve OK
app.get('/crear', async (_req, res) => {
  console.log('creando...')
  await Animal.create({ tipo: 'Chanchito', estado: 'Feliz' })
  return res.send('ok')
})

// el console log es para darse cuenta que corre
app.listen(3000, () => console.log('listening...'))
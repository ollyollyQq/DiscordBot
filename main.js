const {Client} = require('discord.js');
const client = new Client;
const settings = require('./settings.json')

client.on('ready',()=>{
    console.log(`${client.user.tag}`)
})
client.on('message',msg=>{
    if(msg.content.startsWith())
})
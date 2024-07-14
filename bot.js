const Discord = require('discord.js');
const roleId = 'target-role-id-here';

bot = new Discord.Client();

bot.on('message', (message) => {
    if (message.content == '!role') {
        message.member.roles.add(roleId);
    }
});

bot.login('your-bot-token-here');

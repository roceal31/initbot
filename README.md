# Soundbot

Discord bot that plays sound effects and music in a voice channel. Inspired by
https://github.com/stefangotz/initbot for our table top RPG game that we
currently play on Discord.

## Discord

The bot understands a few text commands.
These can be sent in any channel the bot user is a member of or as DMs.
Simply type `$help` to see what the bot can do for you.

### Turning the Soundboard On or Off

The Soundbot doesn't join a voice channel by default. To enable the bot to play
sounds, you need to turn the soundboard feature on:

```$soundboard on```

This will tell the bot to join the first voice channel it can find in the current
server.

Future improvements will allow you to direct the bot to a chosen voice channel.

To turn the soundboard feature off again, you can disconnect the bot with the
`$soundboard off` command.

### List Available Sounds

This bot contains a library of mp3 files that can be played over the voice channel.
To view the library, send the following command:

```$sounds```

The Soundbot will reply with a menu of the name of the sound and a brief description.

### Playing a Sound / Stopping Playback

You will need the name of the sound from the menu. For example:

```$sound typewriter```

The above command would start playing the sound from the library that has been labelled 'typewriter'.
If the name of the sound contains a space character, you'll need to enclose the name in quote
marks, e.g.

```$sound "babbling brook"```

If Soundbot doesn't recognise the name of the sound, you'll see an error message.

If a long-running sound needs to be stopped, you can use the `$shush` command to tell the bot to
stop playback.

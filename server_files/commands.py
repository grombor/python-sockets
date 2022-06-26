_commands = {
    "--quit": "stop server and client",
    "--stop": "stop server and client",
    "--help": "show this help",
    "--info": "show server version and creation date",
    "--uptime": "show server lifetime",
}


def get_commands():
    return _commands


def show_commands():
    text = "\n"
    for key, value in _commands.items():
        text += f"{key}: {value} \n"
    return text



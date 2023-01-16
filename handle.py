def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there'

    if p_message == 'help!':
        return "`This is a help message you can modify.`"

    elif p_message == 'owner':
        return 'Rayyan is the owner'


    elif p_message == 'kesy ho':
        return 'get a life bro'

    elif p_message == 'jee tha ro':
        return 'Agreed jee tha ro beta'

    elif p_message == 'sigma':
        return '''SIGMAAAAAAA
proud bot here!'''
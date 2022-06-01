def start_i(username,userdata,isadmin):
    msg = 'Bienvenido al BOT Pv V1 🛰\n'
    msg+= '🤖 Versión : V1\n\n'
    msg+= '👤 USUARIO : @' + str(username)+'\n\n'
    msg+= '🌐 IP : ' + str(userdata['ip'])+'\n'
    msg+= '➖ RANGO MINIMO : ' + str(userdata['rango_minimo'])+'\n'
    msg+= '➕ RANGO MAXIMO : ' + str(userdata['rango_maximo'])+'\n\n'
    msgAdmin = '👤 [USUARIO]'
    if isadmin:
        msgAdmin = '👑 [PROPIETARIO]'
    msg+= msgAdmin + '\n'
    return msg

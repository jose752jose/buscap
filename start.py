def start_i(username,userdata,isadmin):
    msg = 'Bienvenido al BOT Pv V1 π°\n'
    msg+= 'π€ VersiΓ³n : V1\n\n'
    msg+= 'π€ USUARIO : @' + str(username)+'\n\n'
    msg+= 'π IP : ' + str(userdata['ip'])+'\n'
    msg+= 'β RANGO MINIMO : ' + str(userdata['rango_minimo'])+'\n'
    msg+= 'β RANGO MAXIMO : ' + str(userdata['rango_maximo'])+'\n\n'
    msgAdmin = 'π€ [USUARIO]'
    if isadmin:
        msgAdmin = 'π [PROPIETARIO]'
    msg+= msgAdmin + '\n'
    return msg

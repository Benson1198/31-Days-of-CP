def taumBday(b, w, bc, wc, z):
    if(bc > wc+z):
        tc = (b+w)*wc + b*z

    elif(wc > bc+z):
        tc = (b+w)*bc + w*z

    else:
        tc = b*bc+w*wc
    
    return(tc)
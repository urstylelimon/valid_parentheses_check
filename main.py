s = "()"
length = len(s)
i = 1
first_index = s[0]
flag = False

while i < length:
    if (first_index == "(") :
        if (")" == s[i]):
            flag = True

            if( (i - 0) > 1 ):

                for z in range(2,i+1):
                    if (s[1] == "("):
                        if (")" == s[z]):
                            flag = True

                            if( (z - 0) > 1 ):

                                for x in range(3, z + 1):
                                    if (s[2] == "("):
                                        if (")" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "{"):
                                        if ("}" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "["):
                                        if ("]" == s[x]):
                                            flag = True
                                            break
                                break


                        else:
                            flag = False


                for z in range(2,i+1):
                    if (s[1] == "{"):
                        if ("}" == s[z]):
                            flag = True
                            if( (z - 0) > 1 ):

                                for x in range(3, z + 1):
                                    if (s[2] == "("):
                                        if (")" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "{"):
                                        if ("}" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "["):
                                        if ("]" == s[x]):
                                            flag = True
                                            break
                                break


                        else:
                            flag = False



                for z in range(2,i+1):
                    if (s[1] == "["):
                        if ("]" == s[z]):
                            flag = True

                            if( (z - 0) > 1 ):

                                for x in range(3, z + 1):
                                    if (s[2] == "("):
                                        if (")" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "{"):
                                        if ("}" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "["):
                                        if ("]" == s[x]):
                                            flag = True
                                            break
                                break


                        else:
                            flag = False

    if (first_index == "{"):
        if ("}" == s[i]):
            flag = True
            if ((i - 0) > 1):

                for z in range(2, i + 1):
                    if (s[1] == "("):
                        if (")" == s[z]):
                            flag = True

                            if ((z - 0) > 1):

                                for x in range(3, z + 1):
                                    if (s[2] == "("):
                                        if (")" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "{"):
                                        if ("}" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "["):
                                        if ("]" == s[x]):
                                            flag = True
                                            break
                                break


                        else:
                            flag = False

                for z in range(2, i + 1):
                    if (s[1] == "{"):
                        if ("}" == s[z]):
                            flag = True

                            if ((z - 0) > 1):

                                for x in range(3, z + 1):
                                    if (s[2] == "("):
                                        if (")" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "{"):
                                        if ("}" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "["):
                                        if ("]" == s[x]):
                                            flag = True
                                            break
                                break


                        else:
                            flag = False

                for z in range(2, i + 1):
                    if (s[1] == "["):
                        if ("]" == s[z]):
                            flag = True

                            if ((z - 0) > 1):

                                for x in range(3, z + 1):
                                    if (s[2] == "("):
                                        if (")" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "{"):
                                        if ("}" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "["):
                                        if ("]" == s[x]):
                                            flag = True
                                            break
                                break


                        else:
                            flag = False

    if (first_index == "["):
        if ("]" == s[i]):
            flag = True

            if ((i - 0) > 1):

                for z in range(2, i + 1):
                    if (s[1] == "("):
                        if (")" == s[z]):
                            flag = True

                            if ((z - 0) > 1):

                                for x in range(3, z + 1):
                                    if (s[2] == "("):
                                        if (")" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "{"):
                                        if ("}" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "["):
                                        if ("]" == s[x]):
                                            flag = True
                                            break
                                break


                        else:
                            flag = False

                for z in range(2, i + 1):
                    if (s[1] == "{"):
                        if ("}" == s[z]):
                            flag = True

                            if ((z - 0) > 1):

                                for x in range(3, z + 1):
                                    if (s[2] == "("):
                                        if (")" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "{"):
                                        if ("}" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "["):
                                        if ("]" == s[x]):
                                            flag = True
                                            break
                                break


                        else:
                            flag = False

                for z in range(2, i + 1):
                    if (s[1] == "["):
                        if ("]" == s[z]):
                            flag = True

                            if ((z - 0) > 1):

                                for x in range(3, z + 1):
                                    if (s[2] == "("):
                                        if (")" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "{"):
                                        if ("}" == s[x]):
                                            flag = True
                                            break

                                    if (s[2] == "["):
                                        if ("]" == s[x]):
                                            flag = True
                                            break
                                break


                        else:
                            flag = False




    i += 1

if( flag == True ):
    print("Valid")

if(flag == False):
    print("unvalid")
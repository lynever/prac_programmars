def solution(dartResult):
    tmplst, tmpstr, scrlst = [], '', []
    for idx, val in enumerate(dartResult):
        if val.isdigit():
            tmpstr += val
        elif val in 'SDT':
            if idx == len(dartResult) - 1 or dartResult[idx + 1].isdigit():
                tmpstr += val
                tmplst.append(tmpstr)
                tmpstr = ''
            else:
                tmpstr += val
        elif val in '*#':
            tmpstr += val
            tmplst.append(tmpstr)
            tmpstr = ''
    for scridx, scr in enumerate(tmplst):
        tmp = 0
        if len(scr) == 2:
            if scr[1] == 'S':
                tmp = int(scr[0])
            elif scr[1] == 'D':
                tmp = int(scr[0]) ** 2
            elif scr[1] == 'T':
                tmp = int(scr[0]) ** 3
        elif len(scr) == 3:
            if scr[2] in '*#':
                if scr[1] == 'S':
                    tmp = int(scr[0])
                elif scr[1] == 'D':
                    tmp = int(scr[0]) ** 2
                elif scr[1] == 'T':
                    tmp = int(scr[0]) ** 3
                if scr[2] == '#':
                    tmp *= -1
                elif scr[2] == '*':
                    if scridx != 0:
                        scrlst[scridx - 1] *= 2
                        tmp *= 2
                    else:
                        tmp *= 2
            else:
                if scr[2] == 'S':
                    tmp = int(scr[:2])
                elif scr[2] == 'D':
                    tmp = int(scr[:2]) ** 2
                elif scr[2] == 'T':
                    tmp = int(scr[:2]) ** 3
        elif len(scr) == 4:
            if scr[2] == 'S':
                tmp = int(scr[:2])
            elif scr[2] == 'D':
                tmp = int(scr[:2]) ** 2
            elif scr[2] == 'T':
                tmp = int(scr[:2]) ** 3
            if scr[3] == '#':
                tmp *= -1
            elif scr[3] == '*':
                if scridx != 0:
                    scrlst[scridx - 1] *= 2
                    tmp *= 2
                else:
                    tmp *= 2
        scrlst.append(tmp)
    return sum(scrlst)
def fehrest():
    fa=[]
    file=open('files/book.txt','r')
    while True:
        l=file.readline()
        if l=='':
            file.close()
            break
        z=l.split("_")
        fa.append(z)
    
    del[fa[0]]
    for i in range(len(fa)):
        del[fa[i][3]]
    return fa

def ozvlist():
    ta=[]
    file=open('files/ozvlist.txt','r')
    while True:
        l=file.readline()
        if l=='':
            file.close()
            break
        z=l.split("_-_")
        ta.append(z)
    del[ta[0]]
    for i in range(len(ta)):
        del[ta[i][8]]
    return ta

def tanzimat():
    global esm
    to=ozvlist()
    while True:
        for i in range (len(to)):
            if to[i][0]==esm:
                fard=i
                print("moshakhasate shoma:")
                print("\tnam karbari:\t",to[i][0])
                print("\tnam vaghe'i:\t",to[i][2])
                print("\tnam khanevadegi:",to[i][3])
                print("\te-mail:\t\t",to[i][4])
                if to[i][5]=='vared nashode':
                    print("\ttarikhe tavalod:",end='')
                    print(' vared nashode')
                else:
                    print("\ttarikhe tavalod:",end='')
                    print(to[i][5],end='')
                    print('/',end='')
                    print(to[i][6],end='')
                    print('/',end='')
                    print(to[i][7],end='')
                break
        bimasraf=input('\n(baraye didane edame enter ra bezanid)\n')
        print("""
/\/\dastoore morede nazar ra vared konid/\/\\
  1 avaz kardane nam karbari
  2 avaz kardane gozar vaje
  3 avaz kardane e-mail
  4 hazfe hesabe karbari
  x bazgasht be menu asli""")
        com6=input(" :")
        if com6=='x':
            break
        if com6=='4':
            j=0
            while True:
                if j>4:
                    print("~~~Shoma baraye bare panjom gozar vaje ra eshtebah vared kardid~~~")
                    break
                print("gozar vaje khod ra vared konid:('x' baraye bazgasht)")
                pa=input()
                if pa=='x':
                    break
                if to[fard][1]!=pa:
                    print("~~~Shoma",j,'bar gozar vaje ra eshtebah vared kardid~~~')
                    j+=1
                    continue
                print("""aya az hazf hesab karbari khod etminan darid?
baraye hazfe hesab 'y' va baraye bazgasht 'x' ra vared konid""")
                de=input(":")
                if de=='x':
                    break
                if de=='y':
                    to.remove(to[fard])
                    f=open('files/ozvlist.txt','w')
                    for i in range (len(to)):
                        sabt=to[i][0],'_-_',to[i][1],'_-_',to[i][2],'_-_',to[i][3],'_-_',to[i][4],'_-_',to[i][5],'_-_',to[i][6],'_-_',to[i][7],'_-_'
                        f.writelines('\n')
                        f.writelines(sabt)
                    f.close()
                    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~hesabe shoma hazf shod~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
                    start()
                break
                    
        if com6=='1':
            i=0
            while True:
                if i>5:
                    break
                fard2=input("nam karbari pishin ra vared konid:('x' baraye bazgasht)\n")
                if fard2=='x':
                    break
                if to[fard][0]!=fard2:
                    i+=1
                    print(i,"bar nam karbari ra eshtebah vared kardid")
                    continue
                a=input("nam karbari jadid ra vared konid:('x' baraye bazgasht)\n")
                if a=='x':
                    ok=0
                    break
                if len(a)<3 or len(a)>20:
                    print("##tedad horoof nam bayad bishaz 3 va kamtar az 20 bashad##")
                    continue
                k=0
                te=ozvlist()
                for i in range(len(te)):
                    if te[i][0]==a:
                        k=1
                if k==1:
                    print("""##in nam ghablan entekhab shode##
nam digari baraye khod entekhab konid""")
                    continue
                to[fard][0]=a
                esm=a
                f=open('files/ozvlist.txt','w')
                for i in range (len(to)):
                    sabt=to[i][0],'_-_',to[i][1],'_-_',to[i][2],'_-_',to[i][3],'_-_',to[i][4],'_-_',to[i][5],'_-_',to[i][6],'_-_',to[i][7],'_-_'
                    f.writelines('\n')
                    f.writelines(sabt)
                f.close()
                print("""~~~taghirat sabt shod~~~""")
                break

        if com6=='2':
            i=0
            while True:
                if i>5:
                    break
                fard2=input("gozavaje pishin ra vared konid:('x' baraye bazgasht)\n")
                if fard2=='x':
                    break
                if to[fard][1]!=fard2:
                    i+=1
                    print(i,"bar gozavaje ra eshtebah vared kardid")
                    continue
                b=input("gozavaje jadid ra vared konid:('x' baraye bazgasht)\n")
                if b=='x':
                    ok=0
                    break
                c=input("gozavaje jadid ra taid konid:('x' baraye bazgasht)\n")
                if c=='x':
                    ok=0
                    break
                if c!=b:
                    print("##gozar vaje haye voroodi yeksan nemibashad##")
                    continue
                if len(b)<5 or len(b)>12:
                    print("##tedad horoof gozar vaje bayad bishaz 5 va kamtar az 12 bashad##")
                    continue
                to[fard][1]=b
                f=open('files/ozvlist.txt','w')
                for i in range (len(to)):
                    sabt=to[i][0],'_-_',to[i][1],'_-_',to[i][2],'_-_',to[i][3],'_-_',to[i][4],'_-_',to[i][5],'_-_',to[i][6],'_-_',to[i][7],'_-_'
                    f.writelines('\n')
                    f.writelines(sabt)
                f.close()
                print("""~~~taghirat sabt shod~~~""")
                break

        if com6=='3':
            i=0
            while True:
                e=input("e-mail jadid ra vared konid:('x' baraye bazgasht)\n")
                if e=='x':
                    ok=0
                    break
                to[fard][4]=e
                f=open('files/ozvlist.txt','w')
                for i in range (len(to)):
                    sabt=to[i][0],'_-_',to[i][1],'_-_',to[i][2],'_-_',to[i][3],'_-_',to[i][4],'_-_',to[i][5],'_-_',to[i][6],'_-_',to[i][7],'_-_'
                    f.writelines('\n')
                    f.writelines(sabt)
                f.close()
                print("""~~~taghirat sabt shod~~~""")
                break

        x=input("""
agar mikhahid be menu ghabl bazgardid 'x' ra vared konid
""")
        if x=="x":
            break




def sabtenam():
    global esm
    while True:
        ok=1
        print("""(((ghesmat haye setare dar baraye sabtenam lazem ast.)))
baraye bargasht kelid (x) ra vared konid""")
        while True:
            a=input("* nam karbari:\n")
            if a=='x':
                ok=0
                break
            if len(a)<3 or len(a)>20:
                print("##tedad horoof nam bayad bishaz 3 va kamtar az 20 bashad##")
                continue
            k=0
            te=ozvlist()
            for i in range(len(te)):
                if te[i][0]==a:
                    k=1
            if k==1:
                print("""##in nam ghablan entekhab shode##
nam digari baraye khod entekhab konid""")
                continue
            break
        if ok==0:
            break
        while True:
            b=input("* gozar vaje:\n")
            if b=='x':
                ok=0
                break
            if len(b)<5 or len(b)>12:
                print("##tedad horoof gozar vaje bayad bishaz 5 va kamtar az 12 bashad##")
                continue
            c=input("* taide gozar vaje:\n")
            if c=='x':
                ok=0
                break
            if c!=b:
                print("##gozar vaje haye voroodi yeksan nemibashad##")
                continue
            break
        if ok==0:
            break
        while True:
            d=input("* nam vaghe'i:\n")
            if d=='x':
                ok=0
                break
            if len(a)<3 or len(a)>20:
                print("##tedad horoof nam bayad bishaz 3 va kamtar az 20 bashad##")
                continue
            break
        if ok==0:
            break
        while True:
            e=input("* nam khanevadeghi:\n")
            if e=='x':
                ok=0
                break
            if len(a)<3 or len(a)>20:
                print("##tedad horoof nam khanevadeghi bayad bishaz 3 va kamtar az 30 bashad##")
                continue
            break
        if ok==0:
            break
        while True:
            f=input("adress e-mail:\n")
            if f=='':
                f='vared nashode'
                break
            if f=='x':
                ok=0
                break
            kf=0
            te=ozvlist()
            for i in range (len(te)):
                if f==te[i][4]:
                    kf=1
            if kf==1:
                print("##in e-mail ghablan entekhab shode##")
                continue
            break
        if ok==0:
            break
        print('tavalod:')
        while True:
            g=input('\tsal:')
            if g=='':
                g='vared nashode'
                break
            if g=='x':
                ok=0
                break
            if len(g)!=4:
                print("##sal tavalood bayad 4 raghami bashad##")
                continue
            break
        if ok==0:
            break
        while True:
            h=input('\tmah:')
            if h=='':
                h='vared nashode'
                break
            if h=='x':
                ok=0
                break
            if len(h)!=1 and len(h)!=2:
                print("##mah tavalood 1 ya 2 raghami bashad##")
                continue
            break
        if ok==0:
            break
        while True:
            i=input('\trooz:')
            if i=='':
                i='vared nashode'
                break
            if i=='x':
                ok=0
                break
            if len(i)!=1 and len(i)!=2:
                print("##rooz tavalood 1 ya 2 raghami bashad##")
                continue
            break
        if ok==0:
            break

        co=1
        while co<5:
            j=input("* soale amniyati:\n2+2\n")
            if j=='x':
                ok=0
                break
            if j!='4':
                print("shoma ",co," bar soae amniyati ra eshtebah vared kardid")
                co+=1
                continue
            break
        if ok==0:
            break
        if g=='vared nashode':
            h='vared nashode'
            i='vared nashode'
        esm=a
        sabt=a,'_-_',b+'_-_',d,'_-_',e,'_-_',f,'_-_',g,'_-_',h,'_-_',i,'_-_'
        f=open('files/ozvlist.txt','a+')
        f.writelines('\n')
        f.writelines(sabt)
        f.close()
        print("""sabtenam ba mofaghiyat anjam shod""")
        main()
        break

def display(n):
    for i in range(len(n)):
        print("ketab: ",n[i][0],"\tnevisande: ",n[i][1],"\tsale enteshar:",n[i][2])



def sefareshi():
    while True:
        print("""
/\/\dastoore morede nazar ra vared konid/\/\\
  1 namayesh bar asase nam ketab(a-z)
  2 namayesh bar asase nam ketab(z-a)
  3 namayesh bar asase nam nevisande(a-z)
  4 namayesh bar asase nam nevisande(z-a)
  5 namayesh bar asase sal enteshar(soudi)
  6 namayesh bar asase sal enteshar(nozuli)
  x bazgasht be menu asli""")
        com4=input(":")
        if com4=='x':
            break
        if com4=='1':
            f1=fehrest()
            f1.sort()
            display(f1)
        if com4=='2':
            f1=fehrest()
            f1.sort(reverse=True)
            display(f1)
        if com4=='3':
            f1=fehrest()
            n1=len(f1)
            for i in range(0,n1):
                c=i+1
                while c<n1:
                    if f1[i][1]>f1[c][1]:
                        f1[i],f1[c]=f1[c],f1[i]
                    c=c+1
            display(f1)
        if com4=='4':
            f1=fehrest()
            n1=len(f1)
            for i in range(0,n1):
                c=i+1
                while c<n1:
                    if f1[i][1]<f1[c][1]:
                        f1[i],f1[c]=f1[c],f1[i]
                    c=c+1
            display(f1)
        if com4=='5':
            f1=fehrest()
            n1=len(f1)
            for i in range(0,n1):
                c=i+1
                while c<n1:
                    if int(f1[i][2])>int(f1[c][2]):
                        f1[i],f1[c]=f1[c],f1[i]
                    c=c+1
            display(f1)
        if com4=='6':
            f1=fehrest()
            n1=len(f1)
            for i in range(0,n1):
                c=i+1
                while c<n1:
                    if int(f1[i][2])<int(f1[c][2]):
                        f1[i],f1[c]=f1[c],f1[i]
                    c=c+1
            display(f1)
        x=input("""
agar mikhahid be menu ghabl bazgardid 'x' ra vared konid
""")
        if x=="x":
            break




def superimpose():
    co=0
    su=[]
    while True:
        print('''
be tatib nam v nevisande v sale enteshare ketab ra vared konid
(be manzure bazgasht b menu asli x ra vared konid)
''')
        temporary=[]
        while True:
            ketab=input('nam ketab:\n')
            if len(ketab)>30:
                print("""###..KHATA..###
  (had mojaze nam ketab 30 harf ast)
""")
                continue
            if ketab!="" and ketab!=' ':
                break
            print("""###..KHATA..###
(nami vared nakardid)""")
        if ketab=='x':
            break
        while True:
            nevi=input('nam nevisande\n')
            if len(nevi)>30:
                print("""###..KHATA..###
  (had mojaze nam nevisande 30 harf ast)
""")
                continue
            if nevi!="" and nevi!=' ':
                break
            print("""###..KHATA..###
(nami vared nakardid)""")
        if nevi=='x':
            break
        while True:
            enteshar=input('sale nashr\n')
            if len(enteshar)>4:
                print("""###..KHATA..###
  (had mojaze sale enteshar '4' ragham ast)
""")
                continue
            if enteshar!="" and enteshar!=' ':
                break
            print("""###..KHATA..###
(adadi vared nakardid)""")
        if enteshar=='x':
            break
        temporary.append(ketab)
        temporary.append(nevi)
        temporary.append(enteshar)
        su.append(temporary)
        co=1
    if co==1:
        f=open('files/book.txt','a+')
        for i in range (len(su)):
            f.write('\n')
            x=su[i][0]
            y=su[i][1]
            z=su[i][2]
            ketab2=x,'_',y,'_',z,'_'
            f.writelines(ketab2)
        f.close()
        print('\n',"~~~taghirat soorat gereft~~~",'\n')





def kavosh():
    while True:
        print("""
/\/\dastoore morede nazar ra vared konid/\/\\
  1 kavosh bar asase nam ketab
  2 kavosh bar asase nam nevisande
  3 kavosh bar asase sale enteshar
  x bazgasht be menu asli""")
        com5=input(" :")
        if com5=='x':
            break
        if com5=='1':
            be=1
            while True:
                target=input("""
(baraye bazgasht be menu ghabl 'x' ra vared konid)
nam ketab
 :""")
                if target=='' and target=='':
                    print('\n\n###..KHATA..###\nloghati baraye kavosh vared nashod')
                    continue
                if target=='x':
                    break
                f1=fehrest()
                be=2
                for i in range(len(f1)):
                    f2=f1[i][0]
                    f3=f2.find(target)
                    if f3!=-1:
                        print("ketab: ",f1[i][0],"\tnevisande: ",f1[i][1],"\tsale enteshar:",f1[i][2])
                        be=3
                if be==2:
                    print("ketabi ba in moshakhasaat peyda nashod")
                break     
        if com5=='2':
            be=1
            while True:
                target=input("""
(baraye bazgasht be menu ghabl 'x' ra vared konid)
nam nevisande
 :""")
                if target=='' and target=='':
                    print('\n\n###..KHATA..###\nloghati baraye kavosh vared nashod')
                    continue
                if target=='x':
                    break
                f1=fehrest()
                be=2
                for i in range(len(f1)):
                    f2=f1[i][1]
                    f3=f2.find(target)
                    if f3!=-1:
                        print("ketab: ",f1[i][0],"\tnevisande: ",f1[i][1],"\tsale enteshar:",f1[i][2])
                        be=3
                if be==2:
                    print("ketabi ba in moshakhasaat peyda nashod")
                break
        if com5=='3':
            be=1
            while True:
                target=input("""
(baraye bazgasht be menu ghabl 'x' ra vared konid)
sale enteshar
 :""")
                if target=='' and target=='':
                    print('\n\n###..KHATA..###\nadadi baraye kavosh vared nashod')
                    continue
                if target=='x':
                    break
                f1=fehrest()
                be=2
                for i in range(len(f1)):
                    f2=f1[i][2]
                    f3=f2.find(target)
                    if f3!=-1:
                        print("ketab: ",f1[i][0],"\tnevisande: ",f1[i][1],"\tsale enteshar:",f1[i][2])
                        be=3
                if be==2:
                    print("ketabi ba in moshakhasaat peyda nashod")
                break
        x=input("""
agar mikhahid be menu ghabl bazgardid 'x' ra vared konid
""")
        if x=="x":
            break




def deletion():
    while True:
        print("""
/\/\dastoore morede nazar ra vared konid/\/\\
  1 hazf bar asase nam ketab
  2 hazf bar asase nam nevisande
  3 hazf bar asase sale enteshar
  x bazgasht be menu asli""")
        com5=input(" :")
        if com5=='x':
            break
        be=1
        f1=fehrest()
        transcript=f1[:]
        if com5=='1':
            while True:
                target=input("""
(baraye bazgasht be menu ghabl 'x' ra vared konid)
nam ketab
 :""")
                if target=='' and target=='':
                    print('\n\n###..KHATA..###\nloghati vared nashod')
                    continue
                if target=='x':
                    break
                be=2
                hazf=0
                for i in range(len(f1)):
                    f2=f1[i][0]
                    f3=f2.find(target)
                    if f3!=-1:
                        print("ketab: ",f1[i][0],"\tnevisande: ",f1[i][1],"\tsale enteshar:",f1[i][2])
                        print("baraye hazfe ketab 'y' ra vared konid")
                        hazf=input(":")
                        be=3
                        if hazf=='y':
                            transcript.remove(transcript[i])
                            print("~~~hazf shod~~~")
                            break
                        print("~~~ketab az fehrest hazf nashod~~~",'\n','\n')
                if be==2:
                    print("ketabi ba in moshakhasaat peyda nashod")
                break
        if com5=='2':
            while True:
                target=input("""
(baraye bazgasht be menu ghabl 'x' ra vared konid)
nam nevisande
 :""")
                if target=='' and target=='':
                    print('\n\n###..KHATA..###\nloghati vared nashod')
                    continue
                if target=='x':
                    break
                be=2
                hazf=0
                for i in range(len(f1)):
                    f2=f1[i][1]
                    f3=f2.find(target)
                    if f3!=-1:
                        print("ketab: ",f1[i][0],"\tnevisande: ",f1[i][1],"\tsale enteshar:",f1[i][2])
                        print("baraye hazfe ketab 'y' ra vared konid")
                        hazf=input(":")
                        be=3
                        if hazf=='y':
                            transcript.remove(transcript[i])
                            print("~~~hazf shod~~~")
                            break
                        print("~~~ketab az fehrest hazf nashod~~~",'\n','\n')
                if be==2:
                    print("ketabi ba in moshakhasaat peyda nashod")
                break
        if com5=='3':
            while True:
                target=input("""
(baraye bazgasht be menu ghabl 'x' ra vared konid)
sale entesar
 :""")
                if target=='' and target=='':
                    print('\n\n###..KHATA..###\nloghati vared nashod')
                    continue
                if target=='x':
                    break
                be=2
                hazf=0
                for i in range(len(f1)):
                    f2=f1[i][2]
                    f3=f2.find(target)
                    if f3!=-1:
                        print("ketab: ",f1[i][0],"\tnevisande: ",f1[i][1],"\tsale enteshar:",f1[i][2])
                        print("baraye hazfe ketab 'y' ra vared konid")
                        hazf=input(":")
                        be=3
                        if hazf=='y':
                            transcript.remove(transcript[i])
                            print("~~~hazf shod~~~")
                            break
                        print("~~~ketab az fehrest hazf nashod~~~",'\n','\n')
                if be==2:
                    print("ketabi ba in moshakhasaat peyda nashod")
                break
        else:
            x=input("""
agar mikhahid be menu ghabl bazgardid 'x' ra vared konid
""")
            if x=="x":
                break
        f=open('files/book.txt','w')
        for j in range (len(transcript)):
            k=transcript[j][0],'_',transcript[j][1],'_',transcript[j][2],'_'
            f.write('\n')
            f.writelines(k)
        f.close()


 
def backup():
    k=0
    while True:
        print("""

       ######>>>>EKHTAR<<<<######
aya az gereftane file poshtiban etminan darid?             
dar soorate poshtiban giri file poshtibane jadid jaygozin file poshtiban ghabl mishavad.
baraye gereftane file poshtiban 'y' va baraye bazgasht be menu ghabl 'x' ra vared konid.
(baraye bazgasht be menu ghabl 'x' ra vared konid):""")
        b=input()
        if b=='x':
            break
        if b=='y':
            fa=[]
            file=open('files/book.txt','r')
            while True:
                l=file.readline()
                if l=='':
                    file.close()
                    break
                fa.append(l)
            file=open('files/backup book.txt','w')
            for i in range(len(fa)):
                file.writelines(fa[i])
            file.close()
            k=1
        if k==1:
            bikhodi=input("""
~~~~noskheye poshtiban zakhire shod~~~~
baraye bazgasht be menu enter re bezanid
""")
            break


def restore():
    k=0
    while True:
        print("""

        ######>>>>EKHTAR<<<<######
aya az ejra kardane noskhe poshtiban etminan darid?             
dar soorate Restore kardane barname ,fehreste poshtiban jaygozin fehreste konooni mishavad.
baraye Restore kardane barname 'y' va baraye bazgasht be menu ghabl 'x' ra vared konid.
(baraye bazgasht be menu ghabl 'x' ra vared konid):""")
        b=input()
        if b=='x':
            break
        if b=='y':
            fa=[]
            file=open('files/backup book.txt','r')
            while True:
                l=file.readline()
                if l=='':
                    file.close()
                    break
                fa.append(l)
            file=open('files/book.txt','w')
            for i in range(len(fa)):
                file.writelines(fa[i])
            file.close()
            k=1
        if k==1:
            bikhodi=input("""
 ~~~~~noskheye poshtiban ejra shod~~~~~
baraye bazgasht be menu enter re bezanid
""")
            break
def start():
    global esm
    print("""♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
be systeme ketabkhane daneshgahi khosh amadid
♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥""")
    wrang=0
    while True:
        print("""
1 VOROOD
2 sabtenam
x boroon raf""")
        com1=input()
        if com1=='x':
            break
        if com1=='1':
            print("""
nam karbari:""")
            karbar=input()
            print("""gozar vaje:""")
            pas=input()
            s=ozvlist()
            ok=0
            ko=0
            for i in range(len(s)):
                if s[i][0]==karbar:
                    ok=1
                    esm=s[i][0]
                if s[i][1]==pas:
                    ko=1
            if ok==1 and ko==1:
                main()
                break
            wrang+=1
            if wrang>=5:
                print("shoma baraye bar panjom gozavaje ra eshtebah vared kardid")
                print("~~~~~~~~PAYAN~~~~~~~~~")
                break
            else:
                print("""  ###..KHATA..###
shoma nam karbari ya gozar vaje khod ra eshtebah vared karde'id
(tavajoh: barname be bozorg v koochak boodane horoof hasas ast)\n""",wrang,"bar gozavaje ra eshtebah vared kardid")


        if com1=='2':
            sabtenam()
            break

def main():
    while True:
        print("""
 /\/\/\menu/\/\/\\
 1 namayeshe fehrest
 2 sefareshi sazy namayeshe fehrest
 3 afzoodane ketab be fehrest
 4 hazf ketab az fehrest
 5 KAVOSH
 6 BACKUP
 7 RESTORE
 8 tanzimate hesab karbari
 x boroon raft""")
        com3=input(":")
        if com3=='1':
            display(fehrest())
        if com3=='2':
            sefareshi()
        if com3=='3':
            superimpose()
        if com3=='4':
            deletion()
        if com3=='5':
            kavosh()
        if com3=='6':
            backup()
        if com3=='7':
            restore()
        if com3=='8':
            tanzimat()
        if com3=='x':
            print("~~~~~~~~PAYAN~~~~~~~~~")
            break
        x=input("""
agar mikhahid az barname kharej shavid 'x' ra vared konid
""")
        if x=="x":
            print("~~~~~~~~PAYAN~~~~~~~~~")
            break
start()

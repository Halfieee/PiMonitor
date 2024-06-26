

def get_output(command):
        result = os.popen(command)
        output = result.read().strip()
        return output

def ram():
    ramfree = get_output('sh scripts/ramfree.sh')
    ramtotal = get_output('sh scripts/ramtotal.sh')
    ramfree = int(ramtotal) - int(ramfree)
    return str((int(ramfree / int(ramtotal) * 100))) + "%"
        
def cpu():
    return str(100 - int(get_output('sh scripts/cpu.sh'))) + '%'

def temp()
    return str(get_output('sh scripts/temp.sh'))

def mumble_status():
    if get_output('sh scripts/mumble.sh') == 'running':
        return 'Running'
    else:
        return 'u dun goofed'
if __name__ == '__main__':
    while True:
        os.system('clear')
        print(bold + green + "   .~~.   .~~.       " + red + "RAM Usage:")
        print(green + "  '. \ ' ' / .'      " + clear + ram())
        print(red2 + "   .~ .~~~..~.       " + cyan + "CPU Usage:" + clear)
        print(red2 + "  : .~.'~'.~. :      " + clear + cpu())
        print(red2 + " ~ (   ) (   ) ~     " + magenta + "Mumble Status:" + clear)
        print(red2 + "( : '~'.~.'~' : )    " + clear + mumble_status())
        print(red2 + " ~ .~ (   ) ~. ~     " + clear + )
        print(red2 + "  (  : '~' :  )      ")
        print(red2 + "   '~ .~~~. ~'       ")
        print(red2 + "       '~'           ")

        time.sleep(20) #refresh rate
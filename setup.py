#!/usr/bin/python3

import uuid
import json
from pathlib import Path
import re

def is_valid_domain(domain):
    # 使用正则表达式匹配域名格式
    pattern = r"^(?:(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$"
    
    if re.match(pattern, domain):
        return True
    else:
        return False


DEFAULT_DOMAIN = '<EXAMPLE.COM>'

def handle_uuid():
    # LOAD CONFIG FILE

    path = Path(__file__).parent.joinpath('v2ray/config/config.json')
    file = open(str(path), 'r', encoding='utf-8')
    config = json.load(file)

    # INPUT: UPSTREAM UUID

    defaultUUID = config['inbounds'][0]['settings']['clients'][0]['id']
    if defaultUUID == '<UPSTREAM-UUID>':
        message = "Upstream UUID: (Leave empty to generate a random one)\n"
    else:
        message = f"Upstream UUID: (Leave empty to use `{defaultUUID}`)\n"

    upstreamUUID = input(message)
    if upstreamUUID == '':
        if defaultUUID == '<UPSTREAM-UUID>':
            upstreamUUID = str(uuid.uuid4())
        else:
            upstreamUUID = defaultUUID

    config['inbounds'][0]['settings']['clients'][0]['id'] = upstreamUUID

    # SAVE CONFIG FILE

    content = json.dumps(config, indent=2)
    open(str(path), 'w', encoding='utf-8').write(content)

    # PRINT OUT RESULT

    print('Upstream UUID:')
    print(upstreamUUID)
    
def handle_domain():    
    
    path = Path(__file__).parent.joinpath('caddy/Caddyfile')
    file = open(str(path), 'r', encoding='utf-8')
    lines=file.readlines()   
    file.close()
    
    old_domain=lines[0].replace('{','').strip()    
    
    
    message = f"Setup the domain name: (such as t.example.com, Current is {old_domain})\n"
    domain=input(message)
    
    if domain=='':
        domain=old_domain    
    
    while not is_valid_domain(domain):
        print("Domain:{} is not valid".format(domain))
        domain=input(message)     
    
    out=open(str(path), 'w', encoding='utf-8')
    out.write("%s {\n"%format(domain))
    out.writelines(lines[1:])    
    
    print("Domain:\n{}\n".format(domain))
        
    pass    

if __name__ == '__main__':
    handle_domain()
    handle_uuid()
    
    print('\nDone!')

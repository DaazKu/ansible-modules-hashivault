
#!/usr/bin/env python
DOCUMENTATION = '''
---
module: hashivault_token_lookup
version_added: "2.2.0"
short_description: Hashicorp Vault token create module
description:
    - Module to create tokens in Hashicorp Vault.
options:
    url:
        description:
            - url for vault
        default: to environment variable VAULT_ADDR
    verify:
        description:
            - verify TLS certificate
        default: to environment variable VAULT_SKIP_VERIFY
    authtype:
        description:
            - "authentication type to use: token, userpass, github, ldap"
        default: token
    token:
        description:
            - token for vault
        default: to environment variable VAULT_TOKEN
    accessor:
        description:
            - accessor-token for vault
    username:
        description:
            - username to login to vault.
        default: False
    password:
        description:
            - password to login to vault.
        default: False
    name:
        description:
            - user name to create.
        default: False
    pass:
        description:
            - user to create password.
        default: False
'''
EXAMPLES = '''
---
- hosts: localhost
  tasks:
'''


def main():
    argspec = hashivault_argspec()
    argspec['accessor'] = dict(required=False, type='str')
    argspec['wrap_ttl'] = dict(required=False, type='str')
    module = hashivault_init(argspec)
    result = hashivault_token_lookup(module.params)
    if result.get('failed'):
        module.fail_json(**result)
    else:
        module.exit_json(**result)


from ansible.module_utils.basic import *
from ansible.module_utils.hashivault import *


@hashiwrapper
def hashivault_token_lookup(params):
    client = hashivault_auth_client(params)
    accessor = params.get('accessor')
    token = params.get('token')
    wrap_ttl = params.get('wrap_ttl')
    lookup = client.lookup_token(token=token, accessor=accessor, wrap_ttl=wrap_ttl)
    return {'changed': False, 'lookup': lookup}

if __name__ == '__main__':
    main()

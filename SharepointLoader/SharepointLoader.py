from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext



def get_sharepoint_context_using_user():
    sharepoint_url = 'your url'
    client_credentials = UserCredential('username','password')
    ctx = ClientContext(sharepoint_url).with_credentials(client_credentials)
    return ctx
def create_sharepoint_directory(dir_name: str):
    if dir_name:
        ctx = get_sharepoint_context_using_user()
        result = ctx.web.folders.add(f'{dir_name}').execute_query()
        if result:
            relative_url = f'{dir_name}'
            return relative_url


create_sharepoint_directory('Folder name')
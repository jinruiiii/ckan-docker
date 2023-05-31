import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint, render_template
from ckan.types import AuthResult, Context
from typing import Any, Optional,cast
from ckan.types import (
    AuthFunction, AuthResult, Context, ContextValidator, DataDict)
from ckan.logic.auth import get_group_object

def test():
    '''A simple view function'''
    return render_template("home/layout1.html")


# curators have the authority to manage groups

def group_create(context: Context,
                 data_dict: Optional[DataDict] = None) -> AuthResult:
    user_name: str = context["user"]
    try:
        members = toolkit.get_action('member_list')(
            {},
            {'id': 'curators', 'object_type': 'user'})
    except toolkit.ObjectNotFound:
        # The curators group doesn't exist.
        return {'success': False,
                'msg': "The curators groups doesn't exist, so only sysadmins "
                       "are authorized to create groups."}    
    member_ids = [member_tuple[0] for member_tuple in members]

    convert_user_name_or_id_to_id = cast(
        ContextValidator,
        toolkit.get_converter('convert_user_name_or_id_to_id'))
    try:
        user_id = convert_user_name_or_id_to_id(user_name, context)
    except toolkit.Invalid:
        # The user doesn't exist (e.g. they're not logged-in).
        return {'success': False,
                'msg': 'You must be logged-in as a member of the curators '
                       'group to create new groups.'}

    if user_id in member_ids:
        return {'success': True}
    else:
        return {'success': False,
                'msg': 'Only curators are allowed to create groups'}



# no one can create organizations other than the sysadmin    
def organization_create(context: Context,
                        data_dict: Optional[DataDict] = None) -> AuthResult:
    return {'success': False,
            'msg': "No one is allowed to create organizations other than sysadmin"}

def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action("group_list")({},{"sort":"package_count desc",'all_fields': True})
    groups = groups[:10]
    return groups

def organizations():
    '''Return datasets titles'''

    func = toolkit.get_action("organization_list")
    organizations = func({},{"all_fields":True})
    return organizations

class TestPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):

    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.ITemplateHelpers)


    # IConfigurer
    def update_config(self, config_):

        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic','helloword_extension')
        toolkit.add_resource('assets','test')

    #IBlueprint
    def get_blueprint(self):

        # Create Blueprint for plugin
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = 'templates'
        # Add plugin url rules to Blueprint object
        blueprint.add_url_rule(
            u'/test', 
            u'/test', 
            test,
            methods=['GET']
        )
        return blueprint
    #IAuth
    def get_auth_functions(self):
        return {"group_create": group_create,  "organization_create":organization_create}
    
    #ITemplate
    def get_helpers(self):
        return {"test_most_popular_groups":most_popular_groups, "test_organizations":organizations}
    